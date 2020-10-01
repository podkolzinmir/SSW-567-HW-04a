''' SSW 567 - HW04a
I pledge my honor that I have abided by the Stevens Honor System
Miriam Podkolzin '''

import requests
import json

# Function that takes in a GitHub user ID and outputs a list of the names of 
# the repositories that the user has, along with the number of commits that are
# in each of the listed repositories
def getGitHubInfo(GitHubUserId):
    try:
        urlString =  "https://api.github.com/users/" + GitHubUserId + "/repos"
    except TypeError as error:
        return "gitHubUserId must be a string"
    resultList = []
    gitHubInfo = requests.get(urlString)
    gitHubInfoJson = json.loads(gitHubInfo.content)
    for repo in gitHubInfoJson:
        gitCommits = requests.get("https://api.github.com/repos/" + GitHubUserId + "/" + repo['name'] + "/commits")
        gitCommitsJson = json.loads(gitCommits.content)
        count = 0
        for commitItem in gitCommitsJson:
            count += 1
        resultList.append([repo['name'], count])
    return resultList 