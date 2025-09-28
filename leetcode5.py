# Write a function to find the longest common prefix string amongst an array of strings.
# vertical scanning solution
def longestCommonPrefix(lists):
    if len(lists) == 0:
        return ''
    base = lists[0]
    for i in range(len(base)):
        for word in lists[1:]:
            if i == len(word) or word[i] != base[i]:
                return base[0:i]
            return base
            # if i[j] == i[j+1]:
            #     print('ya')
lists = ["dog","racecar","car"]
print(longestCommonPrefix(lists))