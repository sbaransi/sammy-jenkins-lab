pipeline {
    agent any

    environment {
        APP_NAME = "sammy-app"
    }

    stages {
        stage('Hello') {
            steps {
                echo "Application Name: ${APP_NAME}"
            }
        }

        stage('Environment Check') {
            steps {
                sh 'hostname'
                sh 'pwd'
                sh 'git --version'
                sh 'java -version'
            }
        }
    }
}