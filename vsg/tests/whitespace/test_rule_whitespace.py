
import os
import unittest

from vsg.rules import whitespace
from vsg import vhdlFile
from vsg import line
from vsg.tests import utils

sFileName = os.path.join(os.path.dirname(__file__),'..','whitespace','whitespace_test_input.txt')

class testRuleWhitespaceMethods(unittest.TestCase):

    def setUp(self):
        self.lFile = utils.read_vhdlfile(sFileName)
        self.oFile = vhdlFile.vhdlFile(self.lFile)

    def test_001(self):
        oRule = whitespace.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '001')
        self.assertEqual(oRule.phase, 2)

        dExpected = [2,4]
        self.oFile.lines.append(line.line('  This is a test of ending whitespace'))
        self.oFile.lines.append(line.line('  This is a test of ending whitespace '))
        self.oFile.lines.append(line.line('  This is a test of ending whitespace'))
        self.oFile.lines.append(line.line('  This is a test of ending whitespace  '))
        self.oFile.lines.append(line.line('  This is a test of ending whitespace'))
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_002(self):
        oRule = whitespace.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '002')
        self.assertEqual(oRule.phase, 0)

        dExpected = [1,2,5]
        self.oFile.lines.append(line.line('  This is a test of tabs\t'))
        self.oFile.lines.append(line.line('\tThis is a test of tabs'))
        self.oFile.lines.append(line.line('  This is a test of tabs'))
        self.oFile.lines.append(line.line('  This is a test of tabs'))
        self.oFile.lines.append(line.line('  This is a \t test of tabs'))
        self.oFile.lines.append(line.line('  This is a test of tabs'))
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_003(self):
        oRule = whitespace.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '003')
        self.assertEqual(oRule.phase, 2)

        dExpected = [2,4,6]
        self.oFile.lines.append(line.line('  This is a test of tabs;'))
        self.oFile.lines.append(line.line('  This is a test of tabs ;'))
        self.oFile.lines.append(line.line('  This is a test of tabs;'))
        self.oFile.lines.append(line.line('  This is a test of tabs    ;'))
        self.oFile.lines.append(line.line('  This is a test; of tabs'))
        self.oFile.lines.append(line.line('  This is a test ; of tabs'))
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_004(self):
        oRule = whitespace.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '004')
        self.assertEqual(oRule.phase, 2)

        dExpected = [2,4,6]
        self.oFile.lines.append(line.line('  This is a test of commas,'))
        self.oFile.lines.append(line.line('  This is a test of commas ,'))
        self.oFile.lines.append(line.line('  This is a test of commas,'))
        self.oFile.lines.append(line.line('  This is a test of commas    ,'))
        self.oFile.lines.append(line.line('  This is a test, of commas'))
        self.oFile.lines.append(line.line('  This is a test , of commas'))
        self.oFile.lines.append(line.line('  This is a test, of commas -- This is a comment ,'))
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_005(self):
        oRule = whitespace.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '005')
        self.assertEqual(oRule.phase, 2)

        dExpected = [1,3,5]
        self.oFile.lines.append(line.line('  This is a test of parenthesis ( failure'))
        self.oFile.lines.append(line.line('  This is a test of parenthesis (pass'))
        self.oFile.lines.append(line.line('  This is a test of parentehsis (  failure'))
        self.oFile.lines.append(line.line('  This is a test of parentehsis (  7 pass'))
        self.oFile.lines.append(line.line('  This is a test of parenthesis ( pass) --  ( pass'))
        self.oFile.lines.append(line.line(' --  This is a test of parenthesis ( pass)'))
        self.oFile.lines[5].hasComment = True
        self.oFile.lines[6].isComment = True
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(self.oFile.lines[1].line, '  This is a test of parenthesis (failure')
        self.assertEqual(self.oFile.lines[2].line, '  This is a test of parenthesis (pass')
        self.assertEqual(self.oFile.lines[3].line, '  This is a test of parentehsis (failure')
        self.assertEqual(self.oFile.lines[4].line, '  This is a test of parentehsis (  7 pass')
        self.assertEqual(self.oFile.lines[5].line, '  This is a test of parenthesis (pass) --  ( pass')
        self.assertEqual(self.oFile.lines[6].line, ' --  This is a test of parenthesis ( pass)')


    def test_006(self):
        oRule = whitespace.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '006')
        self.assertEqual(oRule.phase, 2)

        dExpected = [1,3,5]
        self.oFile.lines.append(line.line('  This is a test of parenthesis (failure )'))
        self.oFile.lines.append(line.line('  This is a test of parenthesis (pass)'))
        self.oFile.lines.append(line.line('  This is a test of parentehsis (failure   )'))
        self.oFile.lines.append(line.line('   ) pass'))
        self.oFile.lines.append(line.line('  This is a test of parentehsis (pass ) --  ) pass'))
        self.oFile.lines[5].hasComment = True
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(self.oFile.lines[1].line, '  This is a test of parenthesis (failure)')
        self.assertEqual(self.oFile.lines[2].line, '  This is a test of parenthesis (pass)')
        self.assertEqual(self.oFile.lines[3].line, '  This is a test of parentehsis (failure)')
        self.assertEqual(self.oFile.lines[4].line, '   ) pass')
        self.assertEqual(self.oFile.lines[5].line, '  This is a test of parentehsis (pass) --  ) pass')

    def test_007(self):
        oRule = whitespace.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '007')
        self.assertEqual(oRule.phase, 2)

        dExpected = [1,3]
        self.oFile.lines.append(line.line('  This is a test,of commas (failure )'))
        self.oFile.lines.append(line.line('  This is a test, of commas (pass)'))
        self.oFile.lines.append(line.line('  This is a test of commas,(failure   )'))
        self.oFile.lines.append(line.line('  This is a test of commas -- 1,2,3,4 (PASS)'))
        self.oFile.lines.append(line.line('   ) pass'))
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_008(self):
        oRule = whitespace.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '008')
        self.assertEqual(oRule.phase, 2)

        dExpected = [1,3]
        self.oFile.lines.append(line.line('  std_logic_vector (7 downto 0)'))
        self.oFile.lines.append(line.line('  std_logic_vector(7 downto 0)'))
        self.oFile.lines.append(line.line('  std_logic_vector   (7 downto 0)'))
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_010(self):
        oRule = whitespace.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '010')
        self.assertEqual(oRule.phase, 2)

        dExpected = [1, 3]
        self.oFile.lines.append(line.line('  a <= b& c'))
        self.oFile.lines.append(line.line('  a <= b & c'))
        self.oFile.lines.append(line.line('  a <= b &c'))
        self.oFile.lines.append(line.line('  a <= b &'))
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_011(self):
        oRule = whitespace.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '011')
        self.assertEqual(oRule.phase, 2)

        dExpected = [1,2,4,5,6,8,9,10,12,13,14,16,17,18,20,21,23,24,26]
        self.oFile.lines.append(line.line('  a <= b+ c'))   #1
        self.oFile.lines.append(line.line('  a <= b +c'))   #2
        self.oFile.lines.append(line.line('  a <= b + c'))  #3
        self.oFile.lines.append(line.line('  a <= b+c'))    #4
        self.oFile.lines.append(line.line('  a <= b- c'))   #5
        self.oFile.lines.append(line.line('  a <= b -c'))   #6
        self.oFile.lines.append(line.line('  a <= b - c'))  #7
        self.oFile.lines.append(line.line('  a <= b-c'))    #8
        self.oFile.lines.append(line.line('  a <= b/ c'))   #9
        self.oFile.lines.append(line.line('  a <= b /c'))   #10
        self.oFile.lines.append(line.line('  a <= b / c'))  #11
        self.oFile.lines.append(line.line('  a <= b/c'))    #12
        self.oFile.lines.append(line.line('  a <= b* c'))   #13
        self.oFile.lines.append(line.line('  a <= b *c'))   #14
        self.oFile.lines.append(line.line('  a <= b * c'))  #15
        self.oFile.lines.append(line.line('  a <= b*c'))    #16
        self.oFile.lines.append(line.line('  a <= b** c'))   #17
        self.oFile.lines.append(line.line('  a <= b **c'))   #18
        self.oFile.lines.append(line.line('  a <= b ** c'))  #19
        self.oFile.lines.append(line.line('  a <= b**c'))    #20
        self.oFile.lines.append(line.line('  a <= b**c -- This**is fine'))    #21
        self.oFile.lines.append(line.line('  a <= b ** c -- This**is fine'))    #22
        self.oFile.lines.append(line.line('  a <= )+ ('))   #23
        self.oFile.lines.append(line.line('  a <= ) +('))   #24
        self.oFile.lines.append(line.line('  a <= ) + ('))  #25
        self.oFile.lines.append(line.line('  a <= )+('))    #26
        self.oFile.lines.append(line.line('  G_FILE => "$DIR/somedir/somefile.txt",')) #27
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_012(self):
        oRule = whitespace.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '012')
        self.assertEqual(oRule.phase, 3)

        dExpected = [2,10]
        self.oFile.lines.append(line.line('  a <= b;'))   #1
        self.oFile.lines.append(line.blank_line())        #2
        self.oFile.lines.append(line.blank_line())        #3
        self.oFile.lines.append(line.blank_line())        #4
        self.oFile.lines.append(line.blank_line())        #5
        self.oFile.lines.append(line.line('  c <= d;'))   #6
        self.oFile.lines.append(line.line('  a <= b;'))   #7
        self.oFile.lines.append(line.blank_line())        #8
        self.oFile.lines.append(line.line('  c <= d;'))   #9
        self.oFile.lines.append(line.blank_line())        #10
        self.oFile.lines.append(line.blank_line())        #11
        self.oFile.lines.append(line.line('  a <= b;'))   #12
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
