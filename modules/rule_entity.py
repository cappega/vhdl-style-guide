
import rule
import re


def is_entity(fFlag, sLine):
    if re.match('\s*entity', sLine.lower()):
        return True
    return fFlag


class entity_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'entity'


class rule_001(entity_rule):
    '''Entity rule 001 checks for spaces before the entity keyword.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '001'
        self.description = 'Remove spaces before entity keyword.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s\s*entity', sLine.lower()):
                lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_002(entity_rule):
    '''Entity rule 002 checks for a single space after the entity keyword.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '002'
        self.description = 'Remove extra spaces after entity keyword.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*entity\s\s+', sLine.lower()):
                lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_003(entity_rule):
    '''Entity rule 003 checks for a blank line above the entity keyword.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '003'
        self.description = 'Add blank line above entity keyword.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*entity', sLine.lower()):
                if not re.match('^\s*$', lines[iLineNumber - 1]):
                    lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_004(entity_rule):
    '''Entity rule 004 checks the entity keyword is lower case.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '004'
        self.description = 'Change "entity" keyword to lowercase.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*entity', sLine.lower()):
                if not re.match('^\s*entity', sLine):
                    lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_005(entity_rule):
    '''Entity rule 005 checks the is keyword is on the same line as the entity keyword.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '005'
        self.description = 'Add "is" keyword to same line as "entity" keyword.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*entity', sLine.lower()):
                if not re.match('^.*\s\s*is', sLine.lower()):
                    lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines

class rule_006(entity_rule):
    '''Entity rule 006 checks the "is" keyword is lower case.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '006'
        self.description = 'Change "is" keyword to lowercase.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*entity\s.*\sis', sLine.lower()):
                if not re.match('^.*\s\s*is', sLine):
                    lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines

class rule_007(entity_rule):
    '''Entity rule 007 checks for a single space before the "is" keyword.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '007'
        self.description = 'Remove extra spaces before "is" keyword.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*entity', sLine.lower()):
                if re.match('^.*\s\s+is', sLine.lower()):
                    lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_008(entity_rule):
    '''Entity rule 008 checks for a blank line above the port keyword.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '008'
        self.description = 'Remove blank lines above "port" keyword.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*port', sLine.lower()):
                if re.match('^\s*$', lines[iLineNumber - 1].lower()):
                    lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_009(entity_rule):
    '''Entity rule 009 checks indentation of the "port" keyword.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '009'
        self.description = 'Change indent of "port" keyword to 2 spaces.'

    def analyze(self, lines):
        lFailureLines = []
        fEntityFound = False
        fPortMapFound = False
        for iLineNumber, sLine in enumerate(lines):
            if fEntityFound:
                if re.match('^\s*end', sLine.lower()):
                    fEntityFound = False
                    fPortMapFound = False
            if fEntityFound and not fPortMapFound:
                if re.match('^\s*port', sLine.lower()):
                    fPortMapFound = True
                    if not re.match('^\s\sport', sLine.lower()):
                        lFailureLines.append(iLineNumber + 1)
            fEntityFound = is_entity(fEntityFound, sLine)
        self.violations = lFailureLines


class rule_010(entity_rule):
    '''Entity rule 010 checks spacing between "port" and the open parenthesis.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '010'
        self.description = 'Change spacing between "port" and "(" to one space.'

    def analyze(self, lines):
        lFailureLines = []
        fEntityFound = False
        fPortMapFound = False
        for iLineNumber, sLine in enumerate(lines):
            if fEntityFound:
                if re.match('^\s*end', sLine.lower()):
                    fEntityFound = False
                    fPortMapFound = False
                if not fPortMapFound:
                    if re.match('^\s*port', sLine.lower()):
                        fPortMapFound = True
                        if not re.match('^\s*port \(', sLine.lower()):
                            lFailureLines.append(iLineNumber + 1)
            fEntityFound = is_entity(fEntityFound, sLine)
      
        self.violations = lFailureLines


