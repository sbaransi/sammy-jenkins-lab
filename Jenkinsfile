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

        stage('Use Credentials') {
            steps {

                withCredentials([
                    usernamePassword(
                        credentialsId: 'demo-creds',
                        usernameVariable: 'MY_USER',
                        passwordVariable: 'MY_PASS'
                    )
                ]) {

                    sh 'echo "Username: $MY_USER"'
                    sh 'echo "Password length: ${#MY_PASS}"'
                }
            }
        }

        stage('Done') {
            steps {
                echo 'Credentials Lab Completed'
            }
        }
    }
}