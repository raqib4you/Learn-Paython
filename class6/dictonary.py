Data =  {
    "id" : "1029",
    "Title" : "This is great and first time",
    "Content" : "there have so many element using dictonary",
    "Author" : "Raqib",
    "Category" : "First",
    "slug" : "this-is-great-and-first-time"
}

# read data from Dic
# dic name then [] then element name with quotation marks
# dic name .get () element name with quotation marks

id = Data["id"]
title = Data["Title"]

id2 = Data.get("id")

print(id)
print(id2)
print(title)


#add new element on Dic
# there have 2 way to add new first Dic name [] element id with quotation marks then = then description with quotation marks
# using update Dic name.update then () it append automatically then {} and full dic element with details same like Dic element

Data ["From"] = "Dhaka"
Data.update({"With": "Faysal"})

print(Data)

#update  element on Dic
# there have 2 way to update dic

Data["Author"] = ["New"]
Data.update({"Category" : "2nd"})

print(Data["Author"])
print(Data["Category"])

#remove element from dic
# remove using pop just dic name.pop thene element id

Data.pop("Title")

print(Data)

newdata = Data.get("Content")

print(newdata)



