from flask import Flask, jsonify, request

app = Flask(__name__)

games = [
    {
        "id": 1,
        "title": "The Last of Us",
        "platforms": ["PlayStation 3", "PlayStation 4", "PlayStation 5"]
    },

    {
        "id": 2,
        "title": "The Legend of Zelda: Breath of the Wild",
        "platforms": ["Nintendo Wii U", "Nintendo Switch"]
    },

    {
        "id": 3,
        "title": "Forza Horizon 3",
        "platforms": ["Xbox One"]
    }
]


@app.route("/games", methods=["GET"])
def get_games():
    return jsonify(games)


@app.route("/games/<int:id>", methods=["GET"])
def get_game_by_id(id):
    for game in games:
        if game.get("id") == id:
            return jsonify(game)


@app.route("/games/<int:id>", methods=["PUT"])
def edit_game_by_id(id):
    game_changed = request.get_json()
    for i, game in enumerate(games):
        if game.get("id") == id:
            games[i].update(game_changed)
            return jsonify(games[i])


@app.route("/games", methods=["POST"])
def add_new_game():
    new_game = request.get_json()
    games.append(new_game)
    return jsonify(games)


@app.route("/games/<int:id>", methods=["DELETE"])
def delete_game_by_id(id):
    for i, game in enumerate(games):
        if game.get("id") == id:
            del games[i]

    return jsonify(games)


app.run(port=5050, host="localhost", debug=True)
