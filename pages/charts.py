import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from scipy.stats import gaussian_kde
import numpy as np

st.set_page_config(page_title="Entrepreneurship Insights", layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style/style.css")

@st.cache_data
def load_data():
    return pd.read_excel("education_career_success.xlsx")

df = load_data()


# Sidebar Filters
st.sidebar.title("Filters")

# Gender Filter - Multiselect
gender_options = sorted(df['Gender'].dropna().unique())
selected_genders = st.sidebar.multiselect("Select Gender(s)", gender_options, default=gender_options)

# Handle Gender Filter
if not selected_genders:
    st.sidebar.warning("⚠️ No gender selected. Using full data. Please choose at least one option.")
    gender_filtered = df  # fallback to full data to avoid crash
elif 'All' in selected_genders:
    gender_filtered = df
else:
    gender_filtered = df[df['Gender'].isin(selected_genders)]

# Job Level Filter
job_levels = sorted(df['Current_Job_Level'].dropna().unique())
selected_level = st.sidebar.selectbox("Select Job Level", job_levels)

# Age Filter
min_age, max_age = int(df['Age'].min()), int(df['Age'].max())
age_range = st.sidebar.slider("Select Age Range", min_value=min_age, max_value=max_age, value=(min_age, max_age))

# Check if only one age selected
if age_range[0] == age_range[1]:
    st.sidebar.warning(f"⚠️ Only one age ({age_range[0]}) selected. Using full age range.")
    age_range = (min_age, max_age)

# Entrepreneurship Status Filter - Individual Checkboxes
st.sidebar.markdown("**Select Entrepreneurship Status**")
show_yes = st.sidebar.checkbox("Yes", value=True)
show_no = st.sidebar.checkbox("No", value=True)

selected_statuses = []
if show_yes:
    selected_statuses.append("Yes")
if show_no:
    selected_statuses.append("No")

if not (show_yes or show_no):
    st.sidebar.warning("⚠️ No status selected. Using full data. Please choose at least one option.")
    selected_statuses = ['Yes', 'No']

color_map = {'Yes': '#FFD700', 'No': '#004080'}

# Main Tabs
graph_tab = st.tabs(["📈 Demographics", "📊 Job Offers"])

# === TAB 1 (Demographics) ===
with graph_tab[0]:
    st.title("Demographics")

    chart_option = st.selectbox("Select Variable for Visualization", ['Gender Distribution', 'Field of Study'])

    df_demo = gender_filtered[
        (gender_filtered['Current_Job_Level'] == selected_level) &
        (gender_filtered['Age'].between(age_range[0], age_range[1])) &
        (gender_filtered['Entrepreneurship'].isin(selected_statuses))
    ]

    if df_demo.empty:
        st.warning("⚠️ Not enough data to display charts. Please adjust the filters.")
    else:
        if chart_option == 'Gender Distribution':
            with st.container():
                st.markdown("""<div style="border: 1px solid #e0e0e0; border-radius: 10px; padding: 15px; margin-top: 10px; margin-bottom: 30px;">
                    <div style="display: flex; justify-content: space-around; text-align: center; line-height: 1.3;">
                        <div>
                            <div style="font-size: 14px; color: #555;">Total Records</div>
                            <div style="font-size: 28px;">{}</div>
                        </div>
                        <div>
                            <div style="font-size: 14px; color: #555;">Median Age</div>
                            <div style="font-size: 28px;">{:.1f}</div>
                        </div>
                        <div>
                            <div style="font-size: 14px; color: #555;">% Female</div>
                            <div style="font-size: 28px;">{:.1f}%</div>
                        </div>
                    </div></div>
                """.format(len(df_demo), df_demo['Age'].median(),
                           (df_demo['Gender'] == 'Female').mean() * 100),
                unsafe_allow_html=True)

        else:
            top_fields = df_demo['Field_of_Study'].value_counts().head(3).index.tolist()
            display_fields = ", ".join(top_fields) if top_fields else "N/A"
            with st.container():
                st.markdown("""<div style="border: 1px solid #e0e0e0; border-radius: 10px; padding: 15px; margin-top: 10px; margin-bottom: 30px;">
                    <div style="display: flex; justify-content: space-around; text-align: center; line-height: 1.3;">
                        <div>
                            <div style="font-size: 14px; color: #555;">Total Records</div>
                            <div style="font-size: 28px;">{}</div>
                        </div>
                        <div>
                            <div style="font-size: 14px; color: #555;">Top 3 Fields</div>
                            <div style="font-size: 20px;">{}</div>
                        </div>
                    </div></div>
                """.format(len(df_demo), display_fields),
                unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            fig_density = go.Figure()
            group_col = 'Gender' if chart_option == 'Gender' else 'Field_of_Study'
            title = f"Age Distribution by {group_col.replace('_', ' ')}"
            categories = df_demo[group_col].dropna().unique()

            for cat in categories:
                age_data = df_demo[df_demo[group_col] == cat]['Age']
                if len(age_data) > 1:
                    kde = gaussian_kde(age_data)
                    x_vals = np.linspace(age_range[0], age_range[1], 100)
                    y_vals = kde(x_vals)
                    fig_density.add_trace(go.Scatter(
                        x=x_vals,
                        y=y_vals,
                        mode='lines',
                        name=str(cat),
                        fill='tozeroy'
                    ))

            fig_density.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                title=title,
                xaxis_title="Age",
                yaxis_title="Density",
                height=500,
                margin=dict(t=40, l=40, r=40, b=80),
                legend=dict(orientation="h", yanchor="bottom", y=-0.35, xanchor="center", x=0.5)
            )
            st.plotly_chart(fig_density, use_container_width=True)

        with col2:
            if chart_option == 'Gender Distribution':
                counts = df_demo['Gender'].value_counts().reset_index()
                counts.columns = ['Gender', 'Count']
                labels, values = counts['Gender'], counts['Count']
            else:
                counts = df_demo['Field_of_Study'].value_counts().reset_index()
                counts.columns = ['Field of Study', 'Count']
                labels, values = counts['Field of Study'], counts['Count']

            fig_donut = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.5)])
            fig_donut.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                title=f"{chart_option} Distribution (Donut Chart)",
                height=350,
                margin=dict(t=40, l=40, r=40, b=40),
                showlegend=True
            )
            st.plotly_chart(fig_donut, use_container_width=True)

