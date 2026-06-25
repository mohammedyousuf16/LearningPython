import re
text= 'the quick brown fox jumps over the lazy dog.'

# Find the first occurance of the word
# match= re.search('brown', text)
# if match:
#     print('match found')
#     print('start index:', match.start())
#     print('end index:', match.end())

# Find the all occurance of the word
# matchs = re.findall('the', text, re.IGNORECASE)
# print('Matches', matchs)

# Replace all occurance of the word
new_text = re.sub('fox', 'cat', text)
print(new_text)