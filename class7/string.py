firststr = "raqib, habib, robin, tipu, faysal"

title = firststr.title()

print(title)


str = " raqib is a good boy for now "

stripestr = str.strip()
lstripestr = str.lstrip()
rlstripestr = str.rstrip()


print(str)
print(stripestr)
print(lstripestr)
print(rlstripestr)


str2 = "hello my name is raqibul mia, i am from dhaka"
 #string to list ot split string

list = str2.split()
list2 = str2.split(",")
print(list)
print(list2)


#list to string
#need to take a blank string and use.join() list name into opening braches

list3 = ["raqib", "is", "a", "good", "boy"]

listostr = " ".join(list3)
print(listostr)


#Dictonary to string

dic = {"name":"raqib", "age" : "25"}
dictostr = ("my name is{name} raqibul mia my age is {age}".format_map(dic))
print(dictostr)