class rule_011(entity_rule):
    '''Entity rule 011 checks indentation of ports.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '011'
        self.description = 'Change indent of port to 4 spaces.'

    def analyze(self, lines):
        lFailureLines = []
        fEntityFound = False
        fPortMapFound = False
        for iLineNumber, sLine in enumerate(lines):
            if fPortMapFound:
                if re.match('^\s*\w\w*\s*:\s*[in|out|inout]', sLine.lower()):
                    if not re.match('^\s\s\s\s\w', sLine):
                        lFailureLines.append(iLineNumber + 1)
            if fEntityFound:
                if re.match('^\s*end', sLine.lower()):
                    fEntityFound = False
                    fPortMapFound = False
                if re.match('^\s*port', sLine.lower()):
                    fPortMapFound = True
            fEntityFound = is_entity(fEntityFound, sLine)
        self.violations = lFailureLines


class rule_012(entity_rule):
    '''Entity rule 012 checks for a single space after the colon in a port declaration for "in" and "inout" ports.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '012'
        self.description = 'Reduce number of spaces after the colon to 1.'

    def analyze(self, lines):
        lFailureLines = []
        fEntityFound = False
        fPortMapFound = False
        for iLineNumber, sLine in enumerate(lines):
            if fPortMapFound:
                if re.match('^\s*\w\w*\s*:\s*in\s', sLine.lower()):
                    if not re.match('^\s*\w\w*\s*:\sin', sLine.lower()):
                        lFailureLines.append(iLineNumber + 1)
            if fEntityFound:
                if re.match('^\s*end', sLine.lower()):
                    fEntityFound = False
                    fPortMapFound = False
                if re.match('^\s*port', sLine.lower()):
                    fPortMapFound = True
            fEntityFound = is_entity(fEntityFound, sLine)
        self.violations = lFailureLines


class rule_013(entity_rule):
    '''Entity rule 013 checks for one space after the colon in a port declaration for "out" ports.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '013'
        self.description = 'Change number of spaces before "out" to 3.'

    def analyze(self, lines):
        lFailureLines = []
        fEntityFound = False
        fPortMapFound = False
        for iLineNumber, sLine in enumerate(lines):
            if fPortMapFound:
                if re.match('^\s*\w\w*\s*:\s*out\s', sLine.lower()):
                    if not re.match('^\s*\w\w*\s*:\sout', sLine.lower()):
                        lFailureLines.append(iLineNumber + 1)
            if fEntityFound:
                if re.match('^\s*end', sLine.lower()):
                    fEntityFound = False
                    fPortMapFound = False
                if re.match('^\s*port', sLine.lower()):
                    fPortMapFound = True
            fEntityFound = is_entity(fEntityFound, sLine)
        self.violations = lFailureLines


class rule_014(entity_rule):
    '''Entity rule 014 checks for four spaces after the "in" keyword in a port declaration for "in" ports.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '014'
        self.description = 'Change the number of spaces after the "in" keyword to four spaces.'

    def analyze(self, lines):
        lFailureLines = []
        fEntityFound = False
        fPortMapFound = False
        for iLineNumber, sLine in enumerate(lines):
            if fPortMapFound:
                if re.match('^\s*\w\w*\s*:\s*in\s', sLine.lower()):
                    if not re.match('^\s*\w\w*\s*:\s*in\s\s\s\s\w', sLine.lower()):
                        lFailureLines.append(iLineNumber + 1)
            if fEntityFound:
                if re.match('^\s*end', sLine.lower()):
                    fEntityFound = False
                    fPortMapFound = False
                if re.match('^\s*port', sLine.lower()):
                    fPortMapFound = True
            fEntityFound = is_entity(fEntityFound, sLine)
        self.violations = lFailureLines


