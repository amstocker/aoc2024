[data1, data2] = open("day5.txt").read().split('\n\n')

rules   = set(tuple(map(int, line.split('|'))) for line in data1.splitlines())
updates =     [list(map(int, line.split(','))) for line in data2.splitlines()]

def unordered_pairs(update):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if (update[j], update[i]) in rules:
                yield i, j

def is_ordered(update):
    for _ in unordered_pairs(update):
        return False
    else:
        return True

def is_not_ordered(update):
    return not is_ordered(update)
    
def order(update):
    for i, j in unordered_pairs(update):
        update[i], update[j] = update[j], update[i]
    return update

def aggregate(updates):
    return sum(map(lambda update: update[len(update)//2], updates))


# Part 1
print(aggregate(filter(is_ordered, updates)))

# Part 2
print(aggregate(map(order, filter(is_not_ordered, updates))))
