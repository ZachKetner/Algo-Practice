from multiprocessing.sharedctypes import Value


class Node():
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None

class SLL():
    def __init__(self, nodeValue):
        self.head = Node(nodeValue)
    def addToBack(self, nodeValue):
        newNode = Node(nodeValue)
        runner = self.head
        while runner.next is not None:
            runner = runner.next
        runner.next = newNode
        return self
    def display(self):
        runner = self.head
        while runner:  # while runner is not None
            print(runner.value)
            runner = runner.next
        return self
    def maxValue(self): # Find the max value in a SLL and return that value
        runner = self.head
        maxValue = self.head.value
        while runner:
            if runner.value > maxValue:
                maxValue = runner.value
            else:
                runner = runner.next
        return maxValue

    def secondLargest(self): # Find the value in the second highest in the singly linked list
        max = self.maxValue()
        runner = self.head
        secondmax = self.head.value
        if self.head.value != max:
            secondmax = runner.value
        else:
            secondmax = runner.next.value
        while runner:
            if runner.value > secondmax:
                if runner.value == max:
                    runner = runner.next
                else:
                    secondmax = runner.value
            else:
                runner = runner.next
        return secondmax        
            
    def newSecondLargest(self):
        if self.head.value > self.head.next.value:
            max = self.head.value
            secondmax = self.head.next.value
        else:
            secondmax = self.head.value
            max = self.head.next.value
        runner = self.head.next.next
        while runner:
            if runner.value > secondmax:
                if runner.value > max:
                    max = runner.value
                else:
                    secondmax = runner.value
            else:
                runner = runner.next
        return secondmax


newList = SLL(9)


print(newList.addToBack(7).addToBack(5).addToBack(3).newSecondLargest())



