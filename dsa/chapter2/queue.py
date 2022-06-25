class Queue:
    def __init__(self):
        # Make List
        self.queue_list = []

    def appending(self, item):
        # Checks to see if there are any duplicates in list
        if item in self.queue_list:
            # If so it returns error
            return "Value Already Exists"
        else:
            self.queue_list.append(item)

    def pops(self):
        # Checks to see if list is empty
        if len(self.queue_list) != 0:
            # if it isn’t empty it removes first value
            return self.queue_list.pop(0)
        else:
            return "List is Empty"


Check_Queue = Queue()

# Should add value to list
Check_Queue.appending(100)
Check_Queue.appending(200)
Check_Queue.appending(300)

# Should print 300 and then 200
print(Check_Queue.pops())
print(Check_Queue.pops())
