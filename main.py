person ={
    "name" : "shahad",
    "age" :18,
    "hobbies": ["painting","reading"]

}
print(person["name"])
print(person["age"])
person["age"]=19
person["country"]= "kuwait"
print(person)
print(f"number of objects in dictionary: {len((person))}")
person["hobbies"].append("coding")

def check_hobbies(person):
    if len(person["hobbies"]) >=4:
        return print("wow you are amzing")
    else:
        return print("keep exploring your hobbies")
check_hobbies(person)   