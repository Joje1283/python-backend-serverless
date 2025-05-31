import boto3

# 설정
region = 'ap-northeast-2'

# 클라이언트 생성
def get_sqs_client():
    """Create and return an SQS client."""
    return boto3.client('sqs', region_name=region)