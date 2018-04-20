""" Lambda to launch ec2-instances with tag test01"""
import boto3

boto3 = boto3.Session(profile_name='myprofile')

def daily_lambda(event, context=None):
    start_ec2(self=None)

def start_ec2(self):
    custom_filter = [
    {'Name': 'tag:Name', 'Values':['test01']}
]
    response = EC2.describe_instances(Filters=custom_filter)
    InstanceId = response['Reservations'][0]['Instances'][0]['InstanceId']
    print(InstanceId)
    start_response = EC2.start_instances(InstanceIds=[InstanceId])
