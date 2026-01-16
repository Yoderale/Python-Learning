glossary = {
    'immutable': 'This means a variable cannot be changed.',
    'tuple': 'Used to store multiple items in a single variable.',
    'loop': 'Allows a block of code to be executed repeatedly until a certain condition is met.',
    'if-elif-else': 'essentially a CASE WHEN statement.',
    'list': 'A way to store define a variable with multiple values.',
    'set': 'A set is a collection in which each item must be unique',
    'PEP8': 'Python Enhancement Proposal v8',
    '.values()': 'Dictionary method to pulls each value from the dictionary',
    '.keys()': 'Dictionary method to pull each key from a dictionary'
}
for word in glossary.keys():
    print(f'{word.title()}: {glossary[word]}')