''' SSW 567 - HW04a
I pledge my honor that I have abided by the Stevens Honor System
Miriam Podkolzin '''


import unittest
from solution import getGitHubInfo
from unittest import mock
from unittest.mock import Mock


class TestHw04a(unittest.TestCase):
    def testValidInput2(self):
        with mock.patch('solution.getGitHubInfo', create='gitHubUserId must be a string' ) as MockGithub:
            MockGithub.return_value = 'dangural has the folllowing repos and commits: CPE-695-Final-Project - 0, dsd - 0, Design6 - 1, DSD20S - 1'
            self.assertEqual(MockGithub('dangural'), 'dangural has the folllowing repos and commits: CPE-695-Final-Project - 0, dsd - 0, Design6 - 1, DSD20S - 1')
       


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()