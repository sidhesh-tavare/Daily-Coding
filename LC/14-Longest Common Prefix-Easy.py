class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs: return ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        minn = min(len(first),len(last))
        res = ""
        print(strs)
        prev = False
        if first[0] == last[0]:
            prev = True
            res+=first[0]
        for x in range(1,minn):
            
            if first[x]==last[x] and prev :
                res+=first[x]
            else: break
        return res

        