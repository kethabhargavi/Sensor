# 📝 Project Notes — Sensor Dashboard + Jenkins CI/CD

This file documents the important commands used while developing, testing, containerizing, and deploying the **Sensor Analytics Dashboard**.

---

## 1. 📁 Navigate to the Project

```powershell
cd C:\Users\ketha\OneDrive\Desktop\sensor_dashboard
```

**Purpose:**
Moves to the Sensor Dashboard project directory.

---

## 2. 🐍 Python / Streamlit

### Check Python version

```powershell
python --version
```

**Purpose:**
Verifies the installed Python version.

### Install project dependencies

```powershell
pip install -r requirements.txt
```

**Purpose:**
Installs the Python packages required by the application.

### Run the application locally

```powershell
streamlit run app.py
```

**Purpose:**
Starts the Streamlit development server.

### Local application URL

```text
http://localhost:8501
```

**Purpose:**
Used to access the dashboard locally.

---

# 3. 🔀 Git & GitHub

### Initialize Git

```powershell
git init
```

**Purpose:**
Initializes the project as a Git repository.

### Check repository status

```powershell
git status
```

**Purpose:**
Shows modified, untracked, and staged files.

### Stage project files

```powershell
git add .
```

**Purpose:**
Stages the project files for committing.

### Create a commit

```powershell
git commit -m "Add sensor analytics dashboard"
```

**Purpose:**
Creates a snapshot of the project changes.

### Add GitHub repository

```powershell
git remote add origin https://github.com/kethabhargavi/Sensor.git
```

**Purpose:**
Connects the local Git repository to the GitHub repository.

### Verify GitHub remote

```powershell
git remote -v
```

**Purpose:**
Checks whether the GitHub repository is correctly configured as the remote.

### Push project to GitHub

```powershell
git push -u origin main
```

**Purpose:**
Uploads the local `main` branch to GitHub.

### Push later changes

```powershell
git add .
git commit -m "Update project"
git push origin main
```

**Purpose:**
Stages, commits, and pushes subsequent project changes.

---

# 4. 🐳 Docker

Docker was used to containerize the Streamlit application.

### Check Docker installation

```powershell
docker --version
```

**Purpose:**
Verifies that Docker is installed.

### Check Docker Engine

```powershell
docker info
```

**Purpose:**
Confirms that Docker Desktop / Docker Engine is running and displays Docker configuration.

### Build the Docker image

```powershell
docker build -t sensor-dashboard .
```

**Purpose:**
Builds a Docker image using the project's `Dockerfile`.

* `-t sensor-dashboard` → assigns the image name
* `.` → uses the current directory as the build context

### List Docker images

```powershell
docker images
```

**Purpose:**
Displays locally available Docker images.

### Run the application container

```powershell
docker run -d -p 8501:8501 --name sensor-dashboard sensor-dashboard
```

**Purpose:**
Starts the Streamlit application inside a Docker container.

* `-d` → runs in the background
* `-p 8501:8501` → maps the host port to the container port
* `--name sensor-dashboard` → gives the container a name

### Check running containers

```powershell
docker ps
```

**Purpose:**
Verifies that the application container is running.

### Check all containers

```powershell
docker ps -a
```

**Purpose:**
Shows both running and stopped containers.

### View container logs

```powershell
docker logs sensor-dashboard
```

**Purpose:**
Displays application/container logs for troubleshooting.

### Stop the container

```powershell
docker stop sensor-dashboard
```

**Purpose:**
Stops the running application container.

### Remove the container

```powershell
docker rm sensor-dashboard
```

**Purpose:**
Removes a stopped container.

### Force remove the container

```powershell
docker rm -f sensor-dashboard
```

**Purpose:**
Stops and removes the container in one command.

This was useful during redeployment when an existing container had to be replaced.

---

# 5. 🧪 Docker Application Testing

A separate port was used to test the application container before deployment.

### Start a test container

```powershell
docker run -d --name sensor-dashboard-test -p 8502:8501 sensor-dashboard
```

**Purpose:**
Runs a temporary test container on port `8502`.

The application inside the container still listens on `8501`, while the host accesses it through:

```text
http://localhost:8502
```

### Test the application response

```powershell
Invoke-WebRequest http://localhost:8502 -UseBasicParsing
```

**Purpose:**
Checks whether the Streamlit application is responding to HTTP requests.

### Check HTTP status

```powershell
if ((Invoke-WebRequest http://localhost:8502 -UseBasicParsing).StatusCode -ne 200) { exit 1 }
```

**Purpose:**
Returns a successful result only when the application responds with HTTP status `200`.

This provides a basic application-level health check for CI/CD.

