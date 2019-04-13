from random import randint
from random import choice
process = {}
process_list = {}
msg_count = 0

for i in range(8):
    process[i] = choice([True, False])
print(process)
process_list = [x for x in process if process[x]]
print("Current Processes: ")
print(process_list)

coord = max(process_list)
##del process_list[coord]
del process[coord]
process_list.pop(process_list.index(coord))

parent_node = choice(process_list)
print("Node " + str(parent_node) + " has detected that current co-ordinator " + str(coord) + " has stopped responding")
print(str(parent_node) + " is now conducting elections")

while process_list:
    current_candidates = [x for x in process if x > parent_node and process[x] and x != coord]
    msg_count += len(current_candidates)
    if len(current_candidates) == 0:
        print("No one responded. So", end=" ")
        coord = parent_node
    else:
        print(current_candidates, end=" ")
        print("respond and job of " + str(parent_node) + " is done")
        while current_candidates:
            curr = min(current_candidates)
            print(curr,end=" ")
            print("is conducting elections")
            current_candidates.pop(current_candidates.index(curr))
            if len(current_candidates) != 0:
                print(current_candidates, end=" ")
                print("respond and job of " + str(parent_node) + " is done")
            else:
                print("No one responded")
        coord = curr
    print("New co-ordinator is ", coord)
    print('\n\n\n')
    del process[coord]
    process_list.pop(process_list.index(coord))
    if process_list:
        parent_node = randint(min(process_list), max(process_list))
        print("Node " + str(parent_node) + " has detected that current co-ordinator " + str(coord) + " has stopped responding")
        print(str(parent_node) + " is now conducting elections")
    
print("Current co-ordinator is ",coord)


##print("Total number of messages",msg_count)
