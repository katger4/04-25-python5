# class Person:
#   """Represents a Person on Twitter
#      attributes: first_name, last_name, age, twitter_handle
#   """

# alice = Person() #instantiate the object

# #assign values to attributes
# alice.first_name = "Alice"
# alice.last_name = "Smith"
# alice.age = 22
# alice.pets = ["fido", "rover"] #can be any type

# #access attributes
# print(alice.first_name) #=> "Alice"
# print(alice.last_name) #=> "Smith"
# print(alice.pets[1]) #=> "rover"

# bob = Person()
# bob.first_name = "Bob"
# bob.last_name = "Jones"
class Person: # declare the class
  """Represents a Person with first_name, last_name, and age"""

  def full_name(self):
      return self.first_name + " " + self.last_name
  
  def have_birthday(self):
      self.age = self.age + 1
  
  def is_older_than(self, other):
      """returns whether object is older than other Person"""
      return self.age > other.age #access other's instance variable

  def greet(self, Person):
      """Prints a greeting to the other Person"""
      print(self.full_name() + ' says "Hi ' + Person.full_name()+'!"')

alice = Person(); alice.first_name = "Alice"; alice.last_name = "Smith"
bob = Person(); bob.first_name = "Bob"; bob.last_name = "Brown"

alice.age = 22
alice.have_birthday()
print(alice.age) #=> 23

bob.age = 18
print( alice.is_older_than(bob) ) #=> True

alice.greet(bob) #=> 'Alice Smith says "Hi Bob Brown!"'