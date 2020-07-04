# STRINGS
# are immutable

# Basics
'hello'
"hello"

"double quotes are great for encapsulatin ' "

# Indexing

indexing_test = "this is my indexing tester"

indexing_test[0]  # t
indexing_test[5]  # i
indexing_test[-2]  # l

# Slicing - string[start idx : end idx (not including) : step]
slice_test = "this is my slice tester"

slice_test[3:]  # s is my slice tester
slice_test[:3]  # thi (doesn't include 3rd idx value)
slice_test[1:4]  # his
slice_test[::2]  # ti sm lc etr (every second ltr)

# Basic Methods
basic_methods_test = "this is my Basic methods tester"

basic_methods_test.upper()  # THIS IS MY BASIC METHODS TESTER
basic_methods_test.lower()  # this is my basic methods tester
basic_methods_test.capitalize()  # this is my basic methods tester

# ['this', 'is', 'my', 'Basic', 'methods', 'tester']
basic_methods_test.split()

# Print Formatting
print_formatting_test_1 = "Format this string"
print_formatting_test_2 = "like so"

final = f"{print_formatting_test_1} {print_formatting_test_2}"
print(final)  # Format this string like so
