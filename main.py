numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primers = []
not_primers = []

for i in numbers:
    if i == 1:
        continue
    is_prime = True
    for k in range(2, i):
        if i % k == 0:
            is_prime = False
            break
    if is_prime is True:
        primers.append(i)
    else:
        not_primers.append(i)

print(primers)
print(not_primers)
