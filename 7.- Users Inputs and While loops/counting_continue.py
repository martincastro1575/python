#imprimiendo odd numbers con while
current_number = 0
while current_number <= 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

print('----------------------')
#imprimiendo odd numbers con for
for values in range(1,12):
    if values % 2 == 0:
        continue
    print(values)