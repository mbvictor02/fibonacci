import time
import json

def iterative_fibonacci(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def recursive_fibonacci(n):
    if n <= 1:
        return n    
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

# Load memoization data from a JSON file
def load_memo_from_file():
    try:
        with open('fibonacci_memo.json', 'r') as file:
            data = file.read()
            if data:
                return json.loads(data)
            else:
                return {}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
# Save memoization data to a JSON file
def save_memo_to_file(memo):
    with open('fibonacci_memo.json', 'w') as file:
        json.dump(memo, file)

def memoized_fibonacci(n):
    memo = load_memo_from_file()

    if str(n) in memo:
        return memo[str(n)]

    if n <= 1:
        return n

    result = memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)
    memo[str(n)] = result

    save_memo_to_file(memo)
    return result
# Function to measure execution time
def measure_time(func, n):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

# Set a large value of n
large_n = 40

# Measure execution time for each function
iterative_result, iterative_time = measure_time(iterative_fibonacci, large_n)
recursive_result, recursive_time = measure_time(recursive_fibonacci, large_n)
memoized_result, memoized_time = measure_time(memoized_fibonacci, large_n)

# Print results and execution times
print(f"Iterative Fibonacci result: {iterative_result}, Execution time: {iterative_time} seconds")
print(f"Recursive Fibonacci result: {recursive_result}, Execution time: {recursive_time} seconds")
print(f"Memoized Fibonacci result: {memoized_result}, Execution time: {memoized_time} seconds")
