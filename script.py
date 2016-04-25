# taking in a list, therefore use "cards" not "card"
# def is_flush(cards):
#     words = cards[0].split(' ')
#     suit = words[2] # suit of the first guy
#     # split takes a string like '2 of hearts' and splits it into different words
#     # words is a new list, words[2] is suit
#     for card in cards:
#         print("Looking at "+card)
#         if not card.endswith(suit):
#             return False
#     return True

# result = is_flush(['5 of Clubs', '9 of Clubs', '8 of Clubs', 'Jack of Clubs', '2 of Clubs'])
# print(result)

# result2 = is_flush(['2 of Clubs', '9 of Clubs', '8 of Clubs', 'Jack of Spades', '2 of Clubs'])
# print(result2)
# work backwards from idea of algorithm to build

# text = input("Enter some text: ")

# #number of letters
# letter_counts = {}


# for letter in text:
#     # letter_counts[letter] += 1
#     if letter not in letter_counts: #check if has key
#         letter_counts[letter] = 1
#     else:
#         letter_counts[letter] += 1
# print(letter_counts)


# text = input("Enter some text: ")

# #number of letters
# ltr_counts = {}


# for ltr in text:
#     ltr_counts[ltr] = ltr_counts.get(ltr, 0) + 1
# print(ltr_counts)

import re #for regex
file = open('sonnet_v.txt')

word_counts = {}
for line in file:
    # split on regex (not word or ' chars)
    words = re.split("[^\w']+", line)
    for word in words:
        if word != '':
            word_counts[word] = word_counts.get(word,0) + 1

count_words = {} #reverse dictionary for fast lookup
for word, count in word_counts.items():
    count_words[count] = count_words.get(count,[]) #initialize
    count_words[count].append(word)

counts = list(count_words.keys())
counts.sort(reverse=True)

for x in range(min(50,len(counts))): #go up to 50 words
    print(counts[x], ":" ,count_words[counts[x]])