Which Data Structure?!
    Lists, Dictionaries, Tuples... when to use each?
    Use Lists are for ordered sequences, and are a good default
    # 1st thing, 2ns thing, 3rd thing, 4th thing
    # default data strx, always change to something else

    Use Tuples if it is syntactically easier or you need an immutable type (e.g., a dictionary key; function parameters)
    # list that may or may not be syntactically easier
    # if need an immutable list (e.g. keys in dict)
     
    Use Dictionaries for key-value pairs
    # each piece of data associated with a label/key
    # unordered

External Data Formats:
    Comma-Separated Values (CSV): 
        Lines of values separated by commas. 
        Similar to a list (lines) of lists (values), or a list (lines) of dictionaries (key+values)
        Variant: tab-separated values (tsv)

        CSV and Python: Loop through the lines in the file, then split the values using the comma separator

        data = []
        for line in file:
            row = line.split(',')
            #further processing if necessary
            data.append(row)

        https://docs.python.org/3/library/functions.html
        enumerate:
            >>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
            >>> list(enumerate(seasons))
            [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
            >>> list(enumerate(seasons, start=1))
            [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
            
            Equivalent to:
            def enumerate(sequence, start=0):
                n = start
                for elem in sequence:
                    yield n, elem
                    n += 1

        processing a header row:
            data = []
            header = []
            for i , line in enumerate(file): #tuple w/ line num
                #i=(1st value in tuple),line=(2nd value in tuple)
                row = line.split(',') # each row type = list; 0th row = [Title, Description, Price, Calories]
                if i == 0:
                    header = row #save as header/reassign header to row. which is itself a list (if did header.append(row), would end up with list of values in a list header =[[Title, Description, Price, Calories]])
                else:
                    row_as_dict = dict(zip(header, row)) # dict makes a dictionary (built in fxn); zip is another built in fxn, takes two lists (one is keys, one is values) and merges them into a single dict (1st item in first list = key for 1st item in 2nd list); making header row items the keys for subsequent row values
                    data.append(row_as_dict) # in lecture slides, not tabbed, add header row to data, which probably dont want to do actually
            print(data)

How do we make data more descriptive? diff num of columns, headers, bunch o nums
    XML: EXtensible Markup Language
        A generalized syntax for semantically defining content (HTML with own tags!)
        Similar to a dictionary of dictionaries #e.g. key person has keys(vars) and more dicts (favorites)
        
        <person>
           <firstName>Alice</firstName>
           <lastName>Smith</lastName>
           <favorites>
              <music>jazz</music>
              <food>pizza</food>
           </favorites>
        </person>

        convert plain text to xml fairly easily
        html is a subset of xml, produces a data structue: DocumentObjectModel Tree
            top item is root/node, lower levels are leaf/nodes, branches are chunks lower down too, also parent/child
        XML and Python: 
            less pleasant :( 
            Use a package (e.g. xml.etree.ElementTree) to parse a String into a DOM tree that can be searched for relevant data (https://docs.python.org/3/library/xml.etree.elementtree.html​)

            import xml.etree.ElementTree as ET
            tree = ET.parse(file)
            root = tree.getroot()

            #iterate through all children of type 'Tag'
            for element in root.findall('Tag'):
                #get first <Child> element
                child = root.find('Child1') 
                attrib = child.get('attrib_name') #get attribute
                text = child.text #get content text
                #etc...

    JSON: JavaScript Object Notation
        {
          "first_name": "Alice",
          "last_name": "Smith",
          "age": 22,
          "pets": ["rover", "fluffy", "mittens"],
          "favorites": {
            "music": "jazz",
            "food": "pizza",
            "numbers": [12, 42] 
          }
        }
        Python syntax vs. JSON(above):
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

        JSON values can only be Strings, numbers, booleans (true or false), arrays (lists), or objects (dicts)
        JSON keys can only be Strings (in double-quotes)
        JSON is more strict about trailing commas, etc.

        JSON and Python: Use the json package to convert JSON into a Python dictionary and enjoy!
            https://docs.python.org/3/library/json.html​
            
            import json

            #convert json string to dictionary
            data = json.loads(json_string)

            #convert to json string
            my_json = json.dumps({'a':1, 'b':2}) 

Downloading Data
    Web APIs: Many web services and data sources allow you to use HTTP (web) requests to access their data!
    E.g., GitHub! 
        (https://developer.github.com/v3/)
        https://api.github.com/users/infx598g-s16/repos # list of jsons
        https://api.github.com/users/your-github-name/repos # get that same data file for whatever username (public stuff only)
    
    # command-line downloading
    curl https://api.github.com/users/infx598g-s16/repos

    # authenticate
    curl -u username https://api.github.com/repos/infx598g-s16/charter

    # include headers
    curl -i https://api.github.com/users/infx598g-s16/repos

    An Application Programming Interface. The interface we can use to interact with an application through programming.
        The point at which two components meet and communicate.
        An Interface: 
            def my_function(param1, param2):
                """A function that does something
                   param1 is X and should be type A
                   param2 is Y and should be type B
                """
                #....the thing above is a "docstring"
            docstring: A string (in multiline triple-quotes) explaining and "documenting" the interface/usage of a function
            def say_hello(name):
                """Prints a greeting.
                   name (str): a person to greet
                """
                print("Hello "+name)

            say_hello("y'all")
API URIs
A web services URI has two parts:
    The Base URI
    http://api.github.com
     
    An EndPoint
    /users/:username/repos
    /repos/:owner/:repo
    /search/repositories
    /emojis

HTTP requests include a target resource and a verb (method) specifying what to do with it
    GET Return a representation of the current state of the resource (like SELECT)
    POST    Add a new subresource (e.g., insert a record) (like INSERT)
    PUT Update the resource to have a new state (like UPDATE)
    PATCH   Update a portion of the resources state
    DELETE  Remove the resource (like DELETE)

    GET /api/v1/users - Get all users records the current user is allowed to see, returned as a JSON array of objects
    GET /api/v1/users/me - Get the current users record, returned as a single JSON object
    POST /api/v1/users - Create a new user, using the JSON in the request body as the state of the new user
    PATCH /api/v1/users/me  - Update the current user record using the properties and values in the request body
    DELETE /api/v1/users/1234 - Delete the user record identified by the primary key 1234

REST Architecture: REpresentational State Transfer
    Treat all data as a resource with a unique identifier (URI), and use typed HTTP requests to interact with those data.
     
    A web system is "RESTful" if it conforms to this pattern.

HTTP Requests with Python: We can use the urllib module to send requests to web servers and download data from the web.
    import urllib.request, urllib.parse, urllib.error
    import json

    response = urllib.request.urlopen(web_url) #send request

    #print the contents
    for line in response:
        print(line)

    #convert to json
    data = response.read().decode() # whole page as string
    data = json.loads(data) # string to dict
    print(json.dumps(data, sort_keys=True, indent=3)) #pretty-print json

Third-Party Modules: We can download additional Python modules to get even more pre-written functions (yay abstraction!)
    For example, the Requests package:
    import requests

    r = requests.get(web_url)

    data = r.json() #fetch json as dict
    print(data)

PIP
We can use the included pip package manager to easily download and install modules.
# command-line
pip3 install module_name
See https://pip.pypa.io/en/stable/