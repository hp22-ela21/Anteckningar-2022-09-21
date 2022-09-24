################################################################################
# main.py: Demonstration of Python classes.
################################################################################
from electrical import electrical_list

def main():
   """
   main: Stores data for five electrical quantities, entered from the terminal, in a list. 
         The quantities are printed in the terminal before the program terminates.
   """
   l1 = electrical_list()
   l1.add(5)
   l1.print()
   return

################################################################################
# If the current file is the startup file of the project (recognized by the
# variable __main__) the main function is called to start the program.
################################################################################
if __name__ == "__main__":
   main()