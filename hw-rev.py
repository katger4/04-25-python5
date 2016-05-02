data = [
{
    'list':[1,2,3],
    'dict': {'a':'aardvark','b':'banana'},
    'hashtags':[
    {"indices":[32,36],"text":"lol"},
    {"indices":[32,36],"text":"bloop"}
    ]
},
{
    'list':[10,20,30],
    'dict': {'a':'apple','b':'breakfast'},
    'hashtags':[
    {"indices":[32,36],"text":"lol"}
    ]
},
{
    'list':[100,200,300],
    'dict': {'a':'avocado','b':'bacon'},
    'hashtags':[
    {"indices":[32,36],"text":"lol"}
    ]  
}
]

# all_tags = [] # if put out here then gets all tags all over the place
tweets = []
for i in data:
    tweet = {}
    all_tags = []
    hashtags = i['hashtags'] # each ht is a list
    for i in hashtags: # {"indices":[32,36],"text":"lol"}
        the_tag = i['text'] #lol
        all_tags.append(the_tag)
    tweet['hashtags'] = all_tags
    tweets.append(tweet)
print(tweets)
        
# print(data)

# goal: list of b-words
bwords = []
all_numbers = [] # ALL the numbers in the dataset

for i in data: # i looks like {...}
    word_dict = i['dict'] # looks like {'a':'aardvark','b':'banana'}
    word = word_dict['b'] #example: 'banana'
    bwords.append(word)

    numbers = i['list'] # 'list':[1,2,3]
    for i in numbers:
        all_numbers.append(i)


print(bwords)
print(all_numbers)