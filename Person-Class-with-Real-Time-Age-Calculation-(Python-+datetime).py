'''
  ============================================
  Import the datetime library
  ============================================
  Used for working with dates and times.
  In this case, it will be used to get the current year and calculate age.
'''
from datetime import datetime

'''
  ============================================
  DEFINITION OF A "Person" CLASS
  ============================================
'''
class Person:
  '''
   Class constructor method
   Executes automatically when creating a Person object
  '''
  def __init__(self, first_name, last_name, id_number, birth_year, country, gender):
    # Save the values as internal object attributes
    self._first_name = first_name
    self._last_name = last_name
    self._id_number = id_number        # ID or identification number
    self._birth_year = birth_year      # year of birth
    self._country = country
    self._gender = gender

  '''
   ============================================
   Method to print the person's information
   ============================================
  '''
  def print_info(self): 
    # Returns a text with all the person's data
    return f'''
    First Name: {self._first_name}
    Last Name: {self._last_name}
    Identification: {self._id_number}
    Country of Birth: {self._country}
    Gender: {self._gender}
    '''
  '''
   ============================================
   Method to calculate age
   ============================================
  '''
  def calculate_age(self): 
    current_year = datetime.now().year   # Gets the current year from the system
    age = current_year - self._birth_year   # Subtracts current year minus birth year
    return age                        # Returns the age

'''
  ============================================
  CREATION OF A "Person" CLASS OBJECT
  ============================================
'''
# Create a person with example data
p = Person("Johana", "Garcia", "12345", 2000, "Colombia", "Female")

'''
 ============================================
 USING THE CLASS METHODS
 ============================================
'''
print(p.print_info())                        # Displays all data on screen
print("Age is: ", p.calculate_age())    # Calculates and displays the age
