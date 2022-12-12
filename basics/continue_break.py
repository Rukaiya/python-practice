for index in range(10):
    if index % 2:
        continue

    print(index)

print('------------')

counter = 0
while counter < 10:
    counter += 1

    if not counter % 2:
        continue

    print(counter)