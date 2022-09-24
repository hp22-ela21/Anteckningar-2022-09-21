################################################################################
# electrical.py: Contains functionality for storing and calculating electrical 
#                quantities voltage, current, resistance and power, both as
#                single entities and storage in a dynamic list.
################################################################################
class electrical:
   """
   electrical: Class for computing and storing electrical quantities.

               __voltage   : Voltage measured in V.
               __current   : Current measured in mA.
               __resistance: Resistance measured in kOhm.
               __power     : Power measured in mW.
   """

   def __init__(self):
      """
      __init__: Initiating new object for storing electrical quantities.
      """
      self.__voltage = 0.0
      self.__current = 0.0
      self.__resistance = 0.0
      self.__power = 0.0
      return

   def __del__(self):
      """
      __del__: Setting electrical quantities to None before object deletion.
      """
      self.__voltage = None
      self.__current = None
      self.__resistance = None
      self.__power = 0.0
      return

   def voltage(self):
      """
      voltage: Returns voltage measured in V.
      """
      return self.__voltage

   def current(self):
      """
      current: Returns current measured in mA.
      """
      return self.__current

   def resistance(self):
      """
      resistance: Returns resistance measured in kOhm.
      """
      return self.__resistance

   def power(self):
      """
      power: Returns power measured in mW.
      """
      return self.__power

   def set(self, voltage, current):
      """
      set: Sets new values of electrical quantities by calculation with specified
           voltage and current values.

           - voltage: New voltage measured in V.
           - current: New current measured in mA.
      """
      self.__voltage = voltage
      self.__current = current
      self.__power = voltage * current

      if current != 0:
         self.__resistance = voltage / current
      else:
         self.__resistance = None

      return

   def read(self):
      """
      read: Reads and stored new voltage and current values from the terminal and calculates 
            corresponding resistance and power.
      """
      print("Enter voltage in V:")
      voltage = read_float()
      print("Enter current in mA:")
      current = read_float()
      self.set(voltage, current) 
      return

   def print(self):
      """
      print: Prints stored electrical quantities in the terminal.
      """
      print("--------------------------------------------------------------------------------")
      print("Voltage: " + str(self.__voltage) + " V")
      print("Current: " + str(self.__current) + " mA")
      print("Resistance: " + str(self.__resistance) + " kOhm")
      print("Power: " + str(self.__power) + " mW")
      print("--------------------------------------------------------------------------------\n")
      return

class electrical_list:
   """
   electrical_list: Class for storing objects containing electrical quantities in a list.

                    - __data: Dynamic list containing electrical quantities.
   """

   def __init__(self):
      """
      __init__: Initiating new empty list for storing electrical quantities.
      """
      self.__data = []
      return

   def __del__(self):
      """
      __del__: Emptying list containing electrical quantities before object deletion.
      """
      self.__data.clear()
      self.__data = None
      return

   def data(self):
      """
      data: Returns a reference to the dynamic list containing electrical quantities.
      """
      return self.__data 

   def size(self):
      """
      size: Returns the size of the list, i.e. the number of objects containing 
            electrical quantities stored in the list.
      """
      return len(self.__data)

   def is_empty(self):
      """
      is_empty: Indicated if the list containing electrical quantities is empty.
      """
      if self.size() == 0:
         return True
      else:
         return False

   def push(self, new_electrical):
      """
      push: Adds a new object containing electrical quantities to the back of the dynamic list.

            - new_electrical: The new object containing electrical quantities to be added.
      """
      self.__data.append(new_electrical) 
      return

   def add(self, num_elements):
      """
      add: Adds specified amount of new objects containing electrical quantities to the list.
           The voltage and current for each object is entered from the terminal.

           - num_elements: The number of new objects to be added to the list.
      """
      for i in range(num_elements):
         e1 = electrical()
         e1.read()
         self.push(e1)
      return

   def print(self):
      """
      print: Prints the content of the list, i.e. all stored electrical quantities.
      """
      for i in self.__data:
         i.print()
      return
 
def read_line():
   """
   read_line: Returns a line of text entered from the terminal and generates a new line.
   """
   s = input()
   print()
   return s

def read_float():
   """
   read_float: Returns a floating point number entered from the terminal and generates a new line.
               Input is entered again and again until a valid floating point number is entered.
               Floating point numbers can be entered both by a dot and a comma as decimal separator.
   """
   while True:
      s = read_line()
      s = s.replace(',', '.')
      try:
         return float(s)
      except ValueError:
         print("Invalid input, try again!\n")
