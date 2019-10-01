# Start ec2 instances for using boto3

import boto3

client = boto3.client("ec2")

client.start_instances(
    InstanceIds= ['i-0bf217cc5559c5a30','i-0f5484751e0cb9086']
)