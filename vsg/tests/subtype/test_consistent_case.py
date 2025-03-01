import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import subtype
from vsg import vhdlFile
from vsg.tests import utils


class testConsistentCase(unittest.TestCase):

    def setUp(self):
        # Read in test file used for all tests
        lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'consistent_case_test_input.vhd'))
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_002(self):
        oRule = subtype.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'subtype')
        self.assertEqual(oRule.identifier, '002')
        dExpected = [7,11]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_002(self):
        oRule = subtype.rule_002()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)

        self.assertEqual(self.oFile.lines[7].line, '  signal read  : read_size;')
        self.assertEqual(self.oFile.lines[11].line, '  constant write_sz : write_size := 1;')

        self.assertEqual(oRule.violations, [])
