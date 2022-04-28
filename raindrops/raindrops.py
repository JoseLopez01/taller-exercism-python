def convert(number):
    result = ''
    for key, value in list(zip([3, 5, 7], ['Pling', 'Plang', 'Plong'])): 
        if number % key == 0:
            result += value

    return result if result else str(number)