class rule_015(entity_rule):
    '''Entity rule 015 checks for three spaces after "out" keyword in a port declaration for "out" ports.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '015'
        self.description = 'Change the number of spaces after the "out" keyword to three spaces.'

    def analyze(self, lines):
        lFailureLines = []
        fEntityFound = False
        fPortMapFound = False
        for iLineNumber, sLine in enumerate(lines):
            if fPortMapFound:
                if re.match('^\s*\w\w*\s*:\s*out\s', sLine.lower()):
                    if not re.match('^\s*\w\w*\s*:\s*out\s\s\s\w', sLine.lower()):
                        lFailureLines.append(iLineNumber + 1)
            if fEntityFound:
                if re.match('^\s*end', sLine.lower()):
                    fEntityFound = False
                    fPortMapFound = False
                if re.match('^\s*port', sLine.lower()):
                    fPortMapFound = True
            fEntityFound = is_entity(fEntityFound, sLine)
        self.violations = lFailureLines


class rule_016(entity_rule):
    '''Entity rule 016 checks for a single space after "inout" keyword in a port declaration for "inout" ports.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '016'
        self.description = 'Change the number of spaces after the "inout" keyword to one space.'

    def analyze(self, lines):
        lFailureLines = []
        fEntityFound = False
        fPortMapFound = False
        for iLineNumber, sLine in enumerate(lines):
            if fPortMapFound:
                if re.match('^\s*\w\w*\s*:\s*inout\s', sLine.lower()):
                    if not re.match('^\s*\w\w*\s*:\s*inout\s\w', sLine.lower()):
                        lFailureLines.append(iLineNumber + 1)
            if fEntityFound:
                if re.match('^\s*end', sLine.lower()):
                    fEntityFound = False
                    fPortMapFound = False
                if re.match('^\s*port', sLine.lower()):
                    fPortMapFound = True
            fEntityFound = is_entity(fEntityFound, sLine)
        self.violations = lFailureLines


class rule_017(entity_rule):
    '''Entity rule 017 checks the entity name is uppercase in the entity declaration line.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '017'
        self.description = 'Change entity name to all uppercase.'

    def analyze(self, lines):
        lFailureLines = []
        for iLineNumber, sLine in enumerate(lines):
            if re.match('^\s*entity', sLine.lower()):
                lLine = sLine.split()
                if lLine[1] != lLine[1].upper():
                    lFailureLines.append(iLineNumber + 1)
        self.violations = lFailureLines


class rule_018(entity_rule):
    '''Entity rule 018 checks for spaces before the "end" keyword.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '018'
        self.description = 'Change the number of spaces after the "inout" keyword to one space.'

    def analyze(self, lines):
        lFailureLines = []
        fEntityFound = False
        fPortMapFound = False
        for iLineNumber, sLine in enumerate(lines):
            if fEntityFound:
                if re.match('^\s*end', sLine.lower()):
                    if not re.match('^end', sLine.lower()):
                        lFailureLines.append(iLineNumber + 1)
            if re.match('\s*entity', sLine.lower()):
                fEntityFound = True
        self.violations = lFailureLines


class rule_019(entity_rule):
    '''Entity rule 019 checks the "end" keyword is lowercase.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '019'
        self.description = 'Change "end" keyword to lowercase.'

    def analyze(self, lines):
        lFailureLines = []
        fEntityFound = False
        fPortMapFound = False
        for iLineNumber, sLine in enumerate(lines):
            if fEntityFound:
                if re.match('^\s*end', sLine.lower()):
                    if not re.match('^\s*end', sLine):
                        lFailureLines.append(iLineNumber + 1)
            if re.match('\s*entity', sLine.lower()):
                fEntityFound = True
        self.violations = lFailureLines


class rule_020(entity_rule):
    '''Entity rule 020 checks for a single space after the "end" keyword'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '020'
        self.description = 'Reduce spaces after "end" keyword to one.'

    def analyze(self, lines):
        lFailureLines = []
        fEntityFound = False
        fPortMapFound = False
        for iLineNumber, sLine in enumerate(lines):
            if fEntityFound:
                if re.match('^\s*end', sLine.lower()):
                    if re.match('^\s*end\s\s+', sLine.lower()):
                        lFailureLines.append(iLineNumber + 1)
            if re.match('\s*entity', sLine.lower()):
                fEntityFound = True
        self.violations = lFailureLines


