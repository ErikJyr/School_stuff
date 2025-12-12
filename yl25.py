me = {
    "first_name": "Erik",
    "last_name": "Jyr",
    "birth_year": 2009,
    "location": "Estonia",
    "favorite_dessert": "Black forest cake"
}

print(me["location"])
print(me.get("location"))

me["favorite_dessert"] = "chocolate cake"

for key in me.keys():
    print(key)

for value in me.values():
    print(value)

for key in me:
    print(me[key])

print("id_code" in me)
print(len(me))

me["height_cm"] = 170
me.pop("birth_year")

data = {"a": 1, "b": 2}
copy_data = data
data.clear()

data = {"a": 1, "b": 2}
del data
