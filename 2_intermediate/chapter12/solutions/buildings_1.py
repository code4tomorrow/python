# Create a class called 'building'
# It should have a build method that prints:
# "under construction..."
# "built"
# It should also have an __init__ method that runs the build method
# (basically, the __init__ method should call the build method)
# The __init__ method should also set an attribute 'built' to True

# Create a class 'library'
# It should be a child class from 'building'.
# Its init method should run building's init method. It should also
# create an empty list called 'books'
# 'library' should also have a 'restock' method
# that asks the user for a book to buy and prints "bought %s" where
# %s is the bookname. The 'restock' method should also append the
# book's name to the library's list 'books'
# Lastly, the library class should have a method 'catalog' that prints
# all the books in the library on separate lines

# Finally, instantiate the library class
# (you should see "under construction..." and "built" if you did it right

class building:
  def __init__(self):
    self.build()
    self.built = True

  def build(self):
    print("under construction...")
    print("built")

class library(building):
  def __init__(self):
    super().__init__()
    self.books = []

  def restock(self):
    book = input("What book should we buy?  ")
    print("Bought %s" % book)
    self.books.append(book)

  def catalog(self):
    print("Here are our books:")
    for book in self.books:
      print(book)

oak_library = library()
