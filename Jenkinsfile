pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub...'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'

                bat '''
                    docker build -t sensor-dashboard .
                '''
            }
        }

        stage('Python Validation') {
            steps {
                echo 'Validating Python application inside Docker...'

                bat '''
                    docker run --rm sensor-dashboard python -m py_compile app.py
                '''
            }
        }

        stage('Test Docker Container') {
            steps {
                bat '''
                    echo Removing previous test container if it exists...
                    docker rm -f sensor-dashboard-test 2>NUL || exit /b 0

                    echo Starting test container...
                    docker run -d --name sensor-dashboard-test -p 8502:8501 sensor-dashboard

                    echo Waiting for application to start...
                    powershell -Command "Start-Sleep -Seconds 10"

                    echo Checking container status...
                    docker ps --filter "name=sensor-dashboard-test"

                    echo Testing Streamlit application...
                    powershell -Command "$response = Invoke-WebRequest -Uri 'http://localhost:8502' -UseBasicParsing; if ($response.StatusCode -ne 200) { exit 1 }; Write-Host 'Streamlit health check: HTTP 200 OK'"

                    echo Docker container test completed successfully.
                '''
            }
        }

        stage('Cleanup Test Container') {
            steps {
                bat '''
                    echo Cleaning up test container...
                    docker rm -f sensor-dashboard-test 2>NUL || exit /b 0
                '''
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                    echo Stopping previous production container...
                    docker rm -f sensor-dashboard-container 2>NUL || exit /b 0

                    echo Starting new production container...
                    docker run -d --name sensor-dashboard-container -p 8501:8501 sensor-dashboard

                    echo Waiting for deployment...
                    powershell -Command "Start-Sleep -Seconds 5"

                    echo Checking deployed container...
                    docker ps --filter "name=sensor-dashboard-container"

                    echo Testing deployed application...
                    powershell -Command "$response = Invoke-WebRequest -Uri 'http://localhost:8501' -UseBasicParsing; if ($response.StatusCode -ne 200) { exit 1 }; Write-Host 'Deployment health check: HTTP 200 OK'"

                    echo Deployment completed successfully.
                '''
            }
        }
    }

    post {
        success {
            echo '=============================================='
            echo 'Sensor Dashboard CI/CD pipeline completed!'
            echo 'Docker image built successfully.'
            echo 'Python validation completed successfully.'
            echo 'Docker container tested successfully.'
            echo 'Application deployed successfully.'
            echo 'Application: http://localhost:8501'
            echo '=============================================='
        }

        failure {
            echo '=============================================='
            echo 'Pipeline failed!'
            echo 'Check the Jenkins Console Output for details.'
            echo '=============================================='
        }

        always {
            echo 'CI/CD pipeline execution finished.'
        }
    }
}
