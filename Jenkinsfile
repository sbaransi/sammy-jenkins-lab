pipeline {
    agent any

    stages {

        stage('Docker Credential Test') {
            steps {

                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_TOKEN'
                    )
                ]) {

                    sh 'echo "Docker Username: $DOCKER_USER"'
                    sh 'echo "Token Length: ${#DOCKER_TOKEN}"'
                }
            }
        }
    }
}