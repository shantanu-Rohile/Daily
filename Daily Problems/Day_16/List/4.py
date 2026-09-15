# 40. Split List by First Character

def split_list(lst):
    res= sorted(lst)
    print(lst[0])
    for i in range(1,len(res)):
        
        if res[i][0] != res[i-1][0]:
            print("------------------------------")
        print(lst[i])

lst =  ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think','look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']

split_list(lst)