from flask import Flask, jsonify

app = Flask(__name__)

names = [{"name":"John", "age":22, "id":0}, {"name":"Sam", "age":90,"id":1}, {"name":"george", "age":56,"id":2}]

@app.route("/")
def index():
    return "welcome"

@app.route("/names", methods=['GET'])
def get():
    return jsonify({'names':names})

@app.route("/names/<int:id>", methods=['GET'])
def get_name(id):
    return jsonify({'names':names[id]['name']})


@app.route("/names", methods=['POST'])
def create():
    name1 = {
        "name": "Saurabh",
        "id": 3,
        "age":89
    }
    names.append(name1)
    return jsonify({"created":names})

@app.route("/names/<int:id>", methods=['PUT'])
def update(id):
    names[id]['name'] = "XYZ"
    return jsonify({"names":names})

@app.route("/names/<int:id>", methods=['DELETE'])
def delete_course(id):
    names.remove(names[id])
    return jsonify({"result":True})


if __name__ == "__main__":
    app.run(debug=True)