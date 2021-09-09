class bankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def __getitem__(self, item: str):
        if item == "owner":
            return self.owner
        elif item == "balance":
            return self.balance
        else:
            # if the attribute isn't a valid attribute, you should
            # raise an AttributeError
            raise AttributeError

    def __setitem__(self, item: str, value):
        if item == "owner":
            self.owner = value
        elif item == "balance":
            self.balance = value
        else:
            # if the attribute isn't a valid attribute, you should
            # raise an AttributeError
            raise AttributeError

    def __bool__(self):
        """
        If we wanted the bank account to return True if the person
        is not bankrupt and False if they are bankrupt, we could do:
        """
        return self.balance > 0


account = bankAccount("John", 100)
print(account["owner"])
print(account["balance"])
account["balance"] = 200
print(account["balance"])
account["owner"] = "John Jr."
print(account["owner"])


print(bool(account))
if account:
    print("not bankrupt")
