""" Lambda to delete old ec2-instance and launch ec2-instance with scheduled job"""
import boto3

REGION = 'us-east-1' # region to launch instance.
AMI = 'ami-9ebsdsa'
INSTANCE_TYPE = 't2.small' # instance type to launch.
boto3 = boto3.Session(profile_name='myprofile')

EC2 = boto3.client('ec2', region_name=REGION)


def weekly_lambda(event,context=None):
    terminate_ec2(self=None)
    spin_ec2(self=None)


def terminate_ec2(self):
    custom_filter = [
    {'Name': 'tag:Name', 'Values':['test01']}
]
    response = EC2.describe_instances(Filters=custom_filter)
    print(response['Reservations'][0]['Instances'][0]['State']['Name'])
    response1 = response['Reservations'][0]['Instances'][0]['State']['Name']
    if response1 == "terminated":
        print("No instances to be deleted")
    else:
        InstanceId = response['Reservations'][0]['Instances'][0]['InstanceId']
        terminate_response = EC2.terminate_instances(InstanceIds=[InstanceId])



def spin_ec2(self):
    """ Lambda handler taking [message] and creating a httpd instance with an echo. """
    #message = event['message']
    init_script = """#!/bin/bash
echo "sleep 50" >> /etc/rc.local
echo "shutdown -H +5 >> /etc/rc.local"
sleep 50
shutdown -H +5"""

    print ('Running script:')
    print (init_script)

    instance = EC2.run_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        MinCount=1, # required by boto, even though it's kinda obvious.
        MaxCount=1,
        InstanceInitiatedShutdownBehavior='stop', # make shutdown in script terminate ec2
        UserData=init_script # file to run on instance init.
        
    )

    print ("New instance created.")
    instance_id = instance['Instances'][0]['InstanceId']
    print (instance_id)
    print (instance)
    EC2.create_tags(Resources=[instance_id], Tags=[{"Key" : "Name", 'Value': 'test01',},],)


