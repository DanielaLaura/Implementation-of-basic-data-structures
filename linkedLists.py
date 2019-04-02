class linkedListNode:
    def _init_(self, value, nextNode=None):
        self.value=value
        self.nextNode=nextNode

def insertNode(head, valuetInsert):
    currentNode=head
    while currentNode is not None:
        if currentNode.nextNode is None:
           currentNode.nextNode=linkedListNode(valuetInsert)
           return head
        currentNode=currentNode.nextNode
def deleteNode(head, valuetoDelete):
    currentNode=head
    previousNode=None
    while currentNode is not None:
        if currentNode.value==valuetoDelete:
            if previousNode is None:
                newHead=currentNode.nextNode
                currentNode.nextNode=None
                return newHead
            previousNode.nextNode=currentNode.nextNode
            return head
        previousNode=currentNode
        currentNode=currentNode.nextNode
    return head



# "3" -> "7" -> "10"

node1 = linkedListNode("3") # "3"
node2 = linkedListNode("7") # "7"
node3 = linkedListNode("10") # "10"

node1.nextNode = node2 # node1 -> node2 , "3" -> "7"
node2.nextNode = node3 # node2 -> node3 , "7" -> "10"

head = node1

print ("Traversing the regular linkedList")

# Regular Traversal
currentNode = head
while currentNode is not None:
      print currentNode.value
      currentNode = currentNode.nextNode

print()


print ("deleting the node '7'")
newHead = deleteNode(head, "10")