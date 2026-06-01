import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Page Setup
st.set_page_config(page_title="Solar Dashboard", layout="wide")
st.title("Climate Impact on Solar Energy Generation")

# Load Data
df = pd.read_excel("../data/Solar power generation.xlsx")

# Create Date column
df["Date"] = pd.to_datetime(df[["YEAR","MONTH","DAY"]])
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month

# Sidebar Filters
st.sidebar.header("Filters")

year_range = st.sidebar.slider(
    "Select Year Range",
    int(df["Year"].min()),
    int(df["Year"].max()),
    (2015, 2025)
)

filtered_df = df[
    (df["Year"] >= year_range[0]) &
    (df["Year"] <= year_range[1])
]


# KPI Section
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Avg Temperature (°C)", round(filtered_df["T2M"].mean(), 2))
col2.metric("Avg Solar Generation", round(filtered_df["Solar_gen"].mean(), 2))
col3.metric("Avg Efficiency", round(filtered_df["final_eff"].mean(), 3))


# Temperature Trend
st.subheader("Temperature Trend Over Time")

temp_trend = filtered_df.groupby("Year")["T2M"].mean()

fig, ax = plt.subplots()
temp_trend.plot(ax=ax, marker='o')
ax.set_ylabel("Temperature (°C)")
ax.set_title("Yearly Average Temperature")
st.pyplot(fig)


# Solar Generation Trend
st.subheader("Solar Generation Trend")

solar_trend = filtered_df.groupby("Year")["Solar_gen"].mean()

fig, ax = plt.subplots()
solar_trend.plot(ax=ax, color="orange", marker='o')
ax.set_ylabel("Solar Generation (kWh/m²/day)")
ax.set_title("Yearly Solar Generation")
st.pyplot(fig)


# Temperature vs Solar Generation
st.subheader("Temperature vs Solar Generation")

fig, ax = plt.subplots()
sns.scatterplot(
    data=filtered_df,
    x="T2M",
    y="Solar_gen",
    alpha=0.5
)
ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Solar Generation")
st.pyplot(fig)


# Temperature vs Efficiency
st.subheader("Temperature vs Efficiency")

fig, ax = plt.subplots()
sns.scatterplot(
    data=filtered_df,
    x="T2M",
    y="final_eff",
    color="red",
    alpha=0.5
)
ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Efficiency")
st.pyplot(fig)


# Monthly Pattern
st.subheader("Monthly Temperature Pattern")

monthly_temp = filtered_df.groupby("Month")["T2M"].mean()

fig, ax = plt.subplots()
monthly_temp.plot(ax=ax, marker='o')
ax.set_ylabel("Temperature (°C)")
ax.set_title("Average Monthly Temperature")
st.pyplot(fig)


# Correlation Heatmap
st.subheader("Correlation Heatmap")

corr = filtered_df[["T2M", "RH2M", "WS2M", "Solar_gen"]].corr()

fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)
