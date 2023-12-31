#!/usr/bin/python3

"""
A class Node, contains data and a pointer to the next node
int the singly linked list.
"""


class Node:
    """
    An init method for instantiation of an obj. Node.
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node  # next_node is next node ptr..
    """
    Retrieves the private instance attr, data.
    """
    @property
    def data(self):
        return self.__data
    """
    Modifies the private instance attr, data
    """
    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value
    """
    Retrieves a private instance attr. next_node.
    """
    @property
    def next_node(self):
        return self.__next_node
    """
    Sets a private instance attr. next_node
    """
    @next_node.setter
    def next_node(self, value):
        if value is None or type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


"""
A singly linked list class
"""


class SinglyLinkedList:
    """
    Init method, initializes instances of class.
    """
    def __init__(self):
        self.head = None

    """
    Inserts a node into the singly linked list
    """
    def sorted_insert(self, value):
        new_node = Node(value)  # create a Node.
        if self.head is None:  # empty linked list.
            new_node.next_node = self.head  # new node takes head ptr addr.
            self.head = new_node  # head ptr points to new node.
        else:  # linked list is not empty.
            temp = self.head  # assign a temp node to iterate.
            if self.head.data > value:
                new_node.next_node = self.head
                self.head = new_node
            else:
                while temp.next_node is not None:
                    if temp.next_node.data > value:
                        new_node.next_node = temp.next_node
                        temp.next_node = new_node
                        break
                    else:
                        temp = temp.next_node
                else:
                    temp.next_node = new_node

    """
    Prints a singly linked list to stdout
    """
    def display_linkedlist(self):
        if self.head is not None:
            temp = self.head
            while temp is not None:
                print(str(temp.data))
                temp = temp.next_node
