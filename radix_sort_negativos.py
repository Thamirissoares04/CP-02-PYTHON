
from estrutura_lista import Node

def get_max_digits(head):
    max_num = 0
    current = head
    while current:
        if abs(current.data) > max_num:
            max_num = abs(current.data)
        current = current.next
    return len(str(max_num))

def get_digit(number, digit_index):
    return (number // 10**digit_index) % 10

def radix_sort_linked_list_negativos(head):
    if head is None or head.next is None:
        return head

    current = head
    while current:
        current.data = -current.data 
        current = current.next

    max_digits = get_max_digits(head)

    for d in range(max_digits):

        buckets = [[] for _ in range(10)]

        current = head
        while current:
            index = get_digit(current.data, d)
            buckets[index].append(current)
            current = current.next

        head = None
        tail = None
        for bucket in buckets:
            for node in bucket:
                node.next = None
                if not head:
                    head = node
                    tail = node
                else:
                    tail.next = node
                    tail = node

    current = head
    while current:
        current.data = -current.data  
        current = current.next

    return head
