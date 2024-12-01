lines = [line.split() for line in open("day1.txt").read().splitlines()]

list1 = sorted(map(int, [line[0] for line in lines]))
list2 = sorted(map(int, [line[1] for line in lines]))

# Part 1
print(sum(map(lambda t: abs(t[0] - t[1]), zip(list1, list2))))

# Part 2
print(sum(map(lambda x: x * list2.count(x), list1)))
