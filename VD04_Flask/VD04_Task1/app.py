from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def date_time_now():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return render_template_string("""
        <h1>Текущие дата и время</h1>
        <p>{{ current_time }}</p>
    """, current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)