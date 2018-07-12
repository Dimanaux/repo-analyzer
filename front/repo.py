from git import Repo

import os

from repo_analyzer.settings import BASE_DIR


def clone(url: str):
    os.chdir(BASE_DIR + r'\\res\\')
    return os.system('git clone ' + url)
