from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

# Enable CORS (restricting to API routes for security)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Helper functions
def is_prime(n):
    """Check if a number is prime. Only defined for positive numbers."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is perfect. Only defined for positive numbers."""
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def is_armstrong(n):
    """Check if a number is an Armstrong number (works for negatives)."""
    digits = [int(d) for d in str(abs(n))]  # Use absolute value
    length = len(digits)
    return sum(d**length for d in digits) == abs(n)

def digit_sum(n):
    """Calculate the sum of the digits of a number (ignoring sign)."""
    return sum(int(d) for d in str(abs(n)))  # Use absolute value

def get_fun_fact(n):
    """Fetch a fun fact about the number from the Numbers API with a timeout."""
    url = f"http://numbersapi.com/{abs(n)}/math"  # Use absolute value to get valid API results
    try:
        response = requests.get(url, timeout=2)  # Timeout after 2 seconds
        if response.status_code == 200:
            return response.text
    except requests.exceptions.RequestException:
        return "Fun fact unavailable at the moment."
    return "No fun fact available."

# API endpoint
@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')

    # If the number parameter is missing
    if number is None:
        return jsonify({
            "error": True
        }), 400

    # Input validation: Ensure it's an integer
    if not number.lstrip('-').isdigit():
        return jsonify({
            "number": number,
            "error": True
        }), 400

    number = int(number)

    # Determine properties
    properties = []
    is_armstrong_number = is_armstrong(number)
    if is_armstrong_number:
        properties.append("armstrong")
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    # Prepare response
    response = {
        "number": number,
        "is_prime": is_prime(number) if number >= 0 else False,  # Prime is only for non-negative numbers
        "is_perfect": is_perfect(number) if number >= 0 else False,  # Perfect is only for non-negative numbers
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": get_fun_fact(number)
    }

    # Override fun_fact if the number is an Armstrong number
    if is_armstrong_number:
        digits = [int(d) for d in str(abs(number))]  # Use absolute value
        length = len(digits)
        armstrong_explanation = f"{number} is an Armstrong number because {' + '.join(f'{d}^{length}' for d in digits)} = {abs(number)}"
        response["fun_fact"] = armstrong_explanation

    return jsonify(response), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
