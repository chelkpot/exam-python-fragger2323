# student_solution.py

# Задание 1
s1 = input()
pos = s1.find(',')
part1 = s1[:pos]
part2 = s1[pos+1:]

print(len(part1) > len(part2))
print(part1 == part2)
print(part1.find(part2) != -1)

# Задание 2
s2 = input()
s2_stripped = s2.strip()
print(s2_stripped)
print(len(s2_stripped))
print(s2_stripped.count('a'))
print(s2_stripped.replace('a', '@'))
print(s2_stripped and s2_stripped[0].isupper())

# Задание 3
s3 = input()
print(s3[1:-1])
print(s3[::2])
print(s3.lower()[::-1])

# Задание 4
numbers = list(map(int, input().split()))
sorted_nums = sorted(numbers)
print(sorted_nums)
print(sum(sorted_nums))
print(min(sorted_nums), max(sorted_nums))

# Задание 5
s5 = input()
s5_lower = s5.lower()
s5_no_spaces = s5.replace(' ', '')
is_palindrome = s5_no_spaces == s5_no_spaces[::-1]
no_spaces = ' ' not in s5
print(is_palindrome and no_spaces)

# Задание 6
num = int(input())
hex_str = hex(num)[2:]
print(hex_str)
print(len(hex_str))
print('a' in hex_str)

# Задание 7
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month_num = int(input())
month_index = month_num - 1
print(months[month_index])

