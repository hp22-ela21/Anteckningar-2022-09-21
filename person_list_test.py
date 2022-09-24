# Imports:
from person import person_list

def main():
   """
   main: Creates a person list named l1 and stores person data for five persons, entered
         from the terminalen. The person data is then printed in the terminal.
   """
   l1 = person_list()
   l1.add(5) 
   l1.print()
   return

if __name__ == "__main__":
   # If this file is the start script, the main function is called
   # to start the program:
   main()