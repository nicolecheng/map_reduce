book = open("makeyourownhats.txt", 'r')
text = book.read()
book.close()

def wc(word):
    return len(filter(lambda a: a.lower() == word, text.split()))

def wcs(wordlist):
    return map(lambda word: wc(word), wordlist)

print wc("hats")
print wcs(["hats", "hat", "dog", "girl", "banana", "nicole", "daniel"])
print max(wcs(text.split()))
