# 🚀 Sensor Analytics Dashboard – Docker & Jenkins CI/CD

A time-series **sensor analytics dashboard** built with Python, Streamlit, SQLite, Docker, and Jenkins. The application stores timestamped temperature and humidity readings and provides interactive analytics through a modern Streamlit dashboard.

The project also demonstrates a practical **CI/CD workflow**, where source code changes pushed to GitHub can trigger Jenkins to validate the application, build a Docker image, test the container, perform health checks, and deploy the latest version.

---

## 📌 Features

### 📊 Application Features

* Temperature and humidity sensor readings
* Timestamped sensor data storage using SQLite
* Interactive Streamlit dashboard
* Minimum, maximum, and average temperature analytics
* Average humidity analytics
* Temperature trend visualization
* Humidity trend visualization
* Sensor records table
* Sidebar-based sensor reading input
* Automatic dashboard refresh after adding readings
* Custom dashboard UI

### ⚙️ DevOps Features

* Git-based source code management
* GitHub repository integration
* Jenkins CI/CD pipeline
* Python syntax validation
* Docker containerization
* Automated Docker image build
* Automated container testing
* Automated application health checks
* Test container cleanup
* Automated deployment
* Production container redeployment
* HTTP 200 application verification

---

## 🛠️ Tech Stack

### Application

* **Python**
* **Streamlit**
* **SQLite**
* **Pandas**
* **Matplotlib**

### Automation & DevOps

* **Python Scripting**
* **Git**
* **GitHub**
* **Docker**
* **Jenkins**
* **CI/CD**
* **PowerShell**

---

## 🏗️ Project Architecture

```text
                         GitHub
                            │
                            │ Push
                            ▼
                         Jenkins
                            │
                            ▼
                    Checkout Source Code
                            │
                            ▼
                    Python Validation
                            │
                            ▼
                    Docker Image Build
                            │
                            ▼
                  Temporary Test Container
                            │
                            ▼
                     Health Check
                    HTTP 200 Validation
                            │
                            ▼
                    Cleanup Test Container
                            │
                            ▼
                         Deploy
                            │
                            ▼
                  Production Docker Container
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
│
├── scripts/
│   ├── health_check.py
│   ├── db_backup.py
│   └── cleanup.py
│
└── README.md
```

---

# 🐍 Python Automation Scripts

The project includes Python scripts that demonstrate practical scripting for application and DevOps-related automation.

### `health_check.py`

Performs an application health check to verify that the dashboard is responding correctly.

### `db_backup.py`

Provides a Python-based mechanism for backing up the SQLite sensor database.

### `cleanup.py`

Provides automation for cleanup tasks associated with the project environment.

These scripts demonstrate the use of Python beyond application development, particularly for **automation and operational tasks**.

---

# 🐳 Docker

The application is containerized using Docker to provide a consistent runtime environment.

### Build the Docker image

```bash
docker build -t sensor-dashboard .
```

### Run the container

```bash
docker run -d -p 8501:8501 --name sensor-dashboard-container sensor-dashboard
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
docker stop sensor-dashboard-container
```

### Remove the container

```bash
docker rm sensor-dashboard-container
```

---

# 🔄 Jenkins CI/CD Pipeline

The project uses Jenkins to automate the build, testing, validation, and deployment workflow.

## Pipeline Flow

```text
GitHub Push
     ↓
Jenkins Trigger
     ↓
Checkout Source Code
     ↓
Python Validation
     ↓
Build Docker Image
     ↓
Run Test Container
     ↓
Application Health Check
     ↓
Cleanup Test Container
     ↓
Deploy Production Container
     ↓
Deployment Health Check
     ↓
Application Running
```

## Jenkins Pipeline Stages

| Stage                       | Purpose                                                      |
| --------------------------- | ------------------------------------------------------------ |
| **Checkout**                | Retrieves the latest source code from GitHub                 |
| **Python Validation**       | Validates Python syntax inside the Docker environment        |
| **Build Docker Image**      | Builds the application Docker image                          |
| **Test Docker Container**   | Starts a temporary container for testing                     |
| **Health Check**            | Verifies that Streamlit returns HTTP 200                     |
| **Cleanup Test Container**  | Removes the temporary test container                         |
| **Deploy**                  | Stops the previous container and starts the latest version   |
| **Deployment Health Check** | Verifies that the deployed application responds successfully |

The pipeline has been successfully executed with:

```text
Finished: SUCCESS
```

The deployment health check also returned:

```text
HTTP 200 OK
```

---

# 🔗 GitHub + Jenkins Integration

The repository is connected to Jenkins using:

```text
https://github.com/kethabhargavi/Sensor.git
```

The Jenkins job is configured to build the application from the GitHub repository.

A GitHub/Jenkins trigger is configured so that repository changes can initiate the CI/CD workflow.

---

# ▶️ Installation

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

# ▶️ Run Locally

Start the Streamlit application:

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

# 🌐 Dashboard

The dashboard provides:

* 📈 Temperature analytics
* 💧 Humidity monitoring
* 📊 Minimum / Maximum / Average temperature
* 📊 Average humidity
* 🕒 Timestamped sensor readings
* 📋 Sensor data records
* 🔄 Dashboard refresh after new readings

---

# 💡 Use Cases

This project demonstrates concepts applicable to:

* IoT sensor monitoring
* Environmental monitoring
* Real-time analytics prototypes
* Sensor data visualization
* Time-series data storage
* Python automation
* DevOps and CI/CD demonstrations

---

# 🎯 DevOps Concepts Demonstrated

This project demonstrates practical experience with:

* Source control using Git and GitHub
* Jenkins CI/CD pipelines
* Continuous Integration
* Continuous Deployment
* Python scripting for automation
* Python syntax validation
* Docker image creation
* Docker container management
* Automated container testing
* Application health checks
* Container cleanup
* Automated deployment
* GitHub-triggered CI/CD workflow

---

# 📸 Dashboard Preview

Add a screenshot of the running dashboard:

```text
![Sensor Analytics Dashboard](dashboard-preview.png)
```

---

# 🚀 Future Enhancements

* [ ] CSV report export
* [ ] User authentication
* [ ] PostgreSQL / TimescaleDB integration
* [ ] AWS deployment
* [ ] Prometheus monitoring
* [ ] Grafana dashboards
* [ ] Kubernetes deployment
* [ ] Infrastructure provisioning with Terraform

---

# 👩‍💻 Author

**Bhargavi Ketha**

Computer Science Engineer | Python | SQL | Docker | Jenkins | Cloud | DevOps






