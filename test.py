''' SSW 567 - HW04a
I pledge my honor that I have abided by the Stevens Honor System
Miriam Podkolzin '''


import unittest
import requests
import json
from solution import getGitHubInfo
import unittest.mock as mock


class TestHw04a(unittest.TestCase):
        
    def testValidInput2(self):
        with mock.patch('githubapi.GithubAPI', create=True) as MockgetGitHubInfo:
            MockgetGitHubInfo.return_value = [['CPE-695-Final-Project', 16], ['Design6', 1], ['dsd', 30], ['DSD20S', 1]]
            self.assertEqual(MockgetGitHubInfo('dangural'), [['CPE-695-Final-Project', 16], ['Design6', 1], ['dsd', 30], ['DSD20S', 1]], 
                'dangural has the folllowing repos and commits: CPE-695-Final-Project - 0, dsd - 0, Design6 - 1, DSD20S - 1')

    def testInvalidInput1(self):
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

        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()