class rule_021(entity_rule):
    '''Entity rule 021 checks entity name is uppercase in "end" keyword line.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '021'
        self.description = 'Uppercase entity name.'

    def analyze(self, lines):
        lFailureLines = []
        fEntityFound = False
        fPortMapFound = False
        for iLineNumber, sLine in enumerate(lines):
            if fEntityFound:
                if re.match('^\s*end', sLine.lower()):
                    lLine = sLine.split()
                    if lLine[1] != lLine[1].upper():
                        lFailureLines.append(iLineNumber + 1)
            if re.match('\s*entity', sLine.lower()):
                fEntityFound = True
        self.violations = lFailureLines


class rule_022(entity_rule):
    '''Entity rule 022 checks port names are uppercase.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '022'
        self.description = 'Uppercase port name.'

    def analyze(self, lines):
        lFailureLines = []
        fEntityFound = False
        fPortMapFound = False
        for iLineNumber, sLine in enumerate(lines):
            if fEntityFound:
                if re.match('^\s*end', sLine.lower()):
                    fEntityFound = False
                    fPortMapFound = False
                if fPortMapFound:
                    if re.match('^\s*--', sLine):
                        continue
                    if re.match('^\s*$', sLine):
                        continue
                    lLine = sLine.split()
                    if lLine[0] != lLine[0].upper():
                        lFailureLines.append(iLineNumber + 1)
                if re.match('^\s*port', sLine.lower()):
                    fPortMapFound = True
            if re.match('\s*entity', sLine.lower()):
                fEntityFound = True
        self.violations = lFailureLines


class rule_023(entity_rule):
    '''Entity rule 023 checks port names have I_, O_ or IO_ prefixes.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '023'
        self.description = 'Add proper prefix indicating port direction.'

    def analyze(self, lines):
        lFailureLines = []
        fEntityFound = False
        fPortMapFound = False
        for iLineNumber, sLine in enumerate(lines):
            if fEntityFound:
                if re.match('^\s*end', sLine.lower()):
                    fEntityFound = False
                    fPortMapFound = False
                if fPortMapFound:
                    if re.match('^\s*\w\w+\s*:\s*[in|out|inout]', sLine.lower()):
                        lLine = sLine.lower().split()
                        if not(lLine[0].startswith('i_') or lLine[0].startswith('o_') or lLine[0].startswith('io_')):
                            lFailureLines.append(iLineNumber + 1)
                if re.match('^\s*port', sLine.lower()):
                    fPortMapFound = True
            if re.match('\s*entity', sLine.lower()):
                fEntityFound = True
        self.violations = lFailureLines


class rule_024(entity_rule):
    '''Entity rule 024 checks the closing parenthesis for ports are on a line by itself and one line above the "end" keyword.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '024'
        self.description = 'Closing parenthesis must be on a line by itself and above the "end" keyword.'

    def analyze(self, lines):
        lFailureLines = []
        fEntityFound = False
        fPortMapFound = False
        for iLineNumber, sLine in enumerate(lines):
            if fEntityFound:
                if re.match('^\s*end', sLine.lower()):
                    if not re.match('^\s*\)', lines[iLineNumber - 1]):                 
                        lFailureLines.append(iLineNumber + 1)
                if re.match('^\s*port', sLine.lower()):
                    fPortMapFound = True
            if re.match('\s*entity', sLine.lower()):
                fEntityFound = True
        self.violations = lFailureLines


class rule_025(entity_rule):
    '''Entity rule 025 checks the indentation of closing parenthesis for port maps.'''

    def __init__(self):
        entity_rule.__init__(self)
        self.identifier = '025'
        self.description = 'Closing parenthesis must be on a line by itself and above the "end" keyword.'

    def analyze(self, lines):
        lFailureLines = []
        fEntityFound = False
        fPortMapFound = False
        for iLineNumber, sLine in enumerate(lines):
            if fEntityFound:
                if fPortMapFound:
                    if re.match('^\s*\)', sLine):
                        if not re.match('^\s\s\)', sLine):
                            lFailureLines.append(iLineNumber + 1)
                if re.match('^\s*port', sLine.lower()):
                    fPortMapFound = True
            if re.match('\s*entity', sLine.lower()):
                fEntityFound = True
        self.violations = lFailureLines
