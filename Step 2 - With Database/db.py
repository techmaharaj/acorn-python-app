import psycopg2
import os

DB_HOST = os.getenv("DB_HOST", "db")
DB_DATABASE = os.getenv("DB_DATABASE", "acorn-devspace")
DB_USER = os.getenv("DB_USER", "acorn-devspace")
DB_PASSWORD = os.getenv("DB_PASSWORD", "acorn-devspace")
print("DB_PASSWORD: ", DB_PASSWORD)

def new_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_DATABASE,
        user=DB_USER,
        password=DB_PASSWORD,
    )
    return conn

## List Expenses
def list_expenses():
    conn = new_connection()
    cur=conn.cursor()
    cur.execute("SELECT * FROM expenses")
    res=cur.fetchall()
    
    # Convert the result to a list of dictionaries
    result_list = []
    for row in res:
        result_list.append({'_id' : row[0], 'category' : row[1], 'price' : row[2]})

    conn.close()
    return result_list

## Insert Expenses
def insert_expenses(expense, cost):
    try:
        conn = new_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO expenses (expense, cost) VALUES (%s, %s) RETURNING id"
        cursor.execute(sql, (expense, cost))
        inserted_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        return f"Expense and cost (ID: {inserted_id}) inserted successfully."
    except (Exception, psycopg2.DatabaseError) as error:
        return f"Error: {error}"

## Update Expenses
def update_expenses(expense_id, new_expense, new_cost):
    try:
        conn = new_connection()
        cursor = conn.cursor()
        sql = "UPDATE expenses SET expense = %s, cost = %s WHERE id = %s"
        cursor.execute(sql, (new_expense, new_cost, expense_id))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except (Exception, psycopg2.DatabaseError) as error:
        return False
    
## Delete Expenses
def delete_expenses(expense_id):
    try:
        conn = new_connection()
        cursor = conn.cursor()
        sql = "DELETE FROM expenses WHERE id = %s"
        cursor.execute(sql, (expense_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except (Exception, psycopg2.DatabaseError) as error:
        return "Error deleting expense."