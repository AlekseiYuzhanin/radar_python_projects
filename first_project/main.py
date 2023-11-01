count = 0
start = 1
end = 201

for z in range(start, end):
    for y in range(start, z):
        for x in range(start, y):
            if x**2 + y**2 == z**2:
                print(f"({x}, {y}, {z})")
                count += 1
                
print(f"Количество пифагоровых троек: {count}")