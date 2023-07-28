pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                script {
                    def lastChanges = sh(returnStdout: true, script: 'git log -n 1 --pretty="%h %an - %s"').trim()
                    slackSend color: "warning", message: "Iniciando Processo `${env.JOB_NAME}#${env.BUILD_NUMBER}`\n\n_Mudanças:_\n${lastChanges}"
                }
            }
        }

        stage('Test') {
            steps {
                dir('app') {
                    sh 'virtualenv env'
                    sh '. env/bin/activate'
                    sh 'pip3 install -r requirements.txt'
                    sh 'python3 manage.py test'
                }
            }
        }

        stage('Deploy') {
            steps {
                sh './deploy.sh'
            }
        }
    }

    post {
        always {
            script {
                if (currentBuild.result == 'SUCCESS') {
                    slackSend color: "good", message: "Processo Concluído com Sucesso! :tada: \n`${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Abrir Jenkins>"
                } else {
                    slackSend color: "danger", message: "Processo Falhou :face_with_head_bandage: \n`${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Abrir Jenkins>"
                }
            }
        }
    }
}
