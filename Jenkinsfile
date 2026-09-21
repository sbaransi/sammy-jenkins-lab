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

        stage('Parallel Tasks') {
            parallel {

                stage('Task 1') {
                    steps {
                        echo 'Running Task 1'
                        sh 'sleep 5'
                        echo 'Task 1 Complete'
                    }
                }

                stage('Task 2') {
                    steps {
                        echo 'Running Task 2'
                        sh 'sleep 5'
                        echo 'Task 2 Complete'
                    }
                }

                stage('Task 3') {
                    steps {
                        echo 'Running Task 3'
                        sh 'sleep 5'
                        echo 'Task 3 Complete'
                    }
                }
            }
        }

        stage('Final Stage') {
            steps {
                echo 'All parallel tasks completed'
            }
        }
    }
}