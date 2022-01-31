pipeline {
    agent any

	environment{

	}
    stages {
        stage('Build') {

            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            parallel {
                stage('Test On Windows') {
                    agent {
                        label "windows"
                    }
                    steps {
                        bat "run-tests.bat"
                    }
                }
                stage('Test On Linux') {
                    agent {
                        label "linux"
                    }
                    steps {
                        sh "run-tests.sh"
                    }
                }
            }
        }
        stage('Deploy') {
            when {
                branch 'release'
            }
            steps {
                echo 'Deploying....'
            }
        }
    }
}