import json
from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


def load_projects():
    with open('data/projects.json', 'r') as file:
        return json.load(file)


projects = load_projects()


@app.route('/projects/usercount', methods=['GET'])
def get_employees():
    name = request.args.get('name')

    if name is None:
        return jsonify({'error': 'Empty name parameter'})

    project = list(filter(lambda t: t["name"] == name, projects))

    if len(project) == 0:
        return jsonify({'error': 'Project not found'})

    return jsonify({'users': project[0]['metrics']['users']})
