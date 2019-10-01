import boto3

client = boto3.client('ec2')

resp = client.describe_instances(
    Filters = [
        {
            'Name': 'tag:Env',
            'Values': ['Prod']
        }
    ]
)

for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        # Get Volume on specific Instance
        for volume in instance['BlockDeviceMappings']:
            vol_id = volume['Ebs']['VolumeId']
            print(f"Volume Id is {vol_id}")