from LinkedList import LinkedList

def remove_dups(mm):
    if mm.head is None:
        return
    current=mm.head
    seen=set([current.value])
    while current.next:
        if current.next.value in seen:
            current.next=current.next.next
        else:
            seen.add(current.next.value)
            current=current.next
    return mm

def remove_dups_followup(mm):
    if mm.head is None:
       return
    currnet=mm.head
    while current:
        runner=current
        while  runner.next:
               runner.next.value==current.value
               runner.next = runner.next.next
        else:
            runner=runner.next
            current=current.next
    return mm.head

mm = LinkedList()
mm.generate(100, 0, 9)
print(mm)
remove_dups(mm)
print(mm)

mm.generate(100, 0, 9)
print(mm)
remove_dups_followup(mm)
print(mm)




