from bs4 import BeautifulSoup
from collections import Counter
import numpy as np
import random

# HTML content
html_content = """
<html>
<head>
<title>Our Python Class exam</title>

<style type="text/css">
	
	body{
		width:1000px;
		margin: auto;
	}
	table,tr,td{
		border:solid;
		padding: 5px;
	}
	table{
		border-collapse: collapse;
		width:100%;
	}
	h3{
		font-size: 25px;
		color:green;
		text-align: center;
		margin-top: 100px;
	}
	p{
		font-size: 18px;
		font-weight: bold;
	}
</style>

</head>
<body>
<h3>TABLE SHOWING COLOURS OF DRESS BY WORKERS AT BINCOM ICT FOR THE WEEK</h3>
<table>
	
	<thead>
		<th>DAY</th><th>COLOURS</th>
	</thead>
	<tbody>
	<tr>
		<td>MONDAY</td>
		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
	</tr>
	<tr>
		<td>TUESDAY</td>
		<td>ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE</td>
	</tr>
	<tr>
		<td>WEDNESDAY</td>
		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE</td>
	</tr>
	<tr>
		<td>THURSDAY</td>
		<td>BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
	</tr>
	<tr>
		<td>FRIDAY</td>
		<td>GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE</td>
	</tr>

	</tbody>
</table>

<p>Examine the sequence below very well, you will discover that for every 1s that appear 3 times, the output will be one, otherwise the output will be 0.</p>
<p>0101101011101011011101101000111 <span style="color:orange;">Input</span></p>
<p>0000000000100000000100000000001 <span style="color:orange;">Output</span></p>
<p>
</body>
</html>
"""

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Dictionary to hold lists of colors for each day
colors_by_day = {
    "MONDAY": [],
    "TUESDAY": [],
    "WEDNESDAY": [],
    "THURSDAY": [],
    "FRIDAY": []
}

# Extract colors from HTML
for row in soup.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) == 2:
        day_cell = cells[0].get_text().strip()
        colors_cell = cells[1].get_text().strip()

        if day_cell in colors_by_day:
            colors = colors_cell.split(', ')
            colors_by_day[day_cell] = [color.upper() for color in colors]

# Collect all colors into a single list
all_colors = []
for colors in colors_by_day.values():
    all_colors.extend(colors)

# Count the frequency of each color
color_counter = Counter(all_colors)

# 1. Mean Color (Most Common Color)
mean_color = color_counter.most_common(1)[0][0]

# 2. Most Worn Color Throughout the Week
most_worn_color = color_counter.most_common(1)[0][0]

# 3. Median Color
sorted_colors = sorted(all_colors)
median_index = len(sorted_colors) // 2
if len(sorted_colors) % 2 != 0:
    median_color = sorted_colors[median_index]
else:
    median_color = sorted_colors[median_index - 1]

# 4. BONUS: Get the variance of the colors
frequencies = np.array(list(color_counter.values()))
color_variance = np.var(frequencies)

# 5. BONUS: Probability of Choosing Red
total_colors = len(all_colors)
red_count = color_counter.get('RED', 0)
probability_red = red_count / total_colors

# 6. BONUS: Recursive Searching Algorithm
def recursive_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_search(arr, target, mid + 1, high)
    else:
        return recursive_search(arr, target, low, mid - 1)

# 7. Program to Generate Random 4-Digit Binary Number and Convert to Base 10
def generate_random_binary():
    return ''.join(random.choice('01') for _ in range(4))

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

binary_number = generate_random_binary()
decimal_number = binary_to_decimal(binary_number)

# 8. Program to Sum the First 50 Fibonacci Numbers
def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1
    while len(fibonacci_sequence) < n:
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

def sum_fibonacci(sequence):
    return sum(sequence)

num_fibonacci = 50
fibonacci_sequence = generate_fibonacci(num_fibonacci)
fibonacci_sum = sum_fibonacci(fibonacci_sequence)

# Print results
print("1. Mean Color (Most Common Color):", mean_color)
print("2. Most Worn Color Throughout the Week:", most_worn_color)
print("3. Median Color:", median_color)
print("4. Color Variance:", color_variance)
print("5. Probability of Choosing Red:", probability_red)

# Recursive search example
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target_number = int(input("Enter the number to search: "))
index = recursive_search(numbers, target_number, 0, len(numbers) - 1)
print(f"6. Number found at index: {index}" if index != -1 else "Number not found")

print("7. Random 4-digit binary number converted to base 10:", decimal_number)
print(f"8. The sum of the first {num_fibonacci} Fibonacci numbers is:", fibonacci_sum)
