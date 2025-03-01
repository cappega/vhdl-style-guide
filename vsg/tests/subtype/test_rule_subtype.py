import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import subtype
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','type_definition','type_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleSubtypeMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = subtype.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'subtype')
        self.assertEqual(oRule.identifier, '001')
        dExpected = [51]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = subtype.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'subtype')
        self.assertEqual(oRule.identifier, '003')
        dExpected = [65]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003_w_2_spaces(self):
        oRule = subtype.rule_003()
        oRule.spaces = 2
        dExpected = [51]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
