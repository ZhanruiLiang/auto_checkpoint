import datetime
import unittest

from auto_checkpoint import auto_checkpoint

class AutoCheckpointTest(unittest.TestCase):

    def test_make_commit_message(self):
        now = datetime.datetime.strptime('2020-02-20 18:12:34', '%Y-%m-%d %H:%M:%S')
        self.assertEqual(auto_checkpoint.make_commit_message(now), 'checkpoint at 2020-02-20 18:12:34')

if __name__ == '__main__':
    unittest.main()