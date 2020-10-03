"""For the ones that are too lazy to use git manually."""

from typing import Optional
import datetime
import logging
import os
import sys
import time

import git

class UsageError(Exception):
    pass

def configure_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stderr)
    handler.setLevel(logging.INFO)
    fmt = logging.Formatter('%(asctime)s|%(name)s|%(levelname)s: %(message)s')
    handler.setFormatter(fmt)
    logger.addHandler(handler)
    return logger

LOG = configure_logger()

def watch(path: str, interval_secs: int, init_if_not_exist: bool = True):
    repo = get_repo(path, init_if_not_exist)
    LOG.info('Watching %s, refresh interval %ds', path, interval_secs)
    while True:
        LOG.info('Scanning...')
        updated = False
        try:
            repo.git.add('-u')
            repo.git.add('.')
            if not has_commit(repo) or repo.index.diff('HEAD'):
                msg = make_commit_message()
                repo.index.commit(msg)
                LOG.info('New commit made: %s', msg)
                updated = True
        except Exception as e:
            LOG.error(e)
        if not updated:
            LOG.info('No changes were made')
        time.sleep(interval_secs)

def get_repo(path: str, init_if_not_exist=True) -> git.Repo:
    try:
        return git.Repo(path)
    except git.InvalidGitRepositoryError:
        if init_if_not_exist:
            LOG.info('Initializing new repo...')
            repo = git.Repo.init(path)
            return repo
        raise UsageError(f'{path} is not a git directory')

def make_commit_message(now: Optional[datetime.datetime] = None):
    if not now:
        now = datetime.datetime.now()
    return now.strftime('checkpoint at %Y-%m-%d %H:%M:%S')

def has_commit(repo: git.Repo) -> bool:
    try:
        repo.commit()
        return True
    except ValueError:
        return False