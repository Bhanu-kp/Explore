#list_to_frequency_dict
list1 = ['x','y','z','x','x','x','y', 'z','p','p','z']
dic ={}
temp = 0
def listtodict(list1, dic):
    for i in list1:
    #print("it is i:",i)
        if i in dic.keys():
            #print("It is i in dic",i)
            dic[i] = dic[i] + 1
        else:
            dic[i] = 1
    return dic;

result=listtodict(list1, dic)
print("Output: ",result)