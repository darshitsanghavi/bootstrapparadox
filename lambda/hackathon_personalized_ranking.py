import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    personalizeRt = boto3.client('personalize-runtime')
    response = personalizeRt.get_personalized_ranking(
        campaignArn="Campaign arn",
        userId='UserID',
        inputList=['ItemID1', 'ItemID2'])
    print("Personalized Ranking")
    for item in response['personalizedRanking']:
        print(item['itemId'])

    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }
