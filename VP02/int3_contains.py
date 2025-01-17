def contains_digit_3(number):
  return '3' in str(number)


count = 0
for i in range(1, 2025):
  if contains_digit_3(i):
    count += 1

print("Количество чисел от 1 до 2024, содержащих хотя бы одну цифру 3:", count)
