class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        path=[]
        def ispal(sta,e):
            while sta<e:
                if s[sta]!=s[e]:
                    return False
                sta+=1
                e-=1
            return True
        def bt(st):
            if st==len(s):
                res.append(path[:])
                return
            for end in range(st,len(s)):
                if ispal(st,end):
                    path.append(s[st:end+1])
                    bt(end+1)
                    path.pop()
        bt(0)
        return res
