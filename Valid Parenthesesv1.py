#my first vaid par it doesn't work tho
class Solution(object):
    def isValid(self, s):
        dic = {'(':')', '{':'}','[':']'}
        trueNum = []
        
        for i, char in enumerate(s):
            for ii, charr in enumerate(s):
                print(f'i:{i}')
                print(f'ii:{ii}') 
                print('')
                if len(s)>1:
                    if s[i] in dic and s[ii] in dic:
                        print(f'char:{char}')
                        print(f'charr:{charr}')
                        print(f's ii:{s[ii]}')
                        print('')
                        if i == ii and i < 1:
                            print('i is equal to ii')
                            if char in dic:
                                print('char is in dic')
                                print(f'dic charr: {dic[charr]}')
                                print(f's i+1: {s[i+1]}')
                                if dic[s[i]] == s[i+1]:
                                    print(True)
                                    trueNum.append('True')
                                    print(f'truenum: {trueNum}')
                                    print(f'ii: {ii}')
                                    print(f'i: {i}')
                                    if len(s)-(ii+1) > 1:
                                        print(f'len greather than ii {len(s)-(ii+1)} is greather than 1')
                                        print(f'ii: {ii}')
                                        print(f'i: {i}')
                                    else:
                                        print('len less than ii')
                                        return True
                                else:
                                    print('no')
                                    print('')
                                    if i == len(s)-1:
                                        trueNum.append('False')
                                        print(f'truenum: {trueNum}')
                                        return False
                                    else:
                                        pass
                            else:
                                print('s[ii+1] not in dic')
                                pass
                        else:
                            print('i not euqal to ii')
                            print(f'dic charr: {dic[charr]}')
                            print(f'char: {char}')
                            if char in dic:
                                print('char is in dic')
                                if dic[s[ii]] == s[i]:
                                    trueNum.append('True')
                                    print(f'truenum: {trueNum}')
                                    ii +=1
                                    i +=1
                                else:
                                    print('no')
                                    if i == len(s)-1:
                                        trueNum.append('False')
                                        print(f'truenum: {trueNum}')
                                        return False
                                    else:
                                        pass
                            else:
                                print('s[ii+1] not in dic')
                                pass
                    else:
                        if s[i] in dic:
                            print(f'{s[i]} is in dic')
                        elif s[ii] in dic:
                            print(f'{s[ii]} is in dic')
                    if len(s)-1 == i:
                        trueNum.append('False')
                        print(f'truenum: {trueNum}')
                        return False
                else:
                    trueNum.append('False')
                    print(f'truenum: {trueNum}')
                    return False
        if i == ii and i >= 0:
            if 'False' in trueNum:
                return False
            else:
                if i == len(trueNum):
                    print(i)
                    return True 
              
            
x = Solution()
print(x.isValid("(){}{}"))