### Remove the test container

```powershell
docker rm -f sensor-dashboard-test
```

**Purpose:**
Stops and removes the temporary test container after testing.

---

# 6. ☕ Java Setup for Jenkins

Jenkins requires Java.

The Java executable used during the Jenkins setup was:

```text
C:\Program Files\Eclipse Adoptium\jdk-21.0.12.101-hotspot\bin\java.exe
```

### Check Java version

```powershell
java -version
```

**Purpose:**
Verifies that Java is installed and available.

---

# 7. 🔧 Jenkins

Jenkins was configured to automate the Docker build, testing, and deployment process.

### Check Jenkins Windows service

```powershell
Get-Service Jenkins
```

**Purpose:**
Checks whether the Jenkins service is running.

### Jenkins Pipeline

The project uses:

```text
Jenkinsfile
```

**Purpose:**
Defines the CI/CD pipeline executed by Jenkins.

The pipeline follows this general flow:

```text
GitHub
   ↓
Checkout
   ↓
Docker Build
   ↓
Test Container
   ↓
Health Check
   ↓
Cleanup
   ↓
Deploy
```

---

# 8. 🔄 Jenkins + Docker Deployment

The main Docker commands used by the Jenkins pipeline are based on the same commands used for local testing.

### Build image

```powershell
docker build -t sensor-dashboard .
```

**Purpose:**
Creates the latest Docker image from the source code.

### Check the image

```powershell
docker images
```

**Purpose:**
Confirms that the Docker image was successfully created.

### Check running containers

```powershell
docker ps
```

**Purpose:**
Verifies that the deployed application container is running.

### Remove previous deployment

```powershell
docker rm -f sensor-dashboard
```

**Purpose:**
Removes the previous container before deploying the new version.

### Deploy the latest image

```powershell
docker run -d -p 8501:8501 --name sensor-dashboard sensor-dashboard
```

**Purpose:**
Starts the newly built application container.

---

# 9. 🌐 Application Verification

After deployment, the application can be accessed at:

```text
http://localhost:8501
```

**Purpose:**
Verifies that the deployed Streamlit application is accessible.

For CI/CD testing, the application can also be checked through:

```text
http://localhost:8502
```

when running the temporary test container.

---

# 10. 🔁 Complete Workflow

The commands above were used as part of the following development and deployment workflow:

```text
Develop app.py
      ↓
Install dependencies
      ↓
Run Streamlit locally
      ↓
Test dashboard
      ↓
Git add / commit
      ↓
Push to GitHub
      ↓
Jenkins detects/builds project
      ↓
Build Docker image
      ↓
Run test container
      ↓
Health check
      ↓
Remove test container
      ↓
Remove previous deployment
      ↓
Run new Docker container
      ↓
Open Streamlit dashboard
```

---

# 11. 📌 Important Project Files

| File               | Purpose                                |
| ------------------ | -------------------------------------- |
| `app.py`           | Main Streamlit application             |
| `sensordb.db`      | SQLite database containing sensor data |
| `requirements.txt` | Python dependencies                    |
| `Dockerfile`       | Docker image build instructions        |
| `Jenkinsfile`      | Jenkins CI/CD pipeline                 |
| `README.md`        | Main project documentation             |
| `NOTES.md`         | Commands and development notes         |

---

# 12. 🎯 Key Commands Used in the Project

The most important commands to remember for this project are:

### Git

```powershell
git status
git add .
git commit -m "message"
git push origin main
```

### Streamlit

```powershell
streamlit run app.py
```

### Docker

```powershell
docker build -t sensor-dashboard .
docker images
docker ps
docker ps -a
docker run -d -p 8501:8501 --name sensor-dashboard sensor-dashboard
docker logs sensor-dashboard
docker stop sensor-dashboard
docker rm -f sensor-dashboard
```

### Application health check

```powershell
Invoke-WebRequest http://localhost:8502 -UseBasicParsing
```

---

## 💡 What I Learned

Through this project, I practiced:

* Building a Python/Streamlit application
* Working with SQLite and time-series data
* Managing code with Git and GitHub
* Creating Docker images
* Running and managing Docker containers
* Troubleshooting Docker and WSL on Windows
* Setting up Jenkins
* Creating a Jenkins pipeline
* Integrating Jenkins with Docker
* Testing a containerized application
* Performing a basic application health check
* Automating application deployment through CI/CD

---

## 🚀 Final DevOps Flow

```text
GitHub → Jenkins → Docker Build → Test → Health Check → Deploy → Streamlit
```

This project demonstrates a complete beginner-friendly **CI/CD workflow for a containerized Python application**.
