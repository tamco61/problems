def sum_two_smallest_numbers(numbers):
    return sum(sorted([i for i in numbers if i.__class__.__name__ == 'int' and i >= 0])[:2])
