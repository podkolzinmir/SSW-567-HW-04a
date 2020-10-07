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
    @mock.patch('requests.get')
    def testValidInput2(self, mockedReqs):
        mockedResponses = [0,0,0,0]
        mockedResponses[0] = HolderObject(b'[{"id" : "32808844", "name" : "GuessingGame"}, {"id" : "32816276", "name" : "GuessingGame2"}, {"id" : "31634961", "name" : "hello-world"}, {"id" : "31636381", "name" : "HelloJava"})
        mockedResponses[1] = HolderObject(b'[{"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}]')
        mockedResponses[2] = HolderObject(b'[{"author" : "bsb226"}, {"author" : "bsb226"}]')
        mockedResponses[3] = HolderObject(b'[{"author" : "bsb226"}, {"author" : "bsb226"}, {"author" : "bsb226"}]')

          
        mockedReqs.side_effect = mockedResponses
        self.assertEqual(getGitHubInfo('dangural'), [['CPE-695-Final-Project', 16], ['Design6', 1], ['dsd', 30], ['DSD20S', 1]], 
                'dangural has the folllowing repos and commits: CPE-695-Final-Project - 0, dsd - 0, Design6 - 1, DSD20S - 1')

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