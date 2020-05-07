# Devops_Automation_project

# Devops_Automation_project

## About Project:
This project is to automate a great use-case of industry. This is a small infrastructure that is mostly used in every IT industry. Various DevOps tools such as git, Github, Jenkins, docker are used in this project

## Workflow:
![alt text](https://github.com/aakash1003/Devops_Automation_project/blob/master/workflow.jpg)

## Step 1: to automate git, as soon as you commit your code it will automatically be pushed to your GitHub repository.
For this purpose, we have to use hooks
![alt text](https://github.com/aakash1003/Devops_Automation_project/blob/master/2.PNG)
![alt text](https://github.com/aakash1003/Devops_Automation_project/blob/master/1.PNG)

## Step 2: Now the master branch code will go to the Jenkins and it will trigger the job 2.

## Step 3: Now the triggered job will do its work. It will copy the data to the folder in the host os and then the code is sent to the production system os by mounting the folder where the webserver is running in the docker os, which is triggered by this job as it is the down-stream of this job and clients can connect through the IP.
![alt text](https://github.com/aakash1003/Devops_Automation_project/blob/master/main-1.PNG)
![alt text](https://github.com/aakash1003/Devops_Automation_project/blob/master/main-2.PNG)
![alt text](https://github.com/aakash1003/Devops_Automation_project/blob/master/mainOS.PNG)


## Step 4: It will also go to job 1 when there is any commit in the feature branch and triggered the job 1.

## Step 5: The job 1 will now run the job where it will copy the data into the folder and launch the testing os with the mounting of that folder and this is used by the testing team to test the code.

![alt text](https://github.com/aakash1003/Devops_Automation_project/blob/master/training-1.PNG)
![alt text](https://github.com/aakash1003/Devops_Automation_project/blob/master/training-2.PNG)
![alt text](https://github.com/aakash1003/Devops_Automation_project/blob/master/trainingOS.PNG)

## Step 7 & 8: Now the quality assurance team (QAT) will check that code that it is working well or not and if it is ok then the job 3 will get triggered and code is uploaded to the production server.

![alt text](https://github.com/aakash1003/Devops_Automation_project/blob/master/pycode.PNG)


## Step 8, 9 & 10: In job 3 as the testing team have given the certificate then it will go to the GitHub & merge the code with the master branch code and also delete the testing os as we always want new os for testing that’s why we use Docker.

![alt text](https://github.com/aakash1003/Devops_Automation_project/blob/master/merge-1.PNG)
![alt text](https://github.com/aakash1003/Devops_Automation_project/blob/master/merge-2.PNG)
![alt text](https://github.com/aakash1003/Devops_Automation_project/blob/master/merge-3.PNG)
