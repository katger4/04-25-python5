How could we represent a Rectangle in a program?
    Individual variables:
        rect_x = 10
        rect_y = 20
        rect_width = 50
        rect_height = 60

    A list, tuple, or dictionary:
        rect = (10, 20, 50, 60)
        rect = {'x':10, 'y':20, 'width':50, 'height':60}

    Create a new "type" to store this data!
        rect = Rectangle(10,20,50,60)

Parts of a Computer Program:
    Data:
        name = "Alice"
        age = 22
        food = "waffles"
    Functions/Behaviors:
        def say_hello()
            print("Hello!")

Procedural Programming (keep data & fxns separated): 
  # Data
  tweets = [{...}]

  # Functions
  def includes_dog(tweets):
      #return tweets with 'dog'

  def remove_cat(tweets):
      #return tweets without 'cat'

  def sort_by_date(tweets):
      #return tweets in order

  # Program
  tweets = includes_dog(tweets)
  tweets = remove_cat(tweets)
  tweets = sort_by_date(tweets)

Object Oriented Programming: Object: a set of data AND functionality associated with that data
  Object - attributes(assoc data) - methods(assoc fxns)

  Example: Turtles - Object keeps track of state and lets us easily think about functions to call!
    # create a new Turtle object
    my_turtle = turtle.Turtle()

    # change the turtle's state
    my_turtle.color("purple")
    my_turtle.pendown()

    # tell that object to move!
    my_turtle.forward(100)
    my_turtle.left(12)
    my_turtle.forward(80)

Classes: 
  We define new types for objects by creating Classes (classifications).
  A class is a template, recipe, or blueprint for individual objects. It defines what data and behaviors (functions) they have.
  An object is an "instance of" (example of) a class. We instantiate an object from a class.
  !!! Name classes starting with Capital Letter! (CamelCase) !!!
    rectangle is a variable
    rectangle() is a fxn
    Rectangle is a class

  # declare the class
  class Rectangle:
    """Represents a rectangle
       attributes: x, y, width, height       
    """

  # instantiate an object
  my_rect = Rectangle()
  type(my_rect) #=> <class '__main__.Rectangle'>

  your_rect = Rectangle() # is a separate instance of the rect

  We instantiate an object from a class! (an object is an instance of a class)

Attributes: 
  The data representing the state of a particular object. E.g., the variables belonging to that object.
  Also known as instance variables, member variables, or fields.

  # declare the class
  class Person:
    """Represents a Person on Twitter
       attributes: first_name, last_name, age, twitter_handle
    """

  We access attributes using dot notation.

  class Person:
    """Represents a Person on Twitter
       attributes: first_name, last_name, age, twitter_handle
    """

  alice = Person() #instantiate the object

  #assign values to attributes
  alice.first_name = "Alice"
  alice.last_name = "Smith"
  alice.age = 22
  alice.pets = ["fido", "rover"] #can be any type

  #access attributes
  print(alice.first_name) #=> "Alice"
  print(alice.last_name) #=> "Smith"
  print(alice.pets[1]) #=> "rover"

Functions: We can pass objects into functions like any other value.
  def full_name(person):
      """returns full name of given person"""
      return person.first_name + " " + person.last_name

  def say_hello(person, name):
      """Has the given Person (object) say hello to the name (string)"""
      print(person.first_name + ' says "Hello' + name + '!"') 


  alice = Person() #instantiate the object
  alice.first_name = "Alice"
  alice.last_name = "Smith"

  print( full_name(alice) ) #=> "Alice Smith"

  say_hello(alice, "Bob") #=> 'Alice says "Hello Bob!"'

  each object keeps track of its own attributes

Methods
  Functions can be defined inside classes. These are referred to as methods. 
  Call them on the class with dot notation.

Methods
  Functions can be defined inside classes (they are indented now). These are referred to as methods. 
  Call them on the class with dot notation.
  
  class Person:
      """Represents a person with first_name & last_name"""

      def full_name(person):
          return person.first_name + " " + person.last_name

      def say_hello(person, name):
          print(person.first_name + ' says "Hello' + name + '!"') 

  alice = Person() #instantiate the object
  alice.first_name = "Alice"
  alice.last_name = "Smith"

  print( Person.full_name(alice) ) #=> "Alice Smith"

  Person.say_hello(alice, "Bob") #=> 'Alice says "Hello Bob!"'

We can also call the method on the object. The first parameter becomes the "subject" (e.g., the object).
  class Person:
      """Represents a person with first_name & last_name"""

      def full_name(person):
          return person.first_name + " " + person.last_name

      def say_hello(person, name):
          print(person.first_name + ' says "Hello' + name + '!"') 

  alice = Person() #instantiate the object
  alice.first_name = "Alice"
  alice.last_name = "Smith"

  print( alice.full_name() ) #=> "Alice Smith"

  alice.say_hello("Bob") #=> 'Alice says "Hello Bob!"'

The object the method is called on is assigned to the first param (the "subject")
  class Person:
      def full_name(person):
          return person.first + " " + person.last

  alice = Person()

  print( alice.full_name() ) # person=alice (in fxn) is implicit; don't need first param (already specified)

  class Person:
    def say_hello(person, name):
        print(person.first + ' says Hi ' + name)

  alice = Person()

  alice.say_hello("Bob") #person=alice (in fxn) is implicit; don't need first param (already specified)

!!By convention, that first "subject" parameter is named self.!! #is JS self=this

  class Person:
    """Represents a person with first_name & last_name"""

    def full_name(self):
        return self.first_name + " " + self.last_name

    def say_hello(self, name):
        print(self.first_name + ' says "Hello' + name + '!"') 

  alice = Person() #instantiate the object
  alice.first_name = "Alice"
  alice.last_name = "Smith"

  print( alice.full_name() ) #=> "Alice Smith"

  alice.say_hello("Bob") #=> 'Alice says "Hello Bob!"'

Why use a Class? Why not use a dictionary instead?
  Use a dictionary (or list or tuple) if you just need to organize data.
    This is usual in data science/visualization
   
  Use a class if you also want to give that data behaviors (i.e., functions)
    This is usual in using external modules

alice = Person() # instantiates an object; calling a function (bc ()); what function are we calling??

__init__
  When an object is instantiated, Python calls a method named __init__ to initialize the object.
  
    class Person:
        def __init__(self):
            print("Instantiating a new Person")


    alice = Person() # like a shortcut for Person.__init__()
    #=> prints "Instantiating a new Person")

  We pass the __init__ method parameters to assign to the attributes.

    class Person:
        def __init__(self, first_name, last_name, age=18): # age=18 is an optional param
            self.first_name = first_name #assign params to attribs
            self.last_name = last_name
            self.age = age

    alice = Person("Alice", "Jones", 22)
    print( alice.first_name ) #=> "Alice"
    print( alice.age ) #=> 22

    bob = Person("Bob", "Brown") #no age specified, use default
    print( bob.first_name ) #=> "Bob"
    print( bob.age ) #=> 18

Optional Parameters: Parameters can be assigned default values in the function declaration. If unspecified, the default value is used.

__str__
When an object is cast to a string, (e.g., with str()), Python calls a method named __str__ to stringify the object.