def kaprekars_constant(num):
    num_list = list(num)
    ascending_order_list = sorted(num_list)
    descending_order_list = num_list[::-1]
    descending = "".join(descending_order_list)
    ascending = "".join(ascending_order_list)
    final_value = str(int(descending) - int(ascending))

    if len(final_value) < len(num):
        final_value = '0' + final_value
    return final_value

count = 0
num = input("Enter number : ")
numbers = []

while num not in numbers:
    count += 1
    numbers.append(num)
    num = kaprekars_constant(num)

print(count,num)
