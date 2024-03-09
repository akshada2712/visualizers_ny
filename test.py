import streamlit as st
import numpy as np
import pandas as pd
import re
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import json
import time
import os

start_time = time.time()


st.title("The Visualizers")

#st.write(data)

folder = os.getcwd()

st.header("Empowering New York's artists, CRNY's Guaranteed Income for Artists initiative fosters creativity and resilience with steadfast support")
#data  = pd.read_excel('https://raw.githubusercontent.com/akshada2712/visualizers_ny/main/data.xlsx')
data = pd.read_excel(folder+'/data.csv')
st.markdown("Creatives Rebuild New York (CRNY), launched in January 2021 with the generous backing of the Mellon Foundation, stands as a beacon of hope for New York's beleaguered arts and culture community in the wake of the COVID-19 pandemic. With a steadfast commitment to addressing the systemic inequities plaguing our cultural landscape, CRNY has rolled out innovative programs like the Guaranteed Income for Artists and Artist Employment initiatives. Through these initiatives, individual artists across New York State receive vital support, enabling them to pursue their craft with renewed vigor and without the burden of financial insecurity. The Guaranteed Income for Artists program, with its unencumbered $1,000 monthly stipend over 18 months, not only acknowledges the invaluable contributions of artists but also fosters a sense of solidarity and interconnectedness within the artistic community. As we navigate the path to recovery, the data collected from program participants and applicants serves as a crucial resource, informing our efforts to build a more inclusive and resilient arts ecosystem. The collaboration between CRNY and the Arts, Entrepreneurship, and Innovation Lab at the Center for Cultural Affairs represents a pivotal step towards leveraging data visualization to amplify the impact of these initiatives. In this story we would be crafting insights for how the artists are navigating labour market and the artistic disciplines.")


df = data

st.header("Arts Sectors Linked to Broader Societal Innovation")
st.subheader("Exploring Race/Ethnicity Distribution Across Gender and Language")
st.markdown("In today's diverse society, understanding the distribution of race and ethnicity across different demographic groups is crucial for promoting inclusivity and equity. In this analysis, we delve into the intricate relationship between race/ethnicity, gender, and language using a violin plot visualization.")

import plotly.graph_objects as go


# Violin plot
fig_violin = px.violin(df, x='g23_gender1', y='g22_language', color='g20_raceethnicity1', title='Violin Plot',
                       labels={'g23_gender1': 'Gender', 'g22_language': 'Language', 'g20_raceethnicity1': 'Race/Ethnicity'},
                       category_orders={'g23_gender1': ['Man', 'Woman', 'Non-binary', 'Two-spirit', 'Other', 'I prefer not to answer']},
                       template='plotly_white')

fig_violin.update_traces(meanline_visible=True)  # Show mean line inside violins
fig_violin.update_layout(legend_title='Race/Ethnicity',  # Title of the legend
                            # Display violins on top of each other
                          violingap=0.2,  # Gap between violins
                          font=dict(family='Arial', size=12),  # Specify font family and size
                          title_font=dict(size=20),  # Specify title font size
                          plot_bgcolor='rgba(0,0,0,0)',  # Make plot background transparent
                  paper_bgcolor='rgba(0,0,0,0)')
                          

#fig_violin.show()
st.plotly_chart(fig_violin, theme=None, use_container_width=True)

st.markdown("Unveiling the Melody of Diversity: Journey through the violins reveals a symphony of gender disparities and cultural richness. Each stroke of the bow paints a vibrant tapestry of race/ethnicity, echoing the mosaic of our society's traditions and languages. Delve deeper into the harmonies of language preferences, where intersections with race/ethnicity create unique melodies. Amidst the chorus, the median lines whisper tales of central tendencies, while outliers add an unexpected twist, enriching the grand composition of human experience")

st.header("Mapping New York: Exploring Geographic Patterns with Artists")
st.markdown("Navigating the Cartographic Canvas: Unveiling the Urban Tapestry. From the bustling streets of urban jungles to the serene expanses of rural vistas, each pin on the map tells a tale of human presence. In the heart of metropolitan hubs, clusters of applicants converge, echoing the rhythm of city life. Yet, as we venture into the quiet countryside, lone markers dot the landscape, whispering tales of solitude and untapped potential.")


loc_file = 'locations.txt'
county_count_file = 'countyCount.txt'
with open(loc_file) as json_file:
    county_coordinates = json.load(json_file)

with open(county_count_file) as json_file:
  county_data = json.load(json_file)

