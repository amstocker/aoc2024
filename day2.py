data = [list(map(int, line.split())) for line in open("day2.txt").read().splitlines()]

is_sorted = lambda levels: sorted(levels) == levels or list(reversed(sorted(levels))) == levels
make_deltas = lambda levels: [abs(levels[i+1] - levels[i]) for i in range(len(levels) - 1)]

def safe(levels):
    deltas = make_deltas(levels)
    return is_sorted(levels) and min(deltas) >= 1 and max(deltas) <= 3

# Part 1
print(len(list(filter(safe, data))))

# Part 2
def safe_with_removal(levels):
    return any(safe(levels[:i] + levels[i+1:]) for i in range(len(levels)))

print(len(list(filter(safe_with_removal, data))))