# File for the reported cases 

import pandas as pd
import sqlalchemy
from sql_connection_complete import connection_string
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config (page_title = 'Reported cases', page_icon = '📋')
st.title ('Reported cases')
st.subheader('With data from the World Health Organization')
st.markdown(
    '''
    This page is dedicated to visualization. We have gathered statistical data from the [World Health Organization](https://www.who.int/) and turn it into interactive maps and graphs for you to use. You can select different years with the slide button and thanks to our database, your query will be answered. Feel free to hover over the graphs to see additional information and choose different diseases and locations.
    The plots and graphs you are visuallizing are made in [plotly](https://plotly.com/python/getting-started/).
    
    **👈 Select a disease and a country to start** 
    ''')

def fetch_data(country, disease, year):
    query = f"""
            SELECT
                countries.country_name,
                countries.country_code,
                diseases_stats_per_countries.disease_stat_cases,
                diseases_stats_per_countries.disease_stat_year
            FROM
                diseases_stats_per_countries
            JOIN
                countries ON diseases_stats_per_countries.country_id = countries.country_id
            JOIN
                diseases ON diseases_stats_per_countries.disease_id = diseases.disease_id
            WHERE
                countries.country_name = '{country}'
                AND
                diseases.disease_name = '{disease}'
                AND
                diseases_stats_per_countries.disease_stat_year = '{year}'
            """
    queried_data = pd.read_sql(query, con = connection_string)
    return queried_data

def map_px(queried_data):
    
    queried_data['Cases'] = queried_data['disease_stat_cases']
    
    fig_map = px.scatter_geo(
        data_frame=queried_data,
        title = 'Registrated cases per country and year',
        locations='country_code',
        hover_name='country_name',
        hover_data={'Cases': True, 'disease_stat_cases': False, 'country_code': False}, 
        size='disease_stat_cases',
        projection='natural earth'
    )
    
    return fig_map

def fetch_data_global (disease, year):
    query = f"""
            SELECT
                countries.country_name,
                countries.country_code,
                diseases.disease_name,
                diseases_stats_per_countries.disease_stat_cases,
                diseases_stats_per_countries.disease_stat_year
            FROM
                diseases_stats_per_countries
            JOIN
                countries ON diseases_stats_per_countries.country_id = countries.country_id
            JOIN
                diseases ON diseases_stats_per_countries.disease_id = diseases.disease_id
            WHERE
                diseases.disease_name = '{disease}'
            AND
                diseases_stats_per_countries.disease_stat_year = '{year}'
            """
    queried_data_global = pd.read_sql(query, con = connection_string)
    return queried_data_global

def map_cases(queried_data_global):
    queried_data_global['Cases'] = queried_data_global['disease_stat_cases']

    fig_map_global = px.choropleth(
        title = 'Cases registered',
        data_frame = queried_data_global,
        locations = 'country_code',
        hover_name = 'country_name',
        hover_data = {'Cases': True, 'disease_stat_cases': False, 'country_code': False},
        color = 'Cases',
        color_continuous_scale=px.colors.sequential.Plasma
    )
    
    return fig_map_global

def fetch_cases_inland(disease,country):
    query = f"""
            SELECT
                countries.country_name,
                countries.country_code,
                diseases.disease_name,
                diseases_stats_per_countries.disease_stat_cases,
                diseases_stats_per_countries.disease_stat_year
            FROM
                diseases_stats_per_countries
            JOIN
                countries ON diseases_stats_per_countries.country_id = countries.country_id
            JOIN
                diseases ON diseases_stats_per_countries.disease_id = diseases.disease_id
            WHERE
                diseases.disease_name = '{disease}'
            AND
                countries.country_name = '{country}'
            """
    queried_data_cases_inland = pd.read_sql(query, con = connection_string)
    return queried_data_cases_inland

def graph_inland_cases(queried_data_cases_inland):
    
    # Aggregate data by year, otherwise many lines will appear
    aggregated_data = queried_data_cases_inland.groupby('disease_stat_year')['disease_stat_cases'].sum().reset_index()
    
    x_data = aggregated_data['disease_stat_year'].tolist()
    y_data = aggregated_data['disease_stat_cases'].tolist()

    fig_graph_inland_cases = go.Figure(
        data = [
            go.Scatter(
                x = x_data,
                y = y_data,
                mode = 'lines+markers',
                marker = dict(size = 12, color='#0d0887'),
                line = dict (width = 4, color='#0d0887'),
                name = 'Cases'
            )
        ]
    )

    fig_graph_inland_cases.update_layout(
        title = 'Number of inland cases registered over time',
        xaxis_title = 'Year',
        yaxis_title = 'Registered cases',
        xaxis = dict(tickmode='linear'),
        template = 'plotly_white'
    )

    return fig_graph_inland_cases

# Create a dictionary with the needed data for the user
data_sql = {'countries': pd.read_sql('SELECT DISTINCT country_name FROM countries', con = connection_string)['country_name'].tolist(),
           'diseases': pd.read_sql('SELECT DISTINCT disease_name FROM diseases', con = connection_string)['disease_name'].tolist(),
           'years': pd.read_sql('SELECT DISTINCT disease_stat_year FROM diseases_stats_per_countries', con = connection_string)['disease_stat_year'].tolist(),
           'groups': pd.read_sql('SELECT DISTINCT vaccine_target_population FROM vaccines_schedules', con = connection_string)['vaccine_target_population'].tolist()}

# Ask the user to select a country, disease and year
country = st.sidebar.selectbox('Choose a country', data_sql['countries'])
disease = st.sidebar.selectbox('Choose a disease', data_sql['diseases'])
year = st.slider('Choose a year',  min_value=min(data_sql['years']), max_value=max(data_sql['years']), value=min(data_sql['years']))

# Use the data
data = fetch_data(country, disease, year)
data_global = fetch_data_global(disease,year)
data_cases_inland = fetch_cases_inland(disease,country)

# Plot the map
if not data.empty:
    plot = map_px(data)
    st.plotly_chart(plot)
else:
    st.write("No data available for the selected criteria.")
if not data_global.empty:
    plot_global = map_cases(data_global)
    st.plotly_chart(plot_global)
else:
    st.write('No data available for that selected diseases and/or year')
if not data_cases_inland.empty:
    plot_graph_inland_cases = graph_inland_cases(data_cases_inland)
    st.plotly_chart(plot_graph_inland_cases)
else:
    st.write('No data available for that selected disease')