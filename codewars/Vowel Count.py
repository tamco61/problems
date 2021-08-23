def get_count(input_str):
    num_vowels = 0
    alf = 'aeiou'
    for i in input_str:
        if i in alf:
            num_vowels += 1
    return num_vowels