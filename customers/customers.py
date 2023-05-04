line_counter = 0
data_header = []
customer_list = []

with open(r"C:\Users\JS2-9\Documents\GitHub\HRD-python\customers\customers.csv", 'r')as customer_data:
    while 1:
        data = customer_data.readline()
        if not data:break
        if line_counter == 0:
            data_header = data.split(",")

        else:
            customer_list.append(data.split(","))

        line_counter += 1

print("Header : ", data_header)
for i in range(0,10):
    print("Data", i, ":", customer_list[i])
print(len(customer_list))