class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from queue import Queue

class Codec:
    def __init__(self):
        self.res=[]
    def serialize_from_preTra(self, root):
        '''先序遍历序列化'''
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def tra(root:TreeNode):
            if not root:
                self.res.append('#')
            self.res.append(str(root.val))
            self.serialize(root.left)
            self.serialize(root.right)

        tra(root)
        return ",".join(self.res)

    def deserialize_from_preTra(self, data):
        '''先序遍历解序列化'''
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def tra(tree_list):
            if tree_list[0]=="#":
                res.pop(0)
                return None

            root=TreeNode(int(tree_list[0]))
            tree_list.pop(0)
            root.left=tra(tree_list)
            root.right=tra(tree_list)
            return root

        res=data.split(",")
        return tra(res)

    def serialize_lev(self, root:TreeNode):
        '''层次遍历序列化'''
        q=Queue(0)
        q.put(root)
        while not q.empty():
            node=q.get()
            if node:
                self.res.append(str(node.val))
            else:
                self.res.append("#")
                continue
            q.put(node.left)
            q.put(node.right)
        return ",".join(self.res)

    def deserialize_lev(self, data):
        '''层次遍历解序列化'''
        res=data.split(",")
        q=Queue(0)
        i=0
        if res[i]=="#":
            root=None
        else:
            root=TreeNode(int(res[i]))

        q.put(root)
        while not q.empty():
            t=q.get()
            if t:
                i+=1
                if res[i]=="#":
                    t.left=None
                else:
                    t.left = TreeNode(int(res[i]))

                i+=1
                if res[i]=="#":
                    t.right=None
                else:
                    t.right = TreeNode(int(res[i]))

                q.put(t.left)
                q.put(t.right)
        return root

f=Codec()
print(f.serialize_lev(f.deserialize_lev("1,2,3,#,#,#,#")))
