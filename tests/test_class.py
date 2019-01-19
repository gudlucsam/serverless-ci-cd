import os
import unittest
import boto3
from moto import mock_dynamodb2


class TestDynamo(unittest.TestCase):

    def setUp(self):
        self.table_name = 'users-table-dev'
        self.dynamodb = boto3.resource('dynamodb', 'us-east-1')
        
    @mock_dynamodb2
    def test_create_user(self):
        
        try:
            table = self.dynamodb.create_table(
                TableName=self.table_name,
                KeySchema=[
                    {
                        'AttributeName': 'userId',
                        'KeyType': 'HASH'
                    },
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'userId',
                        'AttributeType': 'S'
                    },

                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            )

            item = {
            'userId': 'qwwrwegregvf123',
            'name': 'samuel atule'
            }

            table.put_item(Item=item)

            table = self.dynamodb.Table(self.table_name)
            response = table.get_item(
                Key={
                    'userId': 'qwwrwegregvf123'
                }
            )
            if 'Item' in response:
                responseItem = response['Item']

            self.assertEqual(response['ResponseMetadata']["HTTPStatusCode"], 200) # status code is 200?
            self.assertTrue("userId" in responseItem)
            self.assertEqual(item["userId"], responseItem['userId'])

        except:
            print("error occurred")

        

    @mock_dynamodb2
    def test_get_users(self):
        try:
            table = self.dynamodb.create_table(
                TableName=self.table_name,
                KeySchema=[
                    {
                        'AttributeName': 'userId',
                        'KeyType': 'HASH'
                    },
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'userId',
                        'AttributeType': 'S'
                    },

                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            )

            items = [
                    {'userId': 'qwwrwegregvf123','name': 'samuel atule'},
                    {'userId':'wedfwetwertre', 'name': 'Tidoo Mustapha'}
                ]
            for item in items:
                table.put_item(Item=item)

            table = self.dynamodb.Table(self.table_name)
            response = table.scan(
                TableName=self.table_name
            )

            self.assertEqual(response['ResponseMetadata']["HTTPStatusCode"], 200)
            self.assertTrue("Items" in response)
        except:
            print("error occurred")
        

        

