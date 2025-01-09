import boto3

# Use the DynamoDB resource object
dynamodb = boto3.resource('dynamodb')

# Reference the table
table_name = "lotteryentriesdb"
table = dynamodb.Table(table_name)

def delete_db_item(partition_key_value):
    response = table.delete_item(
        Key={
            'name': partition_key_value
        }
    )
    return "Item successfully deleted"

def add_db_item(partition_key_value):
    response = table.put_item(
        Item={
            'name': partition_key_value
        }
    )
    return "Item successfully added"

def get_all_items():
    # Perform the initial scan
    response = table.scan()
    data = response['Items']  # Extract items

    # Handle pagination if LastEvaluatedKey exists
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    return data