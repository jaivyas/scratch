#!/bin/bash
MASTER_IP="ec2-UB01"
WORKER_IPs=(ec2-UB02)
INSTALLER_SCRIPT="kubeadm-installer.sh"
MASTER_CONFIG_SCRIPT="kubeadm-master.sh"
USER=ubuntu

echo -e "copying installer to $MASTER_IP"
scp $INSTALLER_SCRIPT $USER@$MASTER_IP:.
for i in ${WORKER_IPs[@]}; do
	echo -e "copying installer to $i"
	scp $INSTALLER_SCRIPT $USER@$i
done

echo -e "Installing on $MASTER_IP"
ssh $USER@$MASTER_IP "bash $INSTALLER_SCRIPT"

for i in ${WORKER_IPs[@]}; do
  echo -e "Installing on $i"
  ssh $USER@$MASTER_IP "bash $INSTALLER_SCRIPT" 
done

echo -e "Configuring master"

ssh $MASTER_IP "sudo kubeadm init"

CMD=$(ssh $MASTER_IP "sudo kubeadm token create --print-join-command")

echo -e "Master should be ready"

echo -e "Joining slaves to master"

for i in ${WORKER_IPs[@]}; do
  echo -e "Joining $i"
  ssh $USER@$i "sudo $CMD"
done
