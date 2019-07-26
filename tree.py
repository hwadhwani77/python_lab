class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorder(temp:Node):
    if not temp:
        return
    inorder(temp.left)
    print(temp.val, end=" ")
    inorder(temp.right)

def insert(temp: Node, key:int):
    q = []
    q.append(temp)

    while(len(q)):
        temp = q[0]
        q.pop(0)

        if not temp.left:
            temp.left = Node(key)
            break
        else:            
            q.append(temp.left)

        if not temp.right:
            temp.right = Node(key)
            break
        else:            
            q.append(temp.right)            

def printLevelOrder(root: Node):
    h = height(root)
    for i in range (1, h+1):
        printGivenLevel(root, i)
    
def printGivenLevel(root: Node, level: int):
    if root is None:
        return
    if level == 1:
        print("%d" %(root.val))
    elif level > 1:
        printGivenLevel(root.left, level -1)
        printGivenLevel(root.right, level -1)

def height(node:Node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if(lheight > rheight):
            return lheight + 1
        else:
            return rheight + 1

root = Node(10)  
root.left = Node(11)  
root.left.left = Node(7)  
root.right = Node(9)  
root.right.left = Node(15)  
root.right.right = Node(8)

inorder(root)
insert(root, 12)  
print()
inorder(root)
print()
printLevelOrder(root)