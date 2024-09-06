# app.py
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def run_script():
    # Replace this with your actual Python code logic
    result = "Hello, World!"  # Example output from your script
    return render_template_string("<h1>Result of Your Python Code</h1><p>{{ result }}</p>", result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
