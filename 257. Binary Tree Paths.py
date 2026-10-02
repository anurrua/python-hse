class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return[]
        stack=[(root,str(root.val))]
        res=[]
        while stack:
            node,path=stack.pop()
            if not node.left and not node.right:
                res.append(path)
            if node.right:
                stack.append((node.right,path+"->"+str(node.right.val)))
            if node.left:
                stack.append((node.left,path+"->"+str(node.left.val)))
        return res