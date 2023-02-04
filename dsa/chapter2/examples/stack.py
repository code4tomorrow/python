class Stack:
    def __init__(self):
        # Make List
        self.stack_list = []

    def appending(self, item):
        # Checks to see if there are any duplicates in list
        if item in self.stack_list:
            # If so it returns error
            return "Value Already Exists"
        else:
            self.stack_list.append(item)

    def pops(self):
        # Checks to see if list is empty
        if len(self.stack_list) != 0:
            # if it isn’t empty it removes last value
            return self.stack_list.pop()
        else:
            return "List is Empty"


Check_Stack = Stack()

# Should add value to list
Check_Stack.appending(100)
Check_Stack.appending(200)
Check_Stack.appending(300)

# Should print 300 and then 200
print(Check_Stack.pops())
print(Check_Stack.pops())
