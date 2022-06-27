pipeline {
    agent any

	environment{
	    NEW_VERSION = '1.3.0'
	}
    stages {
        stage('Build') {

            steps {
                echo 'Building new version ${NEW_VERSION}'
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
                expression {
                    BRANCH_NAME == 'main'
                }
            }
            steps {
                echo 'Deploying....'
            }
        }
    }
}