from flask import Flask, jsonify, request
from collections import OrderedDict

app = Flask(__name__)

# Helper functions for number classification

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is perfect."""
    n = int(abs(n))  # Convert to absolute integer to handle negative numbers
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    digits = [int(digit) for digit in str(n)]
    return sum(d ** len(digits) for d in digits) == n

def calculate_digit_sum(n):
    """Calculate the sum of digits of a number."""
    return sum(int(digit) for digit in str(n))

def generate_fun_fact(n):
    """Generate a fun fact for Armstrong numbers."""
    if is_armstrong(n):
        return f"{n} is an Armstrong number because "
