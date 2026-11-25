pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Code checked out from GitHub'
            }
        }

        stage('Build') {
            steps {
                bat 'python --version'
                bat 'python -m py_compile app.py'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m pip install pytest'
                bat 'python -m pytest -q test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                bat 'python app.py'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
