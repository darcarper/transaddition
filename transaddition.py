
funcion = int(input("Which function do you want to use? (1 for words, 2 for lists): "))
    
def function1(word1,word2):
    i=0
    j=0
    if len(word1)== (len(word2)-1):
        word22=word2
        while i<len(word1):
            
             
                
            finder=word22.find(word1[i])
            if finder==-1:
                j+=1
                    
                if j>=2:
                    #print("Can`t be made via a transaddition")
                    return 0
                        
            else:
                word22=word22.replace(word1[i],  '', 1)
                #print(word22)
            
            if i==len(word1)-1: 
                if j>=1:
                    #print('Can`t be made via a transaddition')
                    return 0
                else:
                    #print('Can be made via a transaddition')
                    return 1
            i+=1      
    else:
        #print('Can`t be made via a transaddition')
        return 0
def function2(list1,list2):
    for word1 in list1:
        dict1 = {word1: []}
        for word2 in list2:
            
            f1=function1(word1,word2)
            

            if f1==1:
              
                dict1[word1].append(word2)
                            
        if len(dict1[word1])!=0:
            print('"%s" can be used with addition to are: ' %  word1, dict1[word1])   



if funcion ==1:
    word1 = str(input("word1: "))
    word2 = str(input("word2: "))
    if function1(word1,word2)==1:
        print('Can be made via a transaddition')
    else:
        print("Can't be made via a transaddition")



if funcion==2:
    list1=[]
    list2=[]
    word1='1'
    word2='1'
    print("Enter 0 to end list")
    while word1 !='0':
        word1 = str(input("Enter word for list 1: "))
        if word1 !='0':
            list1.append(word1)
    while word2 !='0':
        word2 = str(input("Enter word for list 2: "))
        if word2 !='0':
            list2.append(word2)
    print('List 1 consists of:',list1)
    print('List 2 consists of:',list2)
    function2(list1,list2)