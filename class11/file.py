

#first we need to open a file (file = open()) then give a name for file and write mode like a+, w+
#for new line we use \n
#then file close file.close()

file = open("first.txt", "a+")
file.writelines(input("write something")+ "\n")
file.close()