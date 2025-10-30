def lstNum(): 
    lst = [10 ,3 ,7 ,6 ,5 ,1 ,2 ,4 ,9 ,8]

    nova_lst = [i * 3 for i in lst]

    print(nova_lst)
    print(type(nova_lst))

def lstInt():
    lst = ["10" ,"3" ,"7" ,"6" ,"5" ,"1" ,"2" ,"4" ,"9" ,"8"]

    nova_lst = [int(i) for i in lst]

    print(nova_lst)
    print(type(nova_lst))

def listNumStr():
    lst = ["Arvore", "2", "zezo", "6", "46", "Arroz", "luis", "4", "43", "84", "53", "GodOFWar", "32", "42", "Quinze"]
    
    onlyNums = [int(i) for i in lst if i.isnumeric()]
    print(onlyNums)

x = [[1,2,3], [4,5,6], [7,8,9]]

x_dobro = [[x * 2 for x in linha] for linha in x]
print(x_dobro)

#listNumStr()
#lstNum()
#lstInt()
