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

        stage('Test Docker Image') {
            steps {
                bat 'docker images sensor-dashboard'
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
