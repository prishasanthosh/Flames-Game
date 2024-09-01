def flames(name1,name2):
    name1=name1.lower().replace(" ","")
    name2=name2.lower().replace(" ","")

    name1list=list(name1)
    name2list=list(name2)

    for char in name1list[:]:
        if char in name2list:
            name1list.remove(char)
            name2list.remove(char)

    count=len(name1list+name2list)
    flames=["Friends","Love","Affection","Marriage","Enemy","Sibling"]
    
    while len(flames)>1:
        index=(count % len(flames))-1
        if index>=0:
            right=flames[index+1:]
            left=flames[:index]
            flames=right+left
        else:
            flames.pop()
    return flames[0]

if __name__=="__main__":
    name1=input("Enter first name: ")
    name2=input("Enter second name: ")

    result=flames(name1,name2)
    print(f"The relationship is: {result}")