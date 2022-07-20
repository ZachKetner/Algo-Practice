from multiprocessing.sharedctypes import Value

class Node():
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None

class SLL():
    def __init__(self, nodeValue):
        self.head = Node(nodeValue)
    def front(self):
        runner = self.head
        if runner:
            print(runner.value)
        else:
            print("Null")
        return self
    def addFront(self, nodeValue):
        newNode = Node(nodeValue)
        runner = self.head
        runner.next = runner
        newNode.next = runner.next
        runner = newNode
        print(runner.value)
        print(runner.next.value)
        return self
    def removeFront(self):
        runner = self.head
        if runner.next:
            runner.next = self.head
        else:
            print(False)
        print(runner.value)
        return self


newList = SLL(9)

newList.removeFront()