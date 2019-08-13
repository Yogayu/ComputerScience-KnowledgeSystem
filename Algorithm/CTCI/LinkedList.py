'''
@author: youxinyu
@date: 2018-8-29
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(data)

    def prepend(self, data):
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head

    def delete(self, data):
        if self.head == None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next != None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def __str__(self):
        current = self.head
        result = ''
        if current == None:
            result = 'None'
        else:
            result = str(current.data) + ' '
        while current.next != None:
            result += str(current.next.data) + ' '
            current = current.next
        return result


def main():
    myLinkedList = LinkedList()
    
    myLinkedList.append(1)
    myLinkedList.append(6)
    myLinkedList.append(12)
    myLinkedList.append(1)
    print(myLinkedList)

    myLinkedList.delete(1)
    print(myLinkedList)

    myLinkedList.prepend(3)
    print(myLinkedList)


if __name__ == '__main__':
    main()
