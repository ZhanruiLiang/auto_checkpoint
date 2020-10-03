"""For the ones that are too lazy to use git manually."""

from typing import Optional
import argparse
import datetime
import logging
import os
import sys
import time

import git

class UsageError(Exception):
    pass

def watch(path: str, init_if_not_exist: bool = True, interval_secs: int = 120):
    repo = get_repo(path, init_if_not_exist)
    while True:
        try:
            files_to_track = list(filter(should_track, repo.untracked_files))
            repo.index.add(files_to_track)
            if repo.index.diff(None):
                msg = make_commit_message()
                repo.git.add('-u')
                repo.index.commit(msg)
                logging.info('New commit made: %s', msg)
        except Exception as e:
            logging.error(e)
        time.sleep(interval_secs)

def get_repo(path: str, init_if_not_exist=True) -> git.Repo:
    try:
        return git.Repo(path)
    except git.InvalidGitRepositoryError:
        if init_if_not_exist:
            logging.info('Initializing new repo...')
            return git.Repo.init(path)
        raise UsageError(f'{path} is not a git directory')

def make_commit_message(now: Optional[datetime.datetime] = None):
    if not now:
        now = datetime.datetime.now()
    return now.strftime('checkpoint at %Y-%m-%d %H:%M:%S')

def should_track(subpath: str) -> bool:
    dir_ = subpath
    while dir_:
        dir_, name = os.path.split(subpath)
        if name.startswith('.') or name.startswith('__'):
            return False
    return True

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('path', metavar='PATH', type=str, help='The path to watch')
    parser.add_argument('--interval', type=int, help='The refresh interval in seconds')
    args = parser.parse_args(argv)
    watch(args.path, interval_secs=args.interval)

if __name__ == '__main__':
    main(sys.argv)