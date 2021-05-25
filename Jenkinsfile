pipeline {
    agent any 
    environment {
        //once you sign up for Docker hub, use that user_id here
        registry = "atulspatil/pythonjenkins2"
        //- update your credentials ID after creating credentials for connecting to Docker Hub
        registryCredential = 'e9b07e57-3c23-43f0-bdf5-986d74be47f1'
        dockerImage = ''
    }
    
    stages {
        stage('Cloning Git') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '', url: 'https://github.com/atulspatil/jenkins2.git']]])       
            }
        }
    
    // Building Docker images
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build registry
        }
      }
    }
    
     // Uploading Docker images into Docker Hub
    stage('Upload Image') {
     steps{    
         script {
            docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
            }
        }
      }
    }
    
     // Stopping Docker containers for cleaner Docker run
     stage('docker stop container') {
         steps {
            sh 'docker ps -f name=pythonjenkins2appContainer -q | xargs --no-run-if-empty docker container stop'
            sh 'docker container ls -a -fname=pythonjenkins2appContainer -q | xargs -r docker container rm'
         }
       }
    
    
    // Running Docker container, make sure port 8096 is opened in 
    stage('Docker Run') {
     steps{
         script {
            dockerImage.run("-p 5556:5000 --rm --name pythonjenkins2appContainer")
         }
      }
    }
  }
}

