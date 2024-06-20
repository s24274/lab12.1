pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/<TWOJE_UZYTKOWNIK>/calculator.git', branch: 'master'
            }
        }
        stage('Test') {
            steps {
                script {
                    try {
                        sh 'python3 -m unittest discover'
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }
    }

    post {
        failure {
            echo 'One or more tests failed.'
        }
        success {
            echo 'All tests passed.'
        }
    }
}
