from flask import Flask, render_template, request
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# MySQL Database Configuration
db_config = {
    'host': '127.0.0.1',       # Replace with your MySQL host
    'user': 'root',            # Replace with your MySQL username
    'password': '#Priti2002',  # Replace with your MySQL password
    'database': 'mehendi_app'  # Replace with your database name
}

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bridal')
def bridal():
    return render_template('bridal.html')

@app.route('/traditional')
def traditional():
    return render_template('traditional.html')

@app.route('/arabic')
def arabic():
    return render_template('arabic.html')

@app.route('/customized')
def customized():
    return render_template('customized.html')

@app.route('/festive')
def festive():
    return render_template('festive.html')

@app.route('/explore')
def explore():
    return render_template('explore.html')

# Contact Form Submission
@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Save to MySQL database
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO contacts (name, email, message, created_at)
            VALUES (%s, %s, %s, %s)
        """, (name, email, message, datetime.now()))
        conn.commit()
        cursor.close()
        conn.close()
        return {"status": "success", "message": "Message saved successfully!"}
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return {"status": "error", "message": "Failed to save the message. Please try again later."}

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)