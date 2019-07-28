class Queue:
    def __init__(self):
        self.items=[]

    def add(self, x):
        self.items.append(x)

    def get(self):
        return self.items

    def len(self):
        return len(self.items)
