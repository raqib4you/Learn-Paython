Data = [
        "Moris",
        "Male",
        "Japan",
        "30-06-1998",
        "moriskha@gmail.com",
        "017896524",
]
Data2 = [
        "Rojina",
        "Female",
        "Japan",
        "30-06-1998",
        "moriskha@gmail.com",
        "017896524",
]

Gender = Data[1]
if Gender == "Male":
    name = "Boy"
    he = "He"
    his = "his"
else:
    name = "Girls"
    he = "She"
    his = "Her"

Ssentance = f" {Data[0]} is a good {name}. {he} lives in {Data[2]}.{his} " \
            f"Birthday is {Data[3]}. {his} Phone NUmber is {Data[5]}. {he} have a mail that is {Data[4]}"

print(Ssentance)