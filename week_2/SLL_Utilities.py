from multiprocessing.sharedctypes import Value

class Node():
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None

class SLL():
    def __init__(self, nodeValue):
        self.head = Node(nodeValue)
    def display(self):
        runner = self.head
        while runner:  # while runner is not None
            print(runner.value)
            runner = runner.next
        return self
    def addToBack(self, nodeValue):
        newNode = Node(nodeValue)
        runner = self.head
        while runner.next is not None:
            runner = runner.next
        runner.next = newNode
        return self
    def contain(self, valueInput):
        runner = self.head
        foundValue = 0
        while runner:
            if runner.value == valueInput:
                print(True)
                foundValue = 1
                runner = runner.next
            else:
                runner = runner.next
        if foundValue == 0:
            print(False)
        else:
            return self
    def length(self):
        runner = self.head
        numValues = 0
        while runner:
            numValues += 1
            runner = runner.next
        print(numValues)
        return self
    def MoveMaxToBack(self):
        runner = self.head
        maxValue = self.head.value
        while runner:
            if runner.value > maxValue:
                tempNode = runner.next
                runner.next = self.head
                self.head = tempNode
            else:
                runner = runner.next
        runner = runner.next
        print(display())
        return self
newList = SLL(3)

newList.addToBack(4).addToBack(5).addToBack(8).addToBack(12).MoveMaxToBack()