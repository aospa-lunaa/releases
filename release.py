#!/usr/bin/python3

from github import Github
from pathlib import Path
import os
import sys

repo_name = "aospa-lunaa/releases"

home = str(Path.home())
token = str(open(f"{home}/.githubtoken", "r").read().strip())
g = Github(token)

zip = os.path.abspath(sys.argv[1])
zip_name = zip.split("/")[-1]

rom = zip_name.split("-")[0]
version = zip_name.split("-")[1]
officialstat = zip_name.split("-")[2]
codename = zip_name.split("-")[3]
date = zip_name.split("-")[4]
time = zip_name.split("-")[5]

tag = f"{rom}-{version}-{officialstat}-{codename}-{date}-{time}"

repo = g.get_repo(repo_name)

release = repo.create_git_release(tag, zip_name, f"Automated release of {tag}")
print("Uploading build...")
release.upload_asset(zip)
print("Build uploaded!")
print(f"Release created: https://github.com/{repo_name}/releases/tag/{tag}")
