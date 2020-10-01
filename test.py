''' SSW 567 - HW04a
I pledge my honor that I have abided by the Stevens Honor System
Miriam Podkolzin '''


import unittest
from solution import getGitHubInfo

class TestHw04a(unittest.TestCase):
        
    def testValidInput2(self):
        self.assertEqual(getGitHubInfo('dangural'), [['CPE-695-Final-Project', 16], ['Design6', 1], ['dsd', 30], ['DSD20S', 1]], 
                'dangural has the folllowing repos and commits: CPE-695-Final-Project - 0, dsd - 0, Design6 - 1, DSD20S - 1')

    def testInvalidInput1(self):
        self.assertEqual(getGitHubInfo(77), 'gitHubUserId must be a string', 'A string may be passed to getGitHubInfo().')
      
    def testInvalidInput2(self):
       self.assertEqual(getGitHubInfo(False), 'gitHubUserId must be a string', 'A string may be passed to getGitHubInfo().')
        
    def testInvalidInput3(self):
        self.assertEqual(getGitHubInfo(9.5), 'gitHubUserId must be a string', 'A string may be passed to getGitHubInfo().')
        
    def testInvalidInput4(self):
        self.assertEqual(getGitHubInfo([1, 2, 3, 4, 5]), 'gitHubUserId must be a string', 'Only a string may be passed to getGitHubInfo().')
       
    def testInvalidInput5(self):
        self.assertEqual(getGitHubInfo((1, 2, 3, 4, 5)), 'gitHubUserId must be a string', 'Only a string may be passed to getGitHubInfo().')

    def testInvalidInput6(self):
        self.assertEqual(getGitHubInfo({'podkolzinmir':'haydendaly'}), 'gitHubUserId must be a string', 'Only a string may be passed to getGitHubInfo().')

        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()