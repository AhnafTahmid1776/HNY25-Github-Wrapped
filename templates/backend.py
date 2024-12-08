from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

GITHUB_USERNAME = "AhnafTahmid1776"
GITHUB_TOKEN = "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"

def fetch_repositories():
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return []

@app.route('/')
def home():
    repos = fetch_repositories()
    return render_template('index.html', repos=repos)

@app.route('/api/repos')
def api_repos():
    repos = fetch_repositories()
    return jsonify(repos)

if __name__ == '__main__':
    app.run(debug=True)