# Extract county names, latitudes, longitudes, and data values
county_names = list(county_coordinates.keys())
lats, lons = zip(*county_coordinates.values())
data_values = [county_data[county] for county in county_names]

# Normalize or scale the data values
max_value = max(data_values)
min_value = min(data_values)
scaled_values = [(value - min_value) / (max_value - min_value) * 100 for value in data_values]

# Create a Scattergeo plot
fig = go.Figure()

# Add markers for each county
for county, lat, lon, scaled_value in zip(county_names, lats, lons, scaled_values):
    fig.add_trace(go.Scattergeo(
        locationmode = 'USA-states',
        lon = [lon],
        lat = [lat],
        text = f'{county}<br>Applicants: {county_data[county]}',
        mode = 'markers',
        marker = dict(
            size = scaled_value,  # Marker size based on scaled data value
            opacity = 0.8,
            color = 'blue',  # Marker color
            symbol = 'circle',
            line = dict(width = 1, color = 'rgba(102, 102, 102)'),  # Marker border
        )
    ))

# Update trace colors
for i, trace in enumerate(fig.data):
    trace.marker.color = f'rgb({(i * 30) % 255}, {(i * 50) % 255}, {(i * 70) % 255})'  # Change trace color

# Update layout
fig.update_layout(
    title = 'Geographic Distribution of Applicants Across New York State',
    geo_scope = 'usa',  # Set map scope to USA
       plot_bgcolor='rgba(0,0,0,0)',  # Make plot background transparent
        paper_bgcolor='rgba(0,0,0,0)'
)

# Show the map
#fig.show()




st.plotly_chart(fig, theme=None, use_container_width=True)



st.markdown("Understanding the geographic distribution of applicants through an interactive Scattergeo plot is vital for community development and service provision in New York State. This visualization tool provides insights into spatial dynamics by representing each county with markers of varying sizes and colors, reflecting the intensity of applicant engagement and the spectrum of data values. By exploring regional disparities, decision-makers can identify areas with pronounced differences in applicant engagement, enabling them to prioritize interventions and tailor services to address specific community needs effectively. Additionally, the analysis of temporal trends and patterns empowers decision-makers to anticipate evolving needs, allocate resources strategically, and develop responsive, community-centered initiatives.")

st.header("Exploring Artistic Practices: Solitude vs. Collaboration")

import streamlit as st
import plotly.graph_objects as go
import time

start_time = time.time()

# Data
labels = ['Craft', 'Dance', 'Design', 'Film', 'Interdisciplinary Arts',
          'Literary Arts', 'Media Arts', 'Music', 'Oral Traditions', 'Performance Art',
          'Social Practice', 'Theater', 'Traditional Arts', 'Visual Arts']
first_choice = [727, 679, 717, 1093, 437, 745, 495, 2906, 72, 290, 179, 1135, 213, 3201]
second_choice = [768, 308, 985, 1113, 782, 764, 1162, 876, 193, 1027, 498, 708, 344, 1348]
third_choice = [573,  245, 585, 669, 1036, 589, 926, 617, 170, 802, 620, 345, 286, 856]

# Create traces for each choice with custom colors and smooth curves
trace1 = go.Scatter(x=labels, y=first_choice, mode='lines', name='1st Choice',
                    line=dict(color='rgb(31, 119, 180)', shape='spline', smoothing=1.3),
                    fill='tozeroy', fillcolor='rgba(31, 119, 180, 0.3)')
trace2 = go.Scatter(x=labels, y=second_choice, mode='lines', name='2nd Choice',
                    line=dict(color='rgb(255, 127, 14)', shape='spline', smoothing=1.3),
                    fill='tozeroy', fillcolor='rgba(255, 127, 14, 0.3)')
trace3 = go.Scatter(x=labels, y=third_choice, mode='lines', name='3rd Choice',
                    line=dict(color='rgb(44, 160, 44)', shape='spline', smoothing=1.3),
                    fill='tozeroy', fillcolor='rgba(44, 160, 44, 0.3)')

# Create figure
fig = go.Figure()

# Add traces to the figure
fig.add_trace(trace1)
fig.add_trace(trace2)
fig.add_trace(trace3)

# Update layout
fig.update_layout(title='Ranking of Disciplines',
                  xaxis_title='Disciplines',
                  yaxis_title='Count',
                  plot_bgcolor='rgba(0,0,0,0)',  # Make plot background transparent
                  paper_bgcolor='rgba(0,0,0,0)')  # Make paper background transparent

# Show the plot
st.plotly_chart(fig, theme=None, use_container_width=True)

