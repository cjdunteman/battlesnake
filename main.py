import logging
import os

from flask import Flask
from flask import request

import logic

app = Flask(__name__)

@app.get("/")
def handle_info():
    return {
            "apiversion": "1",
            "author": "cjdunteman",
            "color": "#9933ff",
            "head": "default",
            "tail": "default",
            }


@app.post("/start")
def handle_start():
    data = request.get_json()

    print(data['game']['id'])
    return "ok"

@app.post("/move")
def handle_move():
    data = request.get_json()

    my_head = data["you"]["head"]
    my_body = data["you"]["body"]

    print(f"TURN: {data['turn']} MODE: {data['game']['ruleset']['name']}")
    print(f"HEAD: {my_head}")
    print(f"BODY: {my_body}")

    possible_moves = ["up", "down", "left", "right"]

    return {"move": move}

@app.post("/end")
def end():
    return "ok"

if __name__ == "__main__":
    logging.getLogger("werkzeug").setLevel(logging.ERROR)

    print("Starting Battlesnake Server...")
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port, debug=True)
