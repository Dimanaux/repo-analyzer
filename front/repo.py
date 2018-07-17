import os
from datetime import datetime, timedelta

from git import Repo, GitCommandError
from git.objects.commit import Commit

from front.models import Task
from repo_analyzer.settings import BASE_DIR

"""
simple facade for GitPython lib
"""


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

    try:
        repo = Repo.clone_from(url, path)
    except GitCommandError:
        repo = Repo(path)
    return repo


def extract_repo_name(url: str):
    """
    Gets repository name from repository url.

    >> extract_repo_name('https://foo.bar/baz/foo-bar.baz.git')
    'foo-bar.baz'

    Args:
        url (str): url to remote git repository.

    Returns:
         str: Dir name for repo.
    """

    # extract file_name from url
    # eg foo-bar.baz.git
    repo_name_with_extension = url.split('/')[-1]

    try:
        repo_name_with_extension.index('.git')
    except ValueError:
        return repo_name_with_extension

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
    return repo.iter_commits(branch)


def date_time(commit: Commit):
    """
    Get datetime object representing the time the commit was created

    Args:
        commit (Commit): what commit to explore

    Returns:
        datetime: date and time of the commit
    """
    return commit.committed_datetime


def time_delta(commit: Commit):
    """
    Get time delta of the commit and his parent

    Args:
        commit (Commit): what commit to explore

    Returns:
        timedelta: time between commit and his parent
    """
    return commit.committed_datetime - commit.parents[0].commited_datetime


def has_commit(repository: Repo, task: Task):
    for c in commits(repository):
        if task.time_from < c.committed_datetime < task.time_to:
            return True
    return False
