result = []
for x in range(5):
    result.append(x ** 2)

{char: ord(char) for char in "abc"}
{'a': 97, 'b': 98, 'c': 99}

''.join(char for char in "Hello UK" if char.islower())
'ello'