d = {
    "Berlin": 450000,
    "Munich": 190000,
    "Los Angeles": 10000000
}

population = d.get("Los Angeles", 1500000)
# if population == None:
#     population = 10000000

print(population)