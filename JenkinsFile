pipeline {
    agent any

    stages {
        stage("Clone Code") {
            steps {
                echo "Code will cloned via webhook"
            }
        }

        stage("Install Dependencies") {
            steps {
                sh "python -m venv venv"
                sh "venv/bin/pip install -r requirements.txt"
            }
        }

        stage("Run App") {
            steps {
                sh "venv/bin/python app.py &"
            }
        }
    }
}
