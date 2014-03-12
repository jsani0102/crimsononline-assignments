from pprint import pprint # pretty print output formatting
from question1 import (common_words, common_words_min, common_words_tuple,
    common_words_safe)
# fill in the rest!
from question2 import (Article, Picture)

print "==testing question 1=="
print "common_words... ",
pprint(common_words("words.txt"))

print "common_words_min 2... ",
pprint(common_words_min("words.txt", 2))

print "common_words_min 5... ",
pprint(common_words_min("words.txt", 5))

print "common_words_min 9... ",
pprint(common_words_min("words.txt", 9))

print "common_words_tuple w/ min 5... ",
pprint(common_words_tuple("words.txt", 5))

print "common_words_safe... ",
pprint(common_words_safe("words_fail.txt", 5))

print "==testing question 2=="
article = Article("Jayant Sani joins the Crimson tech comp!", "Jayant Sani is currently working on assignment 1 of the Crimson tech comp", "Jayant Sani")
article.show()
article.save()