# === TAB 2 (Job Offers) ===
with graph_tab[1]:
    st.title("Job Offers")

    df_filtered = gender_filtered[
        (gender_filtered['Current_Job_Level'] == selected_level) &
        (gender_filtered['Age'].between(age_range[0], age_range[1])) &
        (gender_filtered['Entrepreneurship'].isin(selected_statuses))
    ]

    if df_filtered.empty:
        st.warning("⚠️ Not enough data to display charts. Please adjust the filters.")
    else:
        with st.container():
            st.markdown("""<div style="border: 1px solid #e0e0e0; border-radius: 10px; padding: 15px; margin-top: 10px; margin-bottom: 30px;">
                <div style="display: flex; justify-content: space-around; text-align: center; line-height: 1.3;">
                    <div>
                        <div style="font-size: 14px; color: #555;">Total Records</div>
                        <div style="font-size: 28px;">{}</div>
                    </div>
                    <div>
                        <div style="font-size: 14px; color: #555;">Median Age</div>
                        <div style="font-size: 28px;">{:.1f}</div>
                    </div>
                    <div>
                        <div style="font-size: 14px; color: #555;">Entrepreneurs (%)</div>
                        <div style="font-size: 28px;">{:.1f}%</div>
                    </div>
                </div></div>
            """.format(len(df_filtered), df_filtered['Age'].median(),
                       (df_filtered['Entrepreneurship'] == "Yes").mean() * 100),
            unsafe_allow_html=True)

        df_grouped = (
            df.groupby(['Current_Job_Level', 'Age', 'Entrepreneurship'])
            .size()
            .reset_index(name='Count')
        )
        df_grouped['Percentage'] = df_grouped.groupby(['Current_Job_Level', 'Age'])['Count'].transform(lambda x: x / x.sum())

        df_bar = df_grouped[
            (df_grouped['Current_Job_Level'] == selected_level) &
            (df_grouped['Age'].between(age_range[0], age_range[1])) &
            (df_grouped['Entrepreneurship'].isin(selected_statuses))
        ]

        even_ages = sorted(df_bar['Age'].unique())
        even_ages = [age for age in even_ages if age % 2 == 0]

        fig_bar = px.bar(
            df_bar,
            x='Age',
            y='Percentage',
            color='Entrepreneurship',
            barmode='stack',
            color_discrete_map=color_map,
            category_orders={'Entrepreneurship': ['No', 'Yes']},
            labels={'Age': 'Age', 'Percentage': 'Percentage'},
            height=450,
            width=1250,
            title=f"Entrepreneurship Distribution by Age – {selected_level} Level"
        )

        fig_bar.update_traces(
            hovertemplate="Entrepreneurship=%{customdata[0]}<br>Age=%{x}<br>Percentage=%{y:.0%}<extra></extra>",
            customdata=df_bar[['Entrepreneurship']].values,
            hoverinfo="skip"
        )

        fig_bar.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(t=40, l=40, r=40, b=40),
            legend_title_text='Entrepreneurship',
            xaxis_tickangle=0,
            bargap=0.1,
            xaxis=dict(tickvals=even_ages),
            yaxis=dict(title="Percentage", range=[0, 1], tickformat=".0%"),
            legend=dict(orientation='h', yanchor='bottom', y=-0.3, xanchor='center', x=0.5)
        )

        df_avg_offers = (
            df_filtered
            .groupby(['Age', 'Entrepreneurship'])['Job_Offers']
            .mean()
            .reset_index()
        )

        fig_line = go.Figure()
        for status in selected_statuses:
            data_status = df_avg_offers[df_avg_offers["Entrepreneurship"] == status]
            fig_line.add_trace(go.Scatter(
                x=data_status["Age"],
                y=data_status["Job_Offers"],
                mode="lines+markers",
                name=status,
                line=dict(color=color_map[status], width=2),
                marker=dict(size=6),
                hovertemplate="%{y:.2f}"
            ))

        fig_line.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(t=40, l=40, r=40, b=40),
            legend_title_text='Entrepreneurship',
            xaxis_tickangle=0,
            hovermode="x unified",
            width=1250,
            xaxis=dict(
                showspikes=True,
                spikemode='across',
                spikesnap='cursor',
                spikethickness=1.2,
                spikedash='dot',
                tickvals=even_ages
            ),
            yaxis=dict(
                title="Average Job Offers",
                showspikes=True,
                spikemode='across',
                spikesnap='cursor',
                spikethickness=1.2,
                spikedash='dot'
            ),
            legend=dict(orientation='h', yanchor='bottom', y=-0.3, xanchor='center', x=0.5)
        )

        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(fig_bar, use_container_width=True)
        with col2:
            st.plotly_chart(fig_line, use_container_width=True)
