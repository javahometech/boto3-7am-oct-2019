import boto3

client = boto3.client("ec2")

resp = client.describe_instances()

for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        print(instance['InstanceId'])
