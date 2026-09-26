phrase = "catsanddog"

words = ["cat", "and", "dog"]

for word in words:
    if word in phrase:
        phrase = phrase.replace(word,"")

if len(phrase) > 0:
    print (False)
else:
    print(True)

print(phrase)