
local_number = []
local_number = {"seoul":"02", "dajeon":"042", "chungnam":"044", "busan":"051"}
print(local_number)

print(local_number["dajeon"])

local_number["daegu"] = '053'
print(local_number)

print("keys:", local_number.keys())
print("values:", local_number.values())

print("items:", local_number.items())

for item in local_number.items():
    k, value = item
    print("k:", k, "value:", value)

for k, v in local_number.items():
    print("k:", k, "value:", value)