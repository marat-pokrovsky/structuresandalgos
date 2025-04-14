from algorithms.sorting.bubble_sort import bubble_sort
from algorithms.sorting.heap_sort import heap_sort
from algorithms.sorting.insertion_sort import insertion_sort
from algorithms.sorting.merge_sort import merge_sort
from algorithms.sorting.quick_sort import quick_sort
from algorithms.sorting.selection_sort import selection_sort
from data_structures.doubly_linked_list.doubly_linked_list import DoublyLinkedList
from data_structures.hash_table.hash_table import HashTable
from data_structures.linked_list.linked_list import LinkedList
from data_structures.stack.stack import Stack
from data_structures.queue.queue import Queue

def bubble_sort_logic(data):
    return bubble_sort(data)

def heap_sort_logic(data):
    return heap_sort(data)

def insertion_sort_logic(data):
    return insertion_sort(data)

def merge_sort_logic(data):
    return merge_sort(data)

def quick_sort_logic(data):
    return quick_sort(data)

def selection_sort_logic(data):
    return selection_sort(data)

def doubly_linked_list_logic(data):
    dll = DoublyLinkedList()
    for item in data:
        dll.append(item)
    return dll.to_list()

def hash_table_logic(data):
    ht = HashTable(size=len(data))
    for key, value in data:
        ht.set(key, value)
    return ht.get_data()

def linked_list_logic(data):
    ll = LinkedList()
    for item in data:
        ll.append(item)
    return ll.to_list()

def stack_logic(data):
    stack = Stack()
    for item in data:
        stack.push(item)
    return stack.to_list()

def queue_logic(data):
    queue = Queue()
    for item in data:
        queue.enqueue(item)
    return queue.to_list()
