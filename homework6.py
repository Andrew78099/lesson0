my_dict = {"Антон" : 16123131, "Семен" : 616513464, "Илья" : 116161321}
print(my_dict)
print("Existing value:",my_dict["Антон"])
print("No existing value:", my_dict.get("Маша"))
my_dict.update({"Саша" : 19123131, "Маша" : 618513464})
a = my_dict.pop("Саша")
print("Deleted value:", a)
print(my_dict)

my_set = {1, 2, 3, 1, 5, 3}
print("Set:",my_set)
my_set.add(11)
my_set.add("green")
my_set.remove(1)
print("Modified set:",my_set)