class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here
        if root == None:
            return -1
        if root.left == None and root.right == None:
            return 0
        return 1 + max(self.getHeight(root.right), self.getHeight(root.left))
            

T=int(input())