import requests

# Replace with your GitHub username and PAT
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
        repos = response.json()
        return repos
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return []

repos = fetch_repositories()

# Example: Print repo names
for repo in repos:
    print(f"Repo: {repo['name']}, Stars: {repo['stargazers_count']}, Language: {repo['language']}")
