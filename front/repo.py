from git import Repo
from git.objects.commit import Commit

import os
from repo_analyzer.settings import BASE_DIR

from datetime import datetime, timedelta


def create_dir(path: str):
    """
    Recursively creates directory

    Args:
        path: path to create
    """
    os.makedirs(path, exist_ok=True)


def clone(url: str):
    """
    Clones repo by url

    Args:
        url (str): url to remote git repository.

    Returns:
        git.Repo: Cloned git.Repo object.
    """

    repo_name = extract_repo_name(url)

    path = os.path.join(BASE_DIR, 'res', repo_name)
    create_dir(path)

    repo = Repo.clone_from(url, path)

    return repo


def extract_repo_name(url: str):
    """
    Gets repository name from repository url.

    >> extract_repo_name('https://foo.bar/baz/foo-bar.baz.git'
    'foo-bar.baz'

    Args:
        url (str): url to remote git repository.

    Returns:
         str: Dir name for repo.
    """
    # extract file_name from url
    # eg foo-bar.baz.git
    repo_name_with_extension = url.split('/')[-1]

    # split by . in order to get rid of extension .git
    split = repo_name_with_extension.split('.')

    # join chunks w/out last one -- (.git)
    repo_name: str = '.'.join(split[:-1])
    return repo_name


def commits(repo: Repo, branch: str = 'master'):
    """
    Returns commits of repo from selected branch.
    The default branch is master.

    Args:
        repo (Repo): repo
        branch (str): default=master
    Returns:
        list<commit>: repo commits from chosen branch
    """
    return list(repo.iter_commits(branch))


def datetime(commit: Commit):
    """
    Get datetime object representing the time the commit was created

    Args:
        commit (Commit): what commit to explore

    Returns:
        datetime: date and time of the commit
    """
    return commit.committed_datetime
