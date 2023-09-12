from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Index
@app.route('/')
def index():
    result_list=""
    return render_template('index.html',expenses=result_list)

# Add Expense
@app.route('/add', methods=['POST'])
def add_expense():
    return redirect(url_for('index'))

# Edit Expense
@app.route('/edit/<expense_id>', methods=['GET', 'POST', 'PUT'])
def edit_expense(expense_id):
    return redirect(url_for('index'))

# Delete Expense
@app.route('/delete/<expense_id>', methods=['GET', 'POST'])
def delete_expense(expense_id):
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')