# Agnipariksha: Evaluating the Impact of Climate Change on Solar Energy Harvesting

## Overview

This project investigates how climate change and environmental conditions influence solar energy generation. Using historical climate data from Pavagada Solar Park (2015–2025), the study evaluates the impact of temperature, humidity, wind speed, and solar radiation on solar panel efficiency and energy output.

The project combines data analytics, feature engineering, machine learning, and interactive visualization to understand the relationship between climate variables and solar energy harvesting.

---

## Objectives

* Analyze climate trends from 2015–2025
* Evaluate the impact of environmental factors on solar energy generation
* Model solar panel efficiency using temperature and degradation factors
* Quantify climate impact using machine learning techniques
* Visualize trends and insights through an interactive Streamlit dashboard

---

## Dataset

**Source:** NASA POWER Database

**Location:** Pavagada Solar Park, Karnataka, India

### Features Used

* Temperature (T2M)
* Relative Humidity (RH2M)
* Wind Speed (WS2M)
* Solar Radiation (SW_IRR)

---

## Methodology

### Data Preprocessing

* Data cleaning and validation
* Date feature creation
* Time-series preparation
* Trend and seasonal analysis

### Feature Engineering

To simulate real-world solar panel behavior:

**Temperature Efficiency**

* Solar panels operate optimally at 25°C
* Efficiency decreases with increasing temperature

**Degradation Efficiency**

* Annual degradation rate assumed: 0.5%
* Base year: 2018

**Solar Generation Model**

* Final Efficiency = Temperature Efficiency × Degradation Efficiency
* Solar Generation = Solar Radiation × Final Efficiency

---

## Machine Learning Models

The following regression models were used:

* Random Forest Regressor
* XGBoost Regressor

### Target Variable

* Solar Generation

### Features

* Temperature
* Relative Humidity
* Wind Speed

---

## Results

| Model         | R² Score | MSE   |
| ------------- | -------- | ----- |
| Random Forest | 0.524    | 0.691 |
| XGBoost       | 0.528    | 0.686 |

### Key Insight

When Solar Radiation was included as a feature, model performance increased significantly (R² ≈ 0.98). However, this introduced data leakage because Solar Radiation is directly involved in calculating Solar Generation.

To ensure realistic analysis, Solar Radiation was excluded from model training.

---

## Dashboard Features

The Streamlit dashboard includes:

* Temperature Trend Analysis
* Solar Generation Trend Analysis
* Temperature vs Solar Generation
* Temperature vs Efficiency
* Monthly Temperature Patterns
* Correlation Heatmap
* Interactive Year Filtering

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* XGBoost
* Streamlit
* Jupyter Notebook

---

## Key Findings

* Rising temperatures negatively affect solar panel efficiency.
* Climate variables moderately influence solar energy generation.
* Solar radiation remains the dominant driver of solar output.
* Climate-aware planning is essential for future renewable energy systems.

---

## Future Scope

* Inclusion of cloud cover and additional climate variables
* Advanced time-series forecasting models
* Multi-location solar farm analysis
* Long-term climate impact prediction

---

## Author

**Asmita Baul**

B.Sc. Data Science & Analytics
JAIN (Deemed-to-be University)

Project developed as part of academic research on climate change and renewable energy analytics.
