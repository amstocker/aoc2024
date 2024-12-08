data = list(map(
    lambda line: (
        int(line[0]),
        list(reversed(list(map(int, line[1].split()))))
    ),
    [line.split(':') for line in open("day7.txt").read().splitlines()]
))


def evaluations(numbers, concat=False):
    if len(numbers) == 1:
        yield numbers[0]
    else:
        for intermediate in evaluations(numbers[1:], concat):
            yield intermediate + numbers[0]
            yield intermediate * numbers[0]
            if concat:
                yield int(str(intermediate) + str(numbers[0]))

def calibration(concat=False):
    sum = 0
    for (n, numbers) in data:
        for m in evaluations(numbers, concat):
            if n == m:
                sum += n
                break
    return sum


# Part 1
print(calibration())

# Part 2
print(calibration(concat=True))