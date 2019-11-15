import time
from bst import BinarySearchTree 
#time complexity of O(n^2)

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()



duplicates = []
bst = BinarySearchTree()

for name_1 in names_1:
    bst.insert(name_1)

for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_2)

end_time = time.time()
print(len(duplicates), duplicates)
print(end_time - start_time)

