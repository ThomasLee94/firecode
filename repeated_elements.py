def duplicate_items(numbers: [int]) -> [int]: 
    output = list()
    
    numbers.sort()

    for i in range(len(numbers)):
        if numbers[i] == numbers[i - 1]:
            output.append(numbers[i])

    return output