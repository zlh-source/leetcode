from typing import List
import numpy as np

class UF:
    def __init__(self,n:int):
        '''
        初始化并查集
        n:节点个数
        '''
        self.count=n  #连通分量的数量
        self.parent=[-1]*n
        self.size=[1]*n #连通分量的尺寸
        for i in range(n):
            self.parent[i]=i

    def union(self,p:int,q:int):
        '''
        连通节点p,q
        '''
        #先找到两个节点的根节点
        rootP=self.find(p)
        rootQ=self.find(q)
        if rootQ!=rootP:
            #小树接到大树下面，较平衡
            if self.size[rootP]>self.size[rootQ]:
                self.parent[rootQ]=rootP
                self.size[rootP]+=self.size[rootQ]
            else:
                self.parent[rootP]=rootQ
                self.size[rootQ]+=self.size[rootP]

        self.count-=1

    def connected(self,p:int,q:int) -> bool:
        '''
        判断p,q是否连通
        '''
        rootP=self.find(p)
        rootQ=self.find(q)
        return rootP==rootQ

    def find(self,x:int) -> int:
        '''
        返回x的根节点
        '''
        while self.parent[x]!=x:
            #先进行路径压缩,提高后续查找效率
            self.parent[x]=self.parent[self.parent[x]]
            x=self.parent[x]
        return x


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        all_a=set()
        for s in equations:
            all_a.add(s[0])
            all_a.add(s[-1])
        all_a=list(all_a)
        all_id=list(range(len(all_a)))

        uf=UF(len(all_a))

        def ch2id(ch:str) -> int:
            return all_id[all_a.index(ch)]

        for s in equations:
            if "==" in s:
                p,q=ch2id(s[0]),ch2id(s[-1])
                uf.union(p,q)
        for s in equations:
            if "!=" in s:
                p,q=ch2id(s[0]),ch2id(s[-1])
                if uf.connected(p,q):
                    return False
        return True


#990.等式方程的可满足性（中等）

eq=["a==b","b==c","a==c"]

f=Solution()
print(f.equationsPossible(eq))
