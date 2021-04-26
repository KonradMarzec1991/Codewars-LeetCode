class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ''
        for item in zip(*strs):
            if len(set(item)) == 1:
                common += item[0]
            else:
                break
        return common
