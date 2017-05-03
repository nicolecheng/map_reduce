book = open("makeyourownhats.txt", 'r')
text = book.read().split()
book.close()

def memoize(f):
    vals = {}
    def inner(*args):
        if args[0] not in vals:
            vals[args[0]] = f(*args)
        return vals[args[0]]
    return inner

#Memoizing this makes it like 10x faster since pre-counted words are saved
@memoize
def wc(word):
    return len(filter(lambda a: a.lower() == word, text))

def wcs(wordlist):
    return map(lambda word: wc(word), wordlist)

print "hats: " + str(wc("hats"))
print

words_to_count = ["hats", "hat", "dog", "girl", "banana", "nicole", "daniel"]
print words_to_count
print wcs(words_to_count)
print

#Alternatively something could have been done with wcs(text) but it doesn't look as clean.
word = reduce( lambda a, b: a if wc(a) >= wc(b) else b, text )
print 'Most common word is "' + word + '"' + ", with a count of " + str(wc(word))

