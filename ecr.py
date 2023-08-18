import boto3

# Specify your AWS credentials here
aws_access_key_id = 'AKIATXTYWQNPCP5P5BGJ'
aws_secret_access_key = 'M2DP+XDhe3is3TvrZyCDzGSiAGnO/jCXYqqxKJsI'
aws_region = 'ap-south-1'  # Change this to your desired region

ecr_client = boto3.client(
    'ecr',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)

repository_name = "medicine-tracker"
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)
