import boto3
ec2 = boto3.client('ec2')

resp = ec2.describe_instances(
    Filters = [
        {
            'Name': 'instance-state-name',
            'Values':['running']
        }
    ]
)

for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        id = instance['InstanceId']
        print(f"Instance Id is {id}")
        ec2.stop_instances(
            InstanceIds = [id]
        )