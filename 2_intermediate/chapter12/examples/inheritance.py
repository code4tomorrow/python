class Test:
	  def __init__(self):
		    self.x = 0
    
class Derived_Test(Test)  # makes Derived_Test a child of Test
	  def __init__(self):
		    Test.__init__(self)  # do Test's __init__ method
		    # Test's __init__ gives Derived_Test the attribute 'x'
		    self.y = 1


b = Derived_Test()
print(b.x, b.y)
