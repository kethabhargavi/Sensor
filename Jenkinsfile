pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t sensor-dashboard .'
            }
        }

        stage('Test Docker Container') {
            steps {
                bat '''
                    docker rm -f sensor-dashboard-test 2>NUL || exit 0
                    docker run -d --name sensor-dashboard-test -p 8502:8501 sensor-dashboard
                    timeout /t 10 /nobreak
                    docker ps --filter "name=sensor-dashboard-test"
                '''
            }
        }

        stage('Cleanup') {
            steps {
                bat 'docker rm -f sensor-dashboard-test 2>NUL || exit 0'
            }
        }
    }

    post {
        success {
            echo 'Sensor Dashboard CI pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