end_time = time.time()


st.markdown("At the crossroads of creativity, individuals are tasked with distilling their essence into a selection of disciplines. Craft, Dance, Film, each representing a facet of human expression, beckon with unique allure. With up to three choices, one carefully navigates through this labyrinth of artistic possibilities, guided by instincts and aspirations.")

st.header("Mapping Artists' Economic Landscapes: Navigating the Labor Market")


# Data
wages_data = {
    'Option Not Selected': 10877,
    'Gigs Contracts Temp': 6008,
    'Art Practice': 2366,
    'Unemployed': 3630,
    'Part Timejob': 4419,
    'Other Earnings': 1357,
    'Full-Time Job': 1189,
    'Family Partner Support': 1447
}

# Create pie chart
labels = list(wages_data.keys())
values = list(wages_data.values())

# Define a custom color scheme
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f']

fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.3, marker=dict(colors=colors, line=dict(color='black', width=1)))])

# Update layout
fig.update_layout(
    title=dict(
        text='Income Sources Among Artists',
        font=dict(
            family='Arial',
            size=24,
            color='navy'
        ),
        x=0.5,
        y=0.9
    ),
    legend=dict(
        x=0.75,
        y=0.5,
        title='Income Sources',
        font=dict(
            family='Helvetica',
            size=12,
            color='black'
        )
    ),
    margin=dict(l=50, r=50, t=100, b=50),  # Adjust margins for better layout
    width=900,  # Set the width of the background
    height=700  # Set the height of the background
)

# Show the plot
#fig.show()

#st.plotly_chart(fig, theme=None, use_container_width=True)



################Transparent plots##########################
import streamlit as st
import plotly.graph_objects as go

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f']

fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.3, marker=dict(colors=colors, line=dict(color='black', width=1)))])

# Update layout
fig.update_layout(
    title=dict(
        text='Income Sources Among Artists',
        font=dict(
            family='Arial',
            size=24,
            color='navy'
        ),
        x=0.5,
        y=0.9
    ),
    legend=dict(
        x=0.75,
        y=0.5,
        title='Income Sources',
        font=dict(
            family='Helvetica',
            size=12,
            color='black'
        )
    ),
    margin=dict(l=50, r=50, t=100, b=50),  # Adjust margins for better layout
    width=900,  # Set the width of the background
    height=700,  # Set the height of the background
    plot_bgcolor='rgba(0,0,0,0)',  # Make plot background transparent
    paper_bgcolor='rgba(0,0,0,0)'  # Make paper background transparent
)

# Show the plot
st.plotly_chart(fig, theme=None, use_container_width=True)

st.markdown("The life of an artist is often a precarious one, with income sources fragmented and inconsistent. The first pie chart reveals that a mere 19.2% of artists rely on a full-time job as their primary income source. The largest segment, 34.8%, consists of those who rely on a combination of various other sources, such as gigs, contracts, temporary jobs, part-time work, and earnings from their art practice.")


############################################################











import streamlit as st
import pandas as pd
import plotly.express as px

# Drop rows with missing values in relevant columns
wages_data = df.dropna(subset=['p10_earnmoney1','p10_earnmoney2', 'p10_earnmoney3', 'p10b_wagespaid1','p_agerange', 'p41_gender1'])
mappings = {'gigs_contracts_temp': 'Gigs, Contracts, Temporary Jobs',
              'parttimejob': 'Part-Time Jobs',
              'other_earn':'Other Earnings',
              'familypartnersupport': 'Family/Partner Support',
              'artpractice': 'Art Practice',
              'fulltimejob': 'Full-time Job',
              'unemployed': 'Unemployed',
              }

wages_mappings = {'freelance': 'Freelance', 'both_w2_1099': 'Both W2 and 1099' , 'w2': 'W2', 'p10b_noans':'Prefer Not to answer', 'p10b_dontknow': "Don't Know"}
gender_mappings = {'man': 'Man', 'woman': 'Woman', 'gender_noanswer': 'Prefer Not to Answer', 'nonbinary': 'Non-Binary', 'gender_oth': 'Other',
       'twospirit': 'Two-Spirit'}

wages_data['p10_earnmoney1'] = wages_data['p10_earnmoney1'].map(mappings)
wages_data['p10_earnmoney2'] = wages_data['p10_earnmoney2'].map(mappings)
wages_data['p10_earnmoney3'] = wages_data['p10_earnmoney3'].map(mappings)
wages_data['p10b_wagespaid1'] = wages_data['p10b_wagespaid1'].map(wages_mappings)
wages_data['p41_gender1'] = wages_data['p41_gender1'].map(gender_mappings)

