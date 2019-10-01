import boto3
client = boto3.client("ec2")

resp = client.describe_instances(
    Filters = [
        {
            'Name': 'instance-type',
            'Values':['t2.medium']
        }
    ]
)

for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        id = instance['InstanceId']
        type = instance['InstanceType']
        print(f"Instance Id is {id} and type is {type}")
