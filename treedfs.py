class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def has_path(root, sum):
  if root is None:
    return False

  # if the current node is a leaf and its value is equal to the sum, we've found a path
  if root.val == sum and root.left is None and root.right is None:
    return True

  # recursively call to traverse the left and right sub-tree
  # return true if any of the two recursive call return true
  return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)

def find_paths(root, sum1):
  allPaths = []
  find_paths_recursive(root, sum1, [], allPaths)
  return allPaths


def find_paths_recursive(currentNode, sum1, currentPath, allPaths):
  if currentNode is None:
    return

  # add the current node to the path
  currentPath.append(currentNode.val)

  # if the current node is a leaf and its value is equal to sum, save the current path
  if currentNode.val == sum1 and currentNode.left is None and currentNode.right is None:
    allPaths.append(list(currentPath))
  else:
    # traverse the left sub-tree
    find_paths_recursive(currentNode.left, sum1 - currentNode.val, currentPath, allPaths)
    # traverse the right sub-tree
    find_paths_recursive(currentNode.right, sum1 - currentNode.val, currentPath, allPaths)

  # remove the current node from the path to backtrack,
  # we need to remove the current node while we are going up the recursive call stack.
  del currentPath[-1]

def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
#   print("Tree has path: " + str(has_path(root, 23)))
#   print("Tree has path: " + str(has_path(root, 16)))
  print("Tree paths with sum " + str(23) +
        ": " + str(find_paths(root, 23)))

main()
