# The Visualizers 📊

A data visualization project exploring New York's Guaranteed Income for Artists initiative by Creatives Rebuild New York (CRNY).

[Live Demo](https://thevisualizers.streamlit.app/)

## Overview

This Streamlit application visualizes data from CRNY's Guaranteed Income for Artists and Artist Employment initiatives, providing insights into the artistic community's demographics, geographic distribution, and economic landscape across New York State.

## Features

- Interactive visualizations of artist demographics and distributions
- Geographic mapping of applicant distribution across NY State
- Analysis of artistic disciplines and preferences
- Economic landscape visualization including income sources
- Comprehensive analysis of wage payment types and other income sources

## Key Visualizations

1. **Race/Ethnicity Distribution**
   - Interactive violin plot showing distribution across gender and language
   - Detailed demographic analysis

2. **Geographic Distribution**
   - Interactive map of New York State
   - Visual representation of applicant density by county

3. **Artistic Disciplines**
   - Ranking analysis of primary, secondary, and tertiary discipline choices
   - Interactive line chart with smooth curves

4. **Economic Analysis**
   - Income sources visualization
   - Wage payment types distribution
   - Analysis of additional income streams

## Prerequisites

- Python 3.7+
- pip or conda for package management

## Installation

1. Clone the repository:
```bash
git clone https://github.com/akshada2712/visualizers_ny.git
cd the-visualizers
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

Required packages include:
- streamlit
- numpy
- pandas
- plotly
- matplotlib
- seaborn

## Usage

1. Run the Streamlit application:
```bash
streamlit run test.py
```

2. Open your browser and navigate to:
```
http://localhost:8501
```

## Data Requirements

The application expects an Excel file with the following structure:
- CRNY survey data with columns for demographics, disciplines, and economic information
- Geographic coordinates for NY counties
- County-wise applicant count data

## Visualization Details

### Demographics Visualization
- Violin plots showing distribution of race/ethnicity across gender and language
- Interactive elements for detailed exploration

### Geographic Visualization
- Scattergeo plot of New York State
- Dynamic sizing based on applicant density
- Interactive tooltips with county-specific information

### Artistic Disciplines
- Smooth curve visualization of discipline rankings
- Three-tiered analysis of primary, secondary, and tertiary choices

### Economic Analysis
- Donut chart of income sources
- Bar charts for wage payment types
- Demographic breakdowns of economic indicators

