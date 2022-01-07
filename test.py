small_value = iter(range(3))
print(next(small_value))
print(next(small_value))
print(next(small_value))

small = iter(i for i in range(3))
print(next(small))
print(next(small))
print(next(small))

print(5//2)