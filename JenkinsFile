pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                echo 'Code will cloned via webhook'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Run App') {
            steps {
                bat 'venv\\Scripts\\activate && python app.py'
            }
        }
    }
}
