# You are given a string and two non-negative integers as input. The two integers specify the start and end indices of a substring in the given string. Create a new string by replicating the substring a minimum number of times so that the resulting string is longer than the input string.

# The input parameters are the string, start index of the substring and the end index of substring (endpoints inclusive) each on a different line.

# _____Solution_________

# Taking input from the user
input_str = input()
start_index = int(input())
end_index = int(input())

# Extract the substring
substring = input_str[start_index:end_index + 1]

# Calculate the length of the input string
input_length = len(input_str)

# Calculate the length of the substring
substring_length = len(substring)

# Calculate the number of times to replicate the substring
replication_factor = (input_length // substring_length) + 1

# Replicate the substring
replicated_substring = substring * replication_factor

# Extract the necessary characters from the replicated substring to make it one character longer than the input string
result = replicated_substring[:input_length + 1]

# Print the resulting string
print(result)
