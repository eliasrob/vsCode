def solution(s):

    sList = list(s)
    CaseIdx = [idx for idx in range(len(s)) if s[idx].isupper()]
    for i in CaseIdx:
        sList[i] = " "+sList[i]
    res = ''.join(sList)
    print(res)
    return res
    


solution("helloWorld")
solution("camelCase")
solution("breakCamelCase")