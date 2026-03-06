class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        freq={}
        for c in t:
            if c in freq:
                freq[c]+=1
            else:
                freq[c]=1
        ml=float('inf')
        cnt=0
        left=0
        st=0
        for r in range(len(s)):
            if s[r] in freq:
                if freq[s[r]]>0:
                    cnt+=1
                freq[s[r]]-=1
            else:
                freq[s[r]]=-1
            while cnt==len(t):
                if r-left+1<ml:
                    ml=r-left+1
                    st=left
                freq[s[left]]+=1
                if freq[s[left]]>0:
                    cnt-=1
                left+=1
        if ml==float('inf'):
            return""
        else:
            return s[st:st+ml]
        
