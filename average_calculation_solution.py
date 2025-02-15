def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}")

my_list = [10, 20, 30]
result = calculate_average(my_list)
print(f"The average is: {result}") #This will print 20.0 as expected