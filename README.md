# Auto Checkpoint
Automatically makes checkpoints using git to reduce the risk of losing progress of your work.

## Install
```
python setup.py install --user
```

## Usage
In any terminal,
```
python -m auto_checkpoint <path/to/watch>
```
The specified path will be watched and `git commit` will be run periodically to add checkpoints. 
To configure the check interval, for example, to 120 seconds, use something like:
```
python -m auto_checkpoint --interval 120 /tmp/foo_project
```

For more help, see:
```
python -m auto_checkpoint -h
```