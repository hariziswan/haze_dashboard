import pandas as pd
import requests
from io import StringIO
import streamlit as st

# Fetch the data
url = 'https://haze.sabah.io/feed.php?range=hourly&type=csv'
response = requests.get(url)
response.raise_for_status()
data = pd.read_csv(StringIO(response.text))

# Dashboard title
st.title("Haze Data Dashboard")

# Display the raw data
st.subheader("Raw Data")
st.write(data.head())

# Plotting the data
st.subheader("Haze Data Plot")
if not data.empty:
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    st.line_chart(data.set_index('timestamp'))
else:
    st.write("No data available to plot.")
