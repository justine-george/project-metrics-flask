import json
from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


def load_projects():
    with open('data/projects.json', 'r') as file:
        return json.load(file)


projects = load_projects()


@app.route('/extensions/<extensionId>/usercount', methods=['GET'])
def get_extension_user_count(extensionId):
    if not extensionId:
        return jsonify({'error': 'Empty extensionId parameter'}), 400

    # scrape the webstore for the user count
    chromeWebStoreUrl = f"https://chrome.google.com/webstore/detail/{extensionId}"

    # redirect loop detection - find a way to handle this better
    response = requests.get(chromeWebStoreUrl, allow_redirects=False)
    if response.status_code == 302 or response.status_code == 301:
        project = list(
            filter(lambda t: t["extensionId"] == extensionId, projects))
        if len(project) == 0:
            return jsonify({'error': 'Extension not found'}), 404
        return jsonify({'users': project[0]['metrics']['users']})

    elif response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup)
        user_count_meta = soup.find('meta', itemprop='interactionCount')

        if user_count_meta:
            # format: <meta content=UserDownloads:number />
            user_count = user_count_meta.get('content', '').split(':')[1]
            return jsonify({'users': user_count})
        else:
            return jsonify({'error': 'User count meta tag not found'}), 404
    else:
        return jsonify({'error': 'Failed to fetch the web page'}), response.status_code


# Deprecated
@app.route('/projects/usercount', methods=['GET'])
def get_employees():
    name = request.args.get('name')

    if name is None:
        return jsonify({'error': 'Empty name parameter'})

    project = list(filter(lambda t: t["name"] == name, projects))

    if len(project) == 0:
        return jsonify({'error': 'Project not found'})

    return jsonify({'users': project[0]['metrics']['users']})
