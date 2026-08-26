import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Sensor Dashboard - Jenkins CI/CD",
    page_icon="📈",
    layout="wide"

)

# =========================================================
# CUSTOM CSS
# =========================================================

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

.dataframe {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TITLE
# =========================================================

st.markdown(
    '<div class="main-title">📈 Time-Series Sensor Analytics Dashboard</div>',
    unsafe_allow_html=True
)


# =========================================================
# DATABASE
# =========================================================

DB_NAME = "sensordb.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def initialize_database():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperature REAL NOT NULL,
            humidity REAL NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


initialize_database()


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.header("⚙ Add Sensor Reading")

temp = st.sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=100.0,
    value=25.0,
    step=0.1
)

hum = st.sidebar.slider(
    "Humidity",
    min_value=0.0,
    max_value=100.0,
    value=60.0,
    step=0.1
)


# =========================================================
# ADD READING
# =========================================================

if st.sidebar.button("➕ Add Reading", use_container_width=True):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO sensor_data
        (temperature, humidity, timestamp)
        VALUES (?, ?, datetime('now'))
        """,
        (temp, hum)
    )

    conn.commit()
    conn.close()

    st.sidebar.success(
        f"Reading added: {temp:.1f}°C / {hum:.1f}%"
    )

    # Force Streamlit to reload the latest database data
    st.rerun()


# =========================================================
# LOAD DATA
# =========================================================

conn = get_connection()

df = pd.read_sql_query(
    """
    SELECT
        id,
        temperature,
        humidity,
        timestamp
    FROM sensor_data
    ORDER BY id ASC
    """,
    conn
)

conn.close()


# =========================================================
# METRICS
# =========================================================

if not df.empty:

    avg_temp = df["temperature"].mean()
    min_temp = df["temperature"].min()
    max_temp = df["temperature"].max()

    avg_humidity = df["humidity"].mean()

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.markdown(
            f"""
            <div class="metric-card">
                <h3>Average Temp</h3>
                <h2>{avg_temp:.2f}°C</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="metric-card">
                <h3>Min Temp</h3>
                <h2>{min_temp:.2f}°C</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            f"""
            <div class="metric-card">
                <h3>Max Temp</h3>
                <h2>{max_temp:.2f}°C</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:

        st.markdown(
            f"""
            <div class="metric-card">
                <h3>Average Humidity</h3>
                <h2>{avg_humidity:.2f}%</h2>
            </div>
            """,
            unsafe_allow_html=True
        )


else:

    st.info(
        "No sensor readings available yet. "
        "Use the sidebar to add your first reading."
    )


# =========================================================
# DATA TABLE
# =========================================================

st.subheader("📋 Sensor Data Records")

if not df.empty:

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

else:

    st.write("No sensor data available.")


# =========================================================
# TEMPERATURE CHART
# =========================================================

if not df.empty:

    st.subheader("📊 Temperature Trend")

    fig, ax = plt.subplots(figsize=(10, 4))

    ax.plot(
        df["id"],
        df["temperature"],
        marker="o",
        linewidth=2
    )

    ax.set_title("Temperature Over Time")
    ax.set_xlabel("Reading ID")
    ax.set_ylabel("Temperature (°C)")

    ax.grid(True, alpha=0.3)

    st.pyplot(fig)


# =========================================================
# HUMIDITY CHART
# =========================================================

if not df.empty:

    st.subheader("💧 Humidity Trend")

    fig, ax = plt.subplots(figsize=(10, 4))

    ax.plot(
        df["id"],
        df["humidity"],
        marker="o",
        linewidth=2
    )

    ax.set_title("Humidity Over Time")
    ax.set_xlabel("Reading ID")
    ax.set_ylabel("Humidity (%)")

    ax.grid(True, alpha=0.3)

    st.pyplot(fig)


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    "Built using Python + Streamlit + SQLite | "
    "Containerized with Docker | Deployed using Jenkins CI/CD"
)
