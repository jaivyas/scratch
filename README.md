# Some quick and dirty scripts for automation
>
>
## *createthumbnail_lambda*
>This script/lambda function will convert images and videos to thumbnail and store it to specified s3 bucket.

#### Pre-requisites:
>Install below python modules in your working directory:

```
pip3 install opencv-python -t ~/mywork/personal/createthumbnail_lambda/
pip3 install Pillow -t ~/mywork/personal/createthumbnail_lambda/
pip3 install  PIL -t ~/mywork/personal/createthumbnail_lambda/
pip3 install Image -t ~/mywork/personal/createthumbnail_lambda/
```
#### Create zip file of createthumbnail_lambda and upload it to lambda via s3
 
## *ec2_delete_launch_job_lambda.py*
> Deletes ec2 instance with given tag name and create a new one with given AMI. Useful for periodic patches.

## *start_ec2_lambda.py*
> Start ec2 instance

## *kubeadm-installer* 
>Automated Installer for kubernetes using kubeadm tool

#### Pre-requisite:
```
Add the user and IPs of master and worker nodes to kubeadm-all.sh
MASTER_IP="master01"
WORKER_IPs=(worker01 worker02)
USER=ubuntu
```

#### How to:
```
Get all the scripts and yml file from kubeadm-installer directory of the repo
#bash 	kubeadm-all.sh
```

## *minikube*
> Automated Installer for kubernetes using minikube

#### How to:
```
#bash minikube-install.sh
```
