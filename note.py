Practice Problem (Pairs!)
Define a function is_flush() that takes in a single parameter: a list of strings representing playing cards (e.g., "Ace of Spades", "2 of Hearts"). The method should return whether or not all of the cards are of the same suit (Clubs, Diamonds, Hearts, or Spades).
Hint: use the String method endswith()

my try:
    # Test Cases:

    # is_flush(['5 of Clubs', '9 of Clubs', '8 of Clubs', 'Jack of Clubs', '2 of Clubs'])
    # #=> True

    # is_flush(['2 of Clubs', '9 of Clubs', '8 of Clubs', 'Jack of Spades', '2 of Clubs'])
    # #=> False

    # is_flush(['2 of Hearts', '9 of Clubs', '8 of Clubs', '2 of Spades', '2 of Clubs'])
    # #=> False
    import re

    cards =['5 of Clubs', '9 of Clubs', '8 of Clubs', 'Jack of Clubs', '2 of Clubs']

    def is_flush(card):
        if card.endswith('\w{4}'):
            print(True)
        else:
            print(False)

    for card in cards:
        is_flush(card)

class:
    # taking in a list, therefore use "cards"
    def is_flush(cards):
        words = cards[0].split(' ')
        suit = words[2] # suit of the first guy
        # split takes a string like '2 of hearts' and splits it into different words
        # words is a new list, words[2] is suit
        for card in cards:
            print("Looking at "+card)
            if not card.endswith(suit):
                return False
        return True

    result = is_flush(['5 of Clubs', '9 of Clubs', '8 of Clubs', 'Jack of Clubs', '2 of Clubs'])
    print(result)

    result2 = is_flush(['2 of Clubs', '9 of Clubs', '8 of Clubs', 'Jack of Spades', '2 of Clubs'])
    print(result2)

    result3 = is_flush(['2 of Hearts', '9 of Clubs', '8 of Clubs', '2 of Spades', '2 of Clubs'])
    print(result3)
    # work backwards from idea of algorithm to build

# major data structure
Dictionaries: A unordered set of "key & value" pairs.
    Similar to a real world dictionary: you have the word (the key) and the definition (the value). Use the key to look up the value.
    Provides a mapping from keys to values
    https://docs.python.org/3/tutorial/datastructures.html#dictionaries
        if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. 
        You can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments, or methods like append() and extend().
        It is best to think of a dictionary as an unordered set of key: value pairs, with the requirement that the keys are unique (within one dictionary). (keys must be a singular entity, not a list)
        The main operations on a dictionary are storing a value with some key and extracting the value given the key. 
        Performing list(d.keys()) on a dictionary returns a list of all the keys used in the dictionary, in arbitrary order (if you want it sorted, just use sorted(d.keys()) instead). [2] To check whether a single key is in the dictionary, use the in keyword.

    ages = {'alice':42, 'bob':35, 'charles':13}
    extensions = {'joel':1622, 'ischool':9937}
    num_words = {1:'one', 2:'two', 3:'three'}
    things = {'num':12, 'dog':'woof', 'list':[1,2,3]}
    empty = {}

Accessing Dicts: We access individual values in a dict using square brackets (specify the key as the "room number")
    ages = {'alice':42, 'bob':35, 'charles':13}

    print(ages['alice']) # => 42
    print(ages['bob']) # => 35 <--"lookups"
    print(ages['charles']) # => 13

    print(names[42]) # => KeyError!
    print(names['fred']) # => KeyError!

    #get() function returns value OR default
    names.get('alice', 0) # => 42, the value
    names.get('fred', 0) # => 0, the default

To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
# to indent in cmd line, use 1 space (not tab!)
    >>> questions = ['name', 'quest', 'favorite color']
    >>> answers = ['lancelot', 'the holy grail', 'blue']
    >>> for q, a in zip(questions, answers):
    ...     print('What is your {0}?  It is {1}.'.format(q, a))
    ...
    What is your name?  It is lancelot.
    What is your quest?  It is the holy grail.
    What is your favorite color?  It is blue.

Changing Dicts: The dict[key] itself is a variable. Assigning a value to a new key will add that key to the dictionary.
    dicts are unordered!

    d = {'a':1, 'b':2, 'c':3}

    d['a'] = 5
    print(d) #=> {'c': 3, 'a': 5, 'b': 2}

    d['x'] = 12 #assigns value to NEW key
    print(d) #=> {'c': 3, 'x': 12, 'a': 5, 'b': 2}

# why do we care about dicts? maybe we care about how many letters are in a particular string
How many of each letter?
    text = "Mississippi"

    #number of letters
    a = 0
    b = 0
    c = 0
    #...
# simplistic approach...loop thru whole alphabet, count letters in text, would produce many errors, need 26 vars (not including case, different languages, etc)
    for letter in text:
        if letter == 'a':
            a += 1 #shortcut for a = a + 1
        if letter == 'b':
            b += 1
        #...

