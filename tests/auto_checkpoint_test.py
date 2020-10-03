import datetime
import unittest

from auto_checkpoint import auto_checkpoint

class AutoCheckpointTest(unittest.TestCase):

    def test_make_commit_message(self):
        now = datetime.datetime.strptime('2020-02-20 18:12:34', '%Y-%m-%d %H:%M:%S')
        self.assertEqual(auto_checkpoint.make_commit_message(now), 'checkpoint at 2020-02-20 18:12:34')

    def test_should_check(self):
        self.assertEqual(auto_checkpoint.should_track('/a/b/c'), True)

if __name__ == '__main__':
    unittest.main()