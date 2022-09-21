
class person:
   """
   person: Class for storing and printing person data.

           - __name   : Stores person name.
           - __age    : Stores age of the person.
           - __address: Stored the address of the person.
   """

   def __init__(self, name, age, address):
      """
      __init__: Constructor, initiating a new person object.

                - name   : Name of the new person.
                - age    : Age of the new person.
                - address: Home address of the new person.
      """
      self.__name = name 
      self.__age = age
      self.__address = address
      return

   def __del__(self):
      """
      __del__: Destructor, sets all instance variables of the person object
               to None before deletion.
      """
      self.__name = None
      self.__age = None
      self.__address = None
      return

   def name(self):
      """
      name: Returns the name of the person.
      """
      return self.__name

   def age(self):
      """
      age: Returns the age of the person.
      """
      return self.__age

   def address(self): 
      """
      address: Returns the home address of the person.
      """
      return self.__address

   def print(self):
      """
      print: Prints person data into the terminal.
      """
      print("--------------------------------------------------------------------------------")
      print("Name: " + str(self.__name))
      print("Age: " + str(self.__age))
      print("Address: " + str(self.__address))
      print("--------------------------------------------------------------------------------\n")
      return

class person_list:
   """
   person_list: Class for storing person data in a list.

                - __data: Dynamic list storing person data.
   """

   def __init__(self):
      """
      __init__: Constructs an empty person list.
      """
      self.__data = []
      return

   def __del__(self):
      """
      __del__: Emptying the person list before deletion.
      """
      self.__data.clear()
      self.__data = None
      return

   def data(self):
      """
      data: Returns a reference to the person list.
      """
      return self.__data

   def size(self):
      """
      size: Returns the number of elements in the person list.
      """
      return len(self.__data)

   def clear(self):
      """
      clear: Clears the person list.
      """
      self.__data.clear()
      return

   def push(self, new_person):
      """
      push: Adds new person data at the back of the person list.

            - new_person: Person object containing new person data to be added.
      """
      self.__data.append(new_person)
      return

   def pop(self):
      """
      pop: Removes an element containing person data at the end of the person list.
      """
      self.__data.pop()
      return

   def add(self, num_persons):
      """
      add: Adds person data for specfied number of persons. The person data
           is entered from the terminal and pushed onto the back of the list.

           - num_persons: The number of person objects to be added.
      """
      for i in range(num_persons):
         print("Enter name:")
         name = get_line()

         print("Enter age:")
         age = get_integer()

         print("Enter address:")
         address = get_line()
         
         p1 = person(name, age, address)
         self.push(p1)
      return

   def print(self):
      """
      print: Prints person data stored in the list.
      """
      for i in self.__data:
         i.print() 
      return 

def get_line():
   """
   get_line: Returns text entered from the terminal.
   """
   s = input()
   print()
   return s

def get_integer():
   """
   get_integer: Returns an integer from the terminal. Input is read from the terminal
                until a valid integer is entered.
   """
   while True:
      s = get_line()
      try:
         return int(s)
      except ValueError:
         print("Invalid input, try again!\n")

