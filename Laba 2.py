main_list = [10, 20, 3, 8, 1, 4, 2, 4, 17, 12, 11,
             "banana", "apple", "grape", "cherry", "orange", "pear", "kiwi", "plum", "peach", "mango", "strawberry"]

ints = sorted([x for x in main_list if isinstance(x, int)])
strings = sorted([x for x in main_list if isinstance(x, str)])

sorted_list = ints + strings

multiples_of_two = [x for x in ints if x % 2 == 0]

uppercased_strings = [x.upper() for x in strings]

print("Основний список:", main_list)
print("Відсортований список:", sorted_list)
print("Елементи, кратні двом:", multiples_of_two)

print("Рядки капсом:", uppercased_strings)
