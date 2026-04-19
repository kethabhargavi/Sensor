import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Sensor Dashboard", layout="wide")

# ---------- Custom CSS ----------
st.markdown("""
<style>
body {
    background-color: #0E1117;
}

.main-title {
    font-size: 38px;
    font-weight: bold;
    color: white;
    text-align: center;
    margin-bottom: 20px;
}

.metric-card {
    background: linear-gradient(135deg, #1f4037, #99f2c8);
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    color: white;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
}

.sidebar .sidebar-content {
    background: #111827;
}

.dataframe {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📈 Time-Series Sensor Analytics Dashboard</div>', unsafe_allow_html=True)

# ---------- Database ----------
conn = sqlite3.connect("sensordb.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sensor_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    temperature REAL,
    humidity REAL,
    timestamp TEXT
)
""")
conn.commit()

# ---------- Sidebar ----------
st.sidebar.header("⚙ Add Sensor Reading")

temp = st.sidebar.slider("Temperature", 0.0, 100.0, 25.0)
hum = st.sidebar.slider("Humidity", 0.0, 100.0, 60.0)

if st.sidebar.button("➕ Add Reading"):
    cursor.execute(
        "INSERT INTO sensor_data (temperature, humidity, timestamp) VALUES (?, ?, datetime('now'))",
        (temp, hum)
    )
    conn.commit()
    st.sidebar.success("Reading Added Successfully")

# ---------- Load Data ----------
df = pd.read_sql_query("SELECT * FROM sensor_data", conn)

# ---------- Metrics ----------
if not df.empty:
    avg_temp = df["temperature"].mean()
    min_temp = df["temperature"].min()
    max_temp = df["temperature"].max()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Average Temp</h3>
            <h2>{avg_temp:.2f}°C</h2>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Min Temp</h3>
            <h2>{min_temp:.2f}°C</h2>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Max Temp</h3>
            <h2>{max_temp:.2f}°C</h2>
        </div>
        """, unsafe_allow_html=True)

# ---------- Table ----------
st.subheader("📋 Sensor Data Records")
st.dataframe(df, use_container_width=True)

# ---------- Animated Chart ----------
if not df.empty:
    st.subheader("📊 Temperature Trend")

    fig, ax = plt.subplots(figsize=(10, 4))

    ax.plot(df["temperature"], linewidth=3)
    ax.set_title("Temperature Over Time")
    ax.set_xlabel("Reading Number")
    ax.set_ylabel("Temperature")

    st.pyplot(fig)

# ---------- Footer ----------
st.markdown("---")
st.caption("Built using Streamlit + SQLite + Python")