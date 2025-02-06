Number Classification API
Overview
The Number Classification API is a simple RESTful API that takes a number and returns interesting mathematical properties about it along with a fun fact. The API provides information about whether the number is prime, perfect, Armstrong, or odd/even. It also provides a fun fact about the number retrieved from the Numbers API.

API Specification
The API accepts a GET request with a number parameter and returns the following details in JSON format:

Prime Status: Indicates whether the number is prime or not.
Perfect Status: Indicates whether the number is perfect or not.
Properties: Includes whether the number is Armstrong and/or odd/even.
Digit Sum: The sum of the digits of the number.
Fun Fact: A fun fact retrieved from the Numbers API.
Endpoint
GET /api/classify-number?number={number}
