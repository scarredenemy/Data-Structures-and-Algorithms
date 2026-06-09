from collections import deque

class tree:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

def BFS(root):
  queue = deque()
  traverse = []
  queue.append(root)
  while queue:
    word = queue.popleft()
    if word.left is not None:
      queue.append(word.left)
    if word.right is not None:
      queue.append(word.right)
    traverse.append(word.val)
  
  return traverse

if __name__ == "__main__":
  root = tree(5)
  root.left = tree(10)
  root.right = tree(89)
  root.left.left = tree(76)
  root.left.right = tree(45)
  root.right.left = tree(55)
  root.right.right = tree(98)
  result = BFS(root)

  print(result)