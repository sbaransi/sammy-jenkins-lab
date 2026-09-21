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

        stage('QA Approval') {
            steps {
                input 'Is the application running successfully?'
            }
        }

        stage('Final Stage') {
            steps {
                echo 'Pipeline approved!'
            }
        }
    }
}