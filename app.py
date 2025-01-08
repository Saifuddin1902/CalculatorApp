from flask import Flask, render_template, request

app = Flask(__name__)

# Route for displaying the calculator
@app.route('/')
def index():
    return render_template('index.html')

# Route for performing the calculation
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = 'Error: Division by zero'
        else:
            result = 'Invalid operation'

    except ValueError:
        result = 'Error: Invalid input'

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
