import random

from flask import Flask, jsonify, request

app = Flask(__name__)



WORDS_LIST = [
                "eating", "sleeping", "exercising", 
                "jumping", "sweet coding", "Git pushing",
                "sitting"
                ]

# RETURN HELLO < WORLD
@app.route("/", methods=["GET"])
def hello():
    return jsonify({
        'message': 'Hello, world'
    })

# GET: MY CURENT STATUS
@app.route("/status", methods=["GET"])
def get_status():
    status = "I am {} right now".format(WORDS_LIST[random.randint(0, len(WORDS_LIST)-1)])
    resp = {
        'status': status
    }

    return jsonify(resp)