dictionaries solve this issue! use variables inside a dictionary

    text = input("Enter some text: ")

    #number of letters
    letter_counts = {}


    for letter in text:
        # letter_counts[letter] += 1
        if letter not in letter_counts: #check if has key
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1
    # creates a dict of each letter/count value

other method:
    text = input("Enter some text: ")

    #number of letters
    ltr_counts = {}


    for ltr in text:
        ltr_counts[ltr] = ltr_counts.get(ltr, 0) + 1

Dicts and Loops: We can use a for loop to go through the keys in a dictionary.
    d = {'a':1, 'b':2, 'c':3}

    for key in d:
        print(d[key])

    ages = {'alice':42, 'bob':35, 'charles':13}

    for person in ages:
        print(person, 'is', ages[person])

Methods can get lists of a dictionarys keys, values, or items for looping:
    d = {'a':1, 'b':2, 'c':3}

    keys = list(d.keys()) #get keys as a list
    keys.sort() #sort the keys bc now a list
    for key in keys: #loop in order
        print(key, "maps to", d[key]) #print the values

    for value in d.values(): #loop just the values
        print(value)

    for key, value in d.items(): #list of tuples! going thru 2 values at once (both key and value for all items in dict). items is the method thats going to get a list of key-value pairs
        print(key, 'maps to', value)

    for letter, number in d.items(): #list of tuples!
        print(letter, 'maps to', number)

Reverse Lookup: Access value by key is fast and easy. Access key by value requires searching.

    ages = {'alice':42, 'bob':35, 'charles':13}

    #how old is Alice?
    print("Alice is", ages['alice']) # <--lookup

    #who is 35?
    persons35 = []
    for person in ages:
        if ages[person] == 35:
            persons35.append(person)

    print(persons35, "are 35")

Nested Dictionaries: Values of dictionaries can themselves be lists or dictionaries!
    person = {
      'first_name': 'Alice',
      'last_name': 'Smith',
      'age': 22,
      'pets': ['rover', 'fluffy', 'mittens'],
      'favorites': {
        'music': 'jazz',
        'food': 'pizza',
        'numbers': [12, 42] 
      }
    }

    name = person['first_name']     #get value of 'first_name' key
    person['last_name'] = 'Jones'   #set value of 'last_name' key
    print(person['first_name'], person['last_name'] #=> "Alice Jones"

    fav_food = person['favorites']['food']; #object in the object
                   #object         #value

    first_number = person['favorite']['numbers'][0]; # 12
    # favorites_dict = person['favorites']
    # fav_nums = favorites_dict['numbers']
    # fav_nums[0]

    person['favorite']['numbers'].append(7); #add 7 to end of the list

Dictionary Example: What are the most common words used in a file?
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

Tuples: An immutable, ordered sequence of values. (comma-separated, often in parentheses) # same as list, but cannot be changed
    letters = 'a', 'b', 'c'
    print(letters) #=> ('a', 'b', 'c')
    # in practice always put in (parentheses) bc makes very clear, but will work sort of if not
    letters = ('a', 'b', 'c')
    print(letters) #=> ('a', 'b', 'c')

    values = ('a', 1, True, [5,6])

    triple = (1,2,3)
    double = (4,5)
    single = (6,) #extra comma so is a tuple! comma makes tuple, not parens
    empty = ()

Accessing Tuples: Access a single variable from a Tuple using square brackets and an index (like with a list). Tuples cannot be modified!

    triple = ('a', 'b', 'c')
    print(triple[0]) #=> 'a'
    print(triple[1:3]) #=> ('b','c')

    triple[0] = 'z' #=> Error! cannot be modified

Comparing Tuples: Relational (comparison) operators start on the first element, then go on to the next in case of a "tie".
    t = (1,2,3)
    u = (2,2,3)
    v = (1,2,1000)

    t < u #=> True bc 1<1
    t < v #=> True bc 1=1, 2=2, but 3<1000
    v < u #=> True bc 1<2

Tuple Assignment: A comma-separate listing of values can be assigned to a tuple (packing). A tuple can be assigned to a comma-separated listing of variables (unpacking).

    triple = 1, 2, 3 #values to tuple (packing)
    print(triple) #=> (1, 2, 3)

    x, y, z = (1,2,3) #tuple to variables (unpacking)
    print(x) #=> 1
    print(y) #=> 2
    print(z) #=> 3

    a, b, c = x, y, z #quick multi-variable assignment!
    #=> a=x; b=y, c=z

    a, b = b, a #swap values!

Tuples and Dicts: The .items() method for a dictionary returns a list of tuples
    for a_tuple in d.items():
        print(a_tuple[0], 'maps to', a_tuple[1])
    
    # refer to it like a tuple
    for (key, value) in d.items():
        print(key, 'maps to', value)
    
    # refer to it like a tuple, w/o parens
    for key, value in d.items():
        print(key, 'maps to', value)

Which Data Structure?!
    Lists, Dictionaries, Tuples... when to use each?
        Use Lists are for ordered sequences, and are a good default
         
        Use Tuples if it is syntactically easier or you need an immutable type (e.g., a dictionary key; function parameters)
     
        Use Dictionaries for key-value pairs