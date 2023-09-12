from flask import Flask, render_template, request, redirect, url_for, jsonify
from db import *

app = Flask(__name__)

# Index
@app.route('/')
def index():
    result_list=list_expenses()
    return render_template('index.html',expenses=result_list)

# Add Expense
@app.route('/add', methods=['POST'])
def add_expense():
    expense = request.form.get('category')
    cost = int(request.form.get('price'))
    result = insert_expenses(expense, cost)
    return redirect(url_for('index'))

# Edit Expense
@app.route('/edit/<expense_id>', methods=['GET', 'POST', 'PUT'])
def edit_expense(expense_id):
    if request.method=='POST':
        new_category = request.form.get('new_category')
        new_price = int(request.form.get('new_price'))
        if update_expenses(expense_id, new_category, new_price):
            return redirect(url_for('index'))
        else:
            return "Error updating expense."

# Delete Expense
@app.route('/delete/<expense_id>', methods=['GET', 'POST'])
def delete_expense(expense_id):
    if delete_expenses(expense_id):
        return redirect(url_for('index'))
    else:
        return "Error deleting expense."


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')