# Combine the multiple columns for p10 into a single column
wages_data['income_sources'] = (wages_data['p10_earnmoney1'].astype(str) + ',' +
                          wages_data['p10_earnmoney2'].astype(str) + ',' +
                          wages_data['p10_earnmoney3'].astype(str))

# Replace NaN values in income_sources with 'nan'
wages_data['income_sources'] = wages_data['income_sources'].replace('nan,', 'nan')

wages_data.rename(columns = {'income_sources':'Income Sources', 'p_agerange' : 'Age Range', 'p41_gender1': 'Gender', 'p11_otherincome': 'Other Income Sources', 'p38_race1': 'Race', 'p10b_wagespaid1': 'Wages Paid'}, inplace = True)

# Visualize wage payment types (p10b)
fig = px.pie(wages_data, names='Wages Paid', title='Wage Payment Types')
fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig, theme=None, use_container_width=True)
st.markdown("This patchwork of income streams is further underscored by the high percentage (53.3%) of freelance or contract-based wage payments, as shown in the second chart. Only 16.6% receive traditional W-2 employment income, while a substantial 15.4% admit to being unsure about their wage payment types. We observe a diverse array of payment methods and supplementary income streams, highlighting the complexity of individuals' financial portfolios")

# Visualize other income sources (p11)
fig = px.bar(wages_data, x='Other Income Sources', title='Distribution of Other Income Sources')
fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig, theme=None, use_container_width=True)
st.markdown('The bar chart showcasing the "Distribution of Other Income Sources" offers insights into the supplementary sources of income reported by participants. From royalties to investments, rental income, and other forms of earnings, the chart illustrates the breadth and complexity of individuals" financial portfolios. This visualization highlights the importance of considering multiple income streams and the role they play in supporting economic stability and resilience.')

# Visualize impact of criminal record on employment (p28b) by gender (p41)
fig = px.bar(wages_data, x='Age Range', color='Age Range', title='Impact of Criminal Record on Employment by Gender', barmode='group')
fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig, theme=None, use_container_width=True)
st.markdown("The chart titled 'Impact of Criminal Record on Employment by Age Range' explores the disparities in employment opportunities faced by individuals with criminal records, disaggregated by age. By comparing employment rates across different age ranges, the visualization reveals nuanced patterns and potential barriers to reintegration into the workforce. It underscores the need for targeted interventions and support systems to address the challenges faced by marginalized groups in accessing employment opportunities and achieving economic independence.")

# Visualize income sources by age range (p_agerange)
fig = px.bar(wages_data, x='Gender', color='Income Sources', title='Income Sources by Age Range', barmode='group')
fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig, theme=None, use_container_width=True)
st.markdown("The bar chart depicting 'Income Sources by Age Range' examines the distribution of income sources across different gender categories. By categorizing income sources such as wages, freelance earnings, and other sources, the visualization provides insights into the economic activities prevalent among different demographic groups. This analysis facilitates a deeper understanding of the factors driving economic participation and the diverse pathways individuals pursue to meet their financial needs. ")


# Visualize wage payment types by race/ethnicity (p38)
fig = px.bar(wages_data, x='Race', color='Wages Paid', title='Wage Payment Types by Race/Ethnicity', barmode='group')
fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig, theme=None, use_container_width=True)

st.markdown("The final visualization, 'Wage Payment Types by Race/Ethnicity,' delves into the intersectionality of race/ethnicity and wage payment methods. By examining the distribution of wage payment types across different racial and ethnic groups, the chart highlights disparities in employment opportunities and income generation. This exploration underscores the imperative of addressing systemic inequalities and promoting inclusive economic policies to foster equitable outcomes for all individuals, regardless of their background or identity. As we navigate through the visualizations, it becomes evident that promoting economic equity requires addressing systemic inequalities and fostering inclusive economic policies. By leveraging data-driven insights, we can inform evidence-based interventions aimed at fostering equitable outcomes for all individuals and communities.")

st.subheader("As we conclude our journey through the visualizations, we gain valuable insights into the complex dynamics of income sources and employment trends. From the diverse modes of wage payment to the impact of criminal records on employment and the intersectionality of race, ethnicity, and income generation, the visualizations offer a nuanced understanding of the economic landscape. By leveraging data-driven insights, we aspire to inform evidence-based policies and interventions aimed at promoting economic equity, opportunity, and empowerment for all individuals and communities.")






























