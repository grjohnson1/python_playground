import random


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
