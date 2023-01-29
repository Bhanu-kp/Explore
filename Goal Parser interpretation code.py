# Goal Parser interpretation
#1st approach
#Function convertor to replace the substrings
def convertor(a)-> str:
    ref=a
    return ref.replace("()","o").replace("(al)","al");
    
res=convertor("G()(al)")
print(res)


#2nd approach
def convertor(dictionary,varaiable,res,temp):
    dic=dic
    vara=variable
    res=temp=""
    for i in range(len(vara)):
        temp+=vara[i]
        #print("forlooptemp"+temp)
        if temp in dic:
            #print("ifloop"+temp)
            res+=dic[temp]
            temp=""
    return res;
        
dictionary={"()":"o","(al)":"al"}
varaiable="G()(al)"
Func=convertor(dictionary,vara)
print("Result: "+Func)



