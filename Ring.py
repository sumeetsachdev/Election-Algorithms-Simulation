from random import randint
ring = {
    0:4,
    4:2,
    2:1,
    1:5,
    5:6,
    6:3,
    3:7,
    7:0
    }
msg_count = 0
coord = max(ring)
print("Current co-ordinator is ",coord)

def find_key(d,value_to_find):
    for key,value in d.items():
        if value == value_to_find:
            return key
while len(ring)>1:
    parent_node = find_key(ring,coord)
    print("Node " + str(parent_node) + " has detected that current co-ordinator " + str(coord) + " has stopped working")

    ring[parent_node] = ring[coord]
    del ring[coord]

    message_list = list()
    curr_node = parent_node
    message_list.append(parent_node)
    curr_node = ring[parent_node]

    while curr_node != parent_node:
        message_list.append(curr_node)
        curr_node = ring[curr_node]
        msg_count += 1
    coord = max(message_list)
    print("Node " + str(coord) + " has been elected as a new co-ordinator")

print("Total Messages", msg_count)
