class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups= {}
        for i in strs:
            count_ana={}
            for j in i:
                count_ana[j]=count_ana.get(j,0)+1
            key=tuple(sorted(count_ana.items()))
            if key not in groups:
                groups[key]=[]
            groups[key].append(i)
        return list(groups.values())