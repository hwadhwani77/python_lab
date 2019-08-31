from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=' ')
      temp = temp.next
    print()


def find_cycle_start(head):
  cycle_length = 0
  # find the LinkedList cycle
  slow, fast = head, head
  if head is not None and head.next is not None:
    while (fast is not None and fast.next is not None):
        fast = fast.next.next
        slow = slow.next
        if slow == fast:  # found the cycle
            cycle_length = calculate_cycle_length(slow)
            break
    if fast == slow:
        return find_start(head, cycle_length)
    else: 
        return None
  else:
      return None
    


def calculate_cycle_length(slow):
  current = slow
  cycle_length = 0
  while True:
    current = current.next
    cycle_length += 1
    if current == slow:
      break
  return cycle_length


def find_start(head, cycle_length):
  pointer1 = head
  pointer2 = head
  # move pointer2 ahead 'cycle_length' nodes
  while cycle_length > 0:
    pointer2 = pointer2.next
    cycle_length -= 1
  # increment both pointers until they meet at the start of the cycle
  while pointer1 != pointer2:
    pointer1 = pointer1.next
    pointer2 = pointer2.next
  return pointer1

def rearrageLinkedList(head):
    if head is None:
        return None
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    
    second_half = slow
    second_head_half = reverse(second_half)
    first_head_half = head

    while first_head_half is not None and second_head_half is not None:
        temp = first_head_half.next
        first_head_half.next = second_head_half
        first_head_half = temp

        temp = second_head_half.next
        second_head_half.next = first_head_half
        second_head_half = temp
    
    if first_head_half.next is not None:
        first_head_half.next =None


def reverse(head):
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev

def main():
#   head = Node(1)
#   head.next = Node(2)
#   head.next.next = None
  # head.next.next = Node(3)
  # head.next.next.next = Node(4)
  # head.next.next.next.next = Node(5)
  # head.next.next.next.next.next = Node(6)

  # head.next.next.next.next.next.next = head.next.next
#   print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  # head.next.next.next.next.next.next = head.next.next.next
  # print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  # head.next.next.next.next.next.next = head
  # print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)
  head.next.next.next.next.next = Node(12)
  rearrageLinkedList(head)
  head.print_list()
main()
