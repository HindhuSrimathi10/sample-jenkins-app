pipeline {
    agent any
    
    stages {
        stage('SCM') {
            steps {
                echo 'Checking out source code from GitHub...'
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Building the application...'
                // For a Java/Maven project, uncomment this:
                // sh 'mvn clean compile'
                
                // For a Node.js project, uncomment this:
                // sh 'npm install'
                
                // For now, just echo to test the pipeline
                echo 'Build completed successfully'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                // For a Java/Maven project, uncomment this:
                // sh 'mvn test'
                
                // For a Node.js project, uncomment this:
                // sh 'npm test'
                
                // For now, just echo to test the pipeline
                echo 'Tests completed successfully'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline finished'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}
