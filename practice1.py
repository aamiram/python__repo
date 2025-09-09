letter = '''Dear <|name|>,
you are selected!
<|Date|>'''

print(letter.replace("<|name|>","Harry").replace("<|Date|>","13 Sep"))



# print(letter.replace("<|name|>","Harry")    * this will be wrong the upper one is write only
# print(letter.replace("<|date|>","13 sep")   