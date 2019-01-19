import os
import boto3

from flask import Flask, jsonify, request

app = Flask(__name__)





USERS_TABLE = os.environ['USERS_TABLE']


client = boto3.client('dynamodb', 'us-east-1')


# RETURN HELLO < WORLD
@app.route("/", methods=["GET"])
def hello():
    return jsonify({
        'message': 'Hello, world'
    })


# CREATE USER 
@app.route("/user", methods=["POST"])
def create_user():
    user_id = request.json.get('userId')
    name = request.json.get('name')
    if not user_id or not name:
        return jsonify({'error': 'Please provider userId and name'}), 400

    resp = client.put_item(
        TableName=USERS_TABLE,
        Item={
            'userId': {'S': user_id },
            'name': {'S': name }
        }
    )
    
    return jsonify({
        'userId': user_id,
        'name': name
    })


# GET: SINGLE USER
@app.route("/users/<string:user_id>", methods=["GET"])
def get_user(user_id):
    resp = client.get_item(
        TableName=USERS_TABLE,
        Key={
            'userId': { 'S': user_id }
        }
    )
    item = resp.get('Item')
    if not item:
        return jsonify({'error': 'User does not exist'}), 404

    return jsonify({
        'message': 'Returned item successfully',
        'item': {
            'userId': item.get('userId').get('S'),
            'name': item.get('name').get('S')
        }
    })


# GET: ALL USERS
@app.route("/users", methods=["GET"])
def get_all_users():
    resp = client.scan(
        TableName=USERS_TABLE
    )
    items = resp.get('Items')
    if not items:
        return jsonify({'error': 'User does not exist'}), 404

    return jsonify({
        'message': 'Retrieves all items',
        'items': items
    })
