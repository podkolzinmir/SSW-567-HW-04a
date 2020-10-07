''' SSW 567 - HW04a
I pledge my honor that I have abided by the Stevens Honor System
Miriam Podkolzin '''


import unittest
from solution import getGitHubInfo
from unittest import mock
from unittest.mock import Mock

class HolderObject(object):
    def __init__(self, content):
        self.content = content

class TestHw04a(unittest.TestCase):
    def testValidInput2(self):
        with mock.patch('githubapi.GithubAPI', create='gitHubUserId must be a string' ) as MockGithub:
            MockGithub.return_value = 'dangural has the folllowing repos and commits: CPE-695-Final-Project - 0, dsd - 0, Design6 - 1, DSD20S - 1'
            self.assertEqual(MockGithub('dangural'), 'dangural has the folllowing repos and commits: CPE-695-Final-Project - 0, dsd - 0, Design6 - 1, DSD20S - 1')
       

 '''   def testInvalidInput1(self):
        with mock.patch('githubapi.GithubAPI', create=True) as MockgetGitHubInfo:
            MockgetGitHubInfo.return_value = 'gitHubUserId must be a string'
            self.assertEqual(MockgetGitHubInfo(77), 'gitHubUserId must be a string', 'A string may be passed to getGitHubInfo().')
      
    def testInvalidInput2(self):
        with mock.patch('githubapi.GithubAPI', create=True) as MockgetGitHubInfo:
            MockgetGitHubInfo.return_value = 'gitHubUserId must be a string'
            self.assertEqual(MockgetGitHubInfo(False), 'gitHubUserId must be a string', 'A string may be passed to getGitHubInfo().')
        
    def testInvalidInput3(self):
        with mock.patch('githubapi.GithubAPI', create=True) as MockgetGitHubInfo:
            MockgetGitHubInfo.return_value = 'gitHubUserId must be a string'
            self.assertEqual(MockgetGitHubInfo(9.5), 'gitHubUserId must be a string', 'A string may be passed to getGitHubInfo().')
        
    def testInvalidInput4(self):
        with mock.patch('githubapi.GithubAPI', create=True) as MockgetGitHubInfo:
            MockgetGitHubInfo.return_value = 'gitHubUserId must be a string'
            self.assertEqual(MockgetGitHubInfo([1, 2, 3, 4, 5]), 'gitHubUserId must be a string', 'Only a string may be passed to getGitHubInfo().')
       
    def testInvalidInput5(self):
        with mock.patch('githubapi.GithubAPI', create=True) as MockgetGitHubInfo:
            MockgetGitHubInfo.return_value = 'gitHubUserId must be a string'
            self.assertEqual(MockgetGitHubInfo((1, 2, 3, 4, 5)), 'gitHubUserId must be a string', 'Only a string may be passed to getGitHubInfo().')

    def testInvalidInput6(self):
        with mock.patch('githubapi.GithubAPI', create=True) as MockgetGitHubInfo:
            MockgetGitHubInfo.return_value = 'gitHubUserId must be a string'
            self.assertEqual(MockgetGitHubInfo({'podkolzinmir':'haydendaly'}), 'gitHubUserId must be a string', 'Only a string may be passed to getGitHubInfo().')

        '''
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()