import random

def testPatterns():
    print(matchWildcard('stop', ['stop']))
    print(matchWildcard('stop', ['stop', 'now']))
    print(matchWildcard('stop', ['I', 'stop', 'now']))
    print(matchWildcard('stop', ['I', 'can', 'stop']))
    print(matchWildcard('stop', ['I', 'can', 'stop', 'now']))
    print(matchWildcard('stop', ['I', 'can', 'finish', 'now']))
    print(matchWildcard([0,'stop', 0], ['stop']))
    print(matchWildcard([0,'stop', 0], ['stop', 'now']))
    print(matchWildcard([0,'stop', 0], ['I', 'stop', 'now']))
    print(matchWildcard([0,'stop', 0], ['I', 'can', 'stop']))
    print(matchWildcard([0,'stop', 0], ['I', 'stop', 'right', 'now']))
    print(matchWildcard([0,'stop', 0], ['I', 'can', 'finish', 'now']))

def matchWildcard(term, text, soFar=''):
    if len(text) == 0:
        return False, '', []
    if (isinstance(term, str) and text[0] == term) or\
            (not isinstance(term,str) and text[0] in term):
        return True, soFar, text
    return matchWildcard(term, text[1:], soFar + ' ' + text[0])

def matchPattern(pattern, text):
    matches = []
    for i in range(len(pattern)):
        if pattern[i] == 0:
            if i + 1 == len(pattern):
                matches.append(''.join(text))
            else:
                success, match, text = \
                    matchWildcard(pattern[i +1], text)
                if not success:
                    return False, []
                else:
                    matches.append(match.strip())
        elif len(text) == 0:
            return False, []
        elif not isinstance(pattern[i], str):
            if text[0] in pattern[i]:
                matches.append(text[0])
                text = text[1:]
            else:
                return False, []
        elif pattern[i] == text[0]:
            matches.append(text[0])
            text = text[1:]
        else:
            return False, []
        return True, matches

def splitClauses(text):
    return map(lambda x: x.strip(' '),
        text.lower().replace(',', '.').replace("'", '').split('.'))

def splitWords(text):
    return text.split(' ')

conversions = { 'i':'you', 'you':'i',
		'am':'are', 'are':'am', 
		'my':'your', 'your':'my', 
		'myself':'yourself', 'yourself':'myself'}

def transform(text):
    return map(lambda x: \
        conversions[x] if x in conversions else x, text)

while True:
    text = input('? ')
    if len(text) == 0:
        break

    # Process input inside the loop
    for clause in splitClauses(text):
        print(splitWords(clause))

#matchPattern( )

testPatterns( )