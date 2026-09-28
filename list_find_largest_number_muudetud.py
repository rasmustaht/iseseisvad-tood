def second_largest_manual_sort(lst):
    if len(lst) < 2:
        return None  # Listis peab olema vähemalt 2 elementi

    last_largest = float('-inf')
    largest = float('-inf')

    for number in lst:
        if number > largest:
            # Leidsime uue suurima, senine suurim liigub teisele kohale
            last_largest = largest
            largest = number
        elif number > last_largest:
            # Arv on väiksem või võrdne suurimaga, aga suurem kui senine teine
            last_largest = number

    return last_largest