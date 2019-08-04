import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    personalizeRt = boto3.client('personalize-runtime')
    response = personalizeRt.get_recommendations(
        campaignArn="Campaign ARN",
        userId='User ID')
    print("Recommended items")
    for item in response['itemList']:
        print(item['itemId'])

    return {
        'statusCode': 200,
        'body': json.dumps(item))
    }
