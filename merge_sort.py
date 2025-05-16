from estrutura_lista import LinkedList, Node

def split_list(head):
    if head is None or head.next is None:
        return head, None

    slow = head
    fast = head.next
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    middle = slow.next
    slow.next = None
    return head, middle

def merge_sorted_lists(left, right):
    if not left:
        return right
    if not right:
        return left

    if left.data <= right.data:
        result = left
        result.next = merge_sorted_lists(left.next, right)
    else:
        result = right
        result.next = merge_sorted_lists(left, right.next)
    return result

def merge_sort_linked_list(head):
    if head is None or head.next is None:
        return head

    left_half, right_half = split_list(head)
    left_sorted = merge_sort_linked_list(left_half)
    right_sorted = merge_sort_linked_list(right_half)

    return merge_sorted_lists(left_sorted, right_sorted)
