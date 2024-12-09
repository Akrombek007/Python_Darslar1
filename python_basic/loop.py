# Example 1: Using 'for' with range
for i in range(5):  # 0, 1, 2, 3, 4
    print(f"Iteration {i}")

# Example 2: Iterating over a list
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(f"Number: {num}")

# Example 3: 'while' loop
counter = 0
while counter < 5:
    print(f"Counter: {counter}")
    counter += 1

# Example 4: Infinite loop with 'while' (useful for interactive programs)
while True:
    user_input = input("Enter 'exit' to stop: ")
    if user_input == "exit":
        break
# Example 5: 'break' in a loop
for i in range(10):
    if i == 5:
        print("Breaking loop at 5")
        break
    print(i)

# Example 6: 'continue' in a loop
for i in range(10):
    if i % 2 == 0:  # Skip even numbers
        continue
    print(f"Odd number: {i}")

# Example 7: 'pass' as a placeholder
for i in range(5):
    if i == 3:
        pass  # No action taken here
    else:
        print(f"Processing {i}")
# Example 8: Nested 'for' loops
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()

# Example 9: Nested loops for combinations
colors = ["red", "green"]
objects = ["ball", "box"]

for color in colors:
    for obj in objects:
        print(f"{color} {obj}")

# Example 10: Nested 'while' and 'for'
x = 1
while x < 3:
    for y in range(3):
        print(f"x={x}, y={y}")
    x += 1
