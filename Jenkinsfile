pipeline {
    agent any

    environment {
        IMAGE_NAME = "sammybaransi537/oneapp"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Parallel Checks') {
            parallel {

                stage('Linting') {
                    steps {
                        echo 'Running linting'
                    }
                }

                stage('Security Scan') {
                    steps {
                        echo 'Running security scan'
                    }
                }
            }
        }

        stage('Docker Build') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
            }
        }

        stage('Docker Login') {
            steps {

                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {

                    sh '''
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    '''
                }
            }
        }

        stage('Docker Push') {
            steps {
                sh "docker push ${IMAGE_NAME}:${BUILD_NUMBER}"
            }
        }
    }

    post {
        success {
            echo 'Image pushed successfully'
        }

        failure {
            echo 'Pipeline failed'
        }
    }
}