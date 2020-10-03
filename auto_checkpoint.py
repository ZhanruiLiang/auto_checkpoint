from typing import Optional
import datetime
import time

import git

class UsageError(Exception):
    pass

def watch(path: str, init_if_not_exist: bool = True, interval_secs: int = 120):
    repo = get_repo(path, init_if_not_exist)
    while True:
        try:
            pass
        except:
            pass
        time.sleep(interval_secs)

def get_repo(path: str, init_if_not_exist=True) -> git.Repo:
    try:
        return git.Repo(path)
    except git.InvalidGitRepositoryError:
        if init_if_not_exist:
            return git.Repo.init(path)
        raise UsageError(f'{path} is not a git directory')

def make_commit_message(now: Optional[datetime.datetime] = None):
    if not now:
        now = datetime.datetime.now()
    return now.strftime('checkpoint at %Y-%m-%d %H:%M:%S')

def has_update(repo: git.Repo) -> bool:
    pass