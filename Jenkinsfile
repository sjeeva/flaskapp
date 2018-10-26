node ('docker') {
  stage ('SCM Checkout') {
    checkout scm
  }
  
  stage ('Docker image build') {
    sh 'docker build -t flaskapp .'
  }
  
  stage ('Docker deploy') {
    sh "docker run -d -p 7373:5000 flaskapp"
  }

  stage ('Launch Info') {
    echo "=================="
    sh "docker ps -a"
  }
}
