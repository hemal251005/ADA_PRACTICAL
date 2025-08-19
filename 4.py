import time

# Iterative Factorial
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Recursive Factorial
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Time Analysis
def time_analysis(n):
    print(f"\nCalculating factorial of {n}:")

    # Iterative method
    start = time.time()
    result_iter = factorial_iterative(n)
    end = time.time()
    print(f"Iterative Factorial: {result_iter}")
    print(f"Time (Iterative): {end - start:.8f} seconds")

    # Recursive method
    start = time.time()
    result_rec = factorial_recursive(n)
    end = time.time()
    print(f"Recursive Factorial: {result_rec}")
    print(f"Time (Recursive): {end - start:.8f} seconds")

# Main Program
if __name__ == "__main__":
    num = 10
    print("Factorial using Iterative:", factorial_iterative(num))
    print("Factorial using Recursive:", factorial_recursive(num))

    # Time comparison
    time_analysis(10)
    time_analysis(100)
