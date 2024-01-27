#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge.

    The first argument will be the repository name
    The second argument will be the owner name
    You must use the packages requests and sys
    You are not allowed to import packages other than requests and sys
    You don’t need to check arguments passed to the script (number or type)
"""

import sys
import requests


if __name__ == "__main__":
    repository_name, repository_owner = sys.argv[1], sys.argv[2]
    url = (
        f"https://api.github.com/repos/"
        f"{repository_owner}/{repository_name}/commits"
    )

    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:
        sha = commit.get("sha")
        author_name = commit.get("commit").get("author").get("name")
        print(f"{sha}: {author_name}")
