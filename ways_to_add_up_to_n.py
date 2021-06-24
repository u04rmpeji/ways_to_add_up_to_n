def ways_to_add_up_to_n(n: int, by: list, stack: list = None):
    # initialize
    if not stack:
        stack = []
        by = list(set(by))
        by.sort()
    this_layer = []
    previous_layer = []
    if n - min(by) >= 0:
        index = 0
        for number in by:
            if n - number == 0:
                this_layer.append(stack + [number])
            elif n - number < 0:
                break
            else:
                previous_layer.extend(ways_to_add_up_to_n(n - number, by[index:], stack + [number]))
            index += 1
    return previous_layer + this_layer


if __name__ == "__main__":
    print(ways_to_add_up_to_n(17, [3, 7, 5, 11]))
