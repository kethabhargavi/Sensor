# 🚀 Sensor Analytics Dashboard – Docker & Jenkins CI/CD

A real-time **time-series sensor analytics dashboard** built with Python, Streamlit, SQLite, Docker, and Jenkins. The application simulates continuous sensor readings, stores timestamped data, and provides interactive temperature and humidity analytics through a modern dashboard.

The project also demonstrates a complete **CI/CD workflow**, where code changes pushed to GitHub are automatically built, tested, containerized, and deployed using Jenkins.

---

## 📌 Features

### 📊 Application Features

* Real-time sensor data generation
* Automatic dashboard refresh
* Time-series data storage using SQLite
* Interactive Streamlit dashboard
* Temperature and humidity monitoring
* Minimum, maximum, and average analytics
* Live temperature trend visualization
* Live humidity trend visualization
* Latest sensor records table
* Responsive dashboard UI

### ⚙️ DevOps Features

* GitHub-based source code management
* Docker containerization
* Jenkins CI/CD pipeline
* Automated Docker image build
* Automated container testing
* Automated deployment
* Container cleanup and redeployment
* Application health verification

---

## 🛠️ Tech Stack

### Application

* **Python**
* **Streamlit**
* **SQLite**
* **Pandas**
* **Matplotlib**

### DevOps

* **Git**
* **GitHub**
* **Docker**
* **Jenkins**
* **CI/CD**

---

## 🏗️ Project Architecture

```text
                     GitHub
                        │
                        │ Push
                        ▼
                    Jenkins
                        │
              ┌─────────┴─────────┐
              │                   │
          Checkout           Docker Build
                                  │
                                  ▼
                           Docker Image
                                  │
                                  ▼
                         Container Testing
                                  │
                                  ▼
                            Deployment
                                  │
                                  ▼
                    Sensor Dashboard Container
                                  │
                                  ▼
                         Streamlit :8501
                                  │
                                  ▼
                      Sensor Analytics Dashboard
```

---

## 📂 Project Structure

```text
sensor_dashboard/
│
├── app.py
├── sensordb.db
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
└── README.md
```

---

## 🐳 Docker

The application is containerized using Docker to provide a consistent runtime environment.

### Build the Docker image

```bash
docker build -t sensor-dashboard .
```

### Run the container

```bash
docker run -d -p 8501:8501 --name sensor-dashboard sensor-dashboard
```

The application will be available at:

```text
http://localhost:8501
```

### Check running containers

```bash
docker ps
```

### Stop the container

```bash
docker stop sensor-dashboard
```

### Remove the container

```bash
docker rm sensor-dashboard
```

---

## 🔄 Jenkins CI/CD Pipeline

The project uses Jenkins to automate the application delivery process.

### Pipeline Flow

```text
GitHub Push
     ↓
Jenkins Trigger
     ↓
Checkout Source Code
     ↓
Build Docker Image
     ↓
Run Container Test
     ↓
Health Check
     ↓
Cleanup Previous Container
     ↓
Deploy New Container
     ↓
Application Running
```

### Jenkins Pipeline Stages

| Stage                  | Purpose                                 |
| ---------------------- | --------------------------------------- |
| **Checkout**           | Retrieves the latest source code        |
| **Build Docker Image** | Creates the application Docker image    |
| **Test Container**     | Starts a temporary container            |
| **Health Check**       | Verifies that Streamlit is responding   |
| **Cleanup**            | Removes previous containers             |
| **Deploy**             | Starts the latest application container |

This demonstrates a basic but practical **CI/CD workflow using Jenkins and Docker**.

---

## ▶️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/kethabhargavi/Sensor.git
cd Sensor
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Locally

Start the Streamlit application:

```bash
streamlit run app.py
```

Open the dashboard:

```text
http://localhost:8501
```

---

## 🌐 Dashboard

The dashboard provides:

* 📈 Live temperature analytics
* 💧 Humidity monitoring
* 📊 Minimum / Maximum / Average values
* 🕒 Timestamped sensor readings
* 📋 Latest sensor records
* 🔄 Automatic data refresh

---

## 💡 Use Cases

This project demonstrates how lightweight time-series systems can be used for:

* IoT sensor monitoring
* Environmental monitoring
* Real-time analytics
* Sensor data visualization
* Time-series data storage
* Data engineering prototypes
* DevOps and CI/CD demonstrations

---

## 🎯 DevOps Concepts Demonstrated

This project was also developed to demonstrate practical DevOps concepts:

* Source control with Git and GitHub
* Continuous Integration
* Continuous Deployment
* Jenkins pipelines
* Docker image creation
* Docker container management
* Automated application testing
* Application health checks
* Automated deployment

---

## 🚀 Future Enhancements

* [ ] CSV report export
* [ ] User authentication
* [ ] PostgreSQL / TimescaleDB integration
* [ ] AWS deployment
* [ ] Prometheus monitoring
* [ ] Grafana dashboards
* [ ] Jenkins webhook automation
* [ ] Kubernetes deployment

---

## 📸 Dashboard Preview

Add a screenshot of the running dashboard here:

```text
![Sensor Analytics Dashboard](dashboard-preview.png)
```

---

## 👩‍💻 Author

**Bhargavi Ketha**

Computer Science Engineer | Python | SQL | Cloud | DevOps

* GitHub: `https://github.com/kethabhargavi`
* LinkedIn: Add your LinkedIn profile
* Portfolio: Add your portfolio URL

---

## ⭐ Project Highlights

> **Python + Streamlit + SQLite + Docker + Jenkins CI/CD**

A practical project combining **real-time data analytics with containerization and automated CI/CD deployment**.
