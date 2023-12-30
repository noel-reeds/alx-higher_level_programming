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
        return next_node
    """
    Sets a private instance attr. next_node
    """
    @next_node.setter
    def next_node(self, value):
        if value is None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


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
        if self.__head is None:  # empty linked list.
            new_node.next_node = self.__head  # new node takes head ptr addr.
            self.__head = new_node  # head ptr points to new node.
        else:  # linked list is not empty.
            temp = self.__head  # assign a temp node to iterate.
            while temp.next_node is not None:
                if temp.next_node.data > value:
                    new_node.next_node = temp.next_node
                    temp.next_node = new_node
                else:
                    temp = temp.next_node
            temp.next_node = new_node

    """
    Prints a singly linked list to stdout
    """
    def display_linkedlist(self):
        if self.__head is None:
            temp = self.__head
            while tempt is not None:
                print(temp.data)
                temp = temp.next_node
