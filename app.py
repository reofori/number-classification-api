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
        return f"{n} is an Armstrong number because " + " + ".join(f"{d}^3" for d in str(n)) + f" = {n}"
    return "No fun fact available"

def classify_number_properties(n):
    """Classify properties of a given number."""
    properties = []
    if is_armstrong(n):
        properties.append("armstrong")
    if is_prime(n):
        properties.append("prime")
    if is_perfect(n):
        properties.append("perfect")
    if n % 2 != 0:
        properties.append("odd")
    else:
        properties.append("even")
    return properties

def validate_input(number_str):
    """Validate the input number to ensure it's an integer."""
    try:
        return int(number_str), None
    except (ValueError, TypeError):
        return None, f"Invalid input: {number_str} is not a valid integer."

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    # Get the number from the query parameter
    number_str = request.args.get('number')
    
    # Validate input
    number, error = validate_input(number_str)
    if error:
        # Ensure the error response matches the required format (number first, then error)
        return jsonify(OrderedDict([
            ("number", number_str),  # Place number first
            ("error", True)           # Place error second
        ])), 400

    # Get properties of the valid number
    properties = classify_number_properties(number)
    digit_sum = calculate_digit_sum(number)
    fun_fact = generate_fun_fact(number)

    # Create the response data
    data = OrderedDict([
        ("number", number),
        ("is_prime", is_prime(number)),
        ("is_perfect", is_perfect(number)),
        ("properties", properties),
        ("digit_sum", digit_sum),
        ("fun_fact", fun_fact)
    ])

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
