# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# # Sample to-do list
# tasks = [
#     {'id': 1, 'task': 'Complete assignment', 'time': '10:00 AM', 'done': False},
#     {'id': 2, 'task': 'Attend meeting', 'time': '1:00 PM', 'done': True}
# ]

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/manage', methods=['GET', 'POST'])
# def manage_tasks():
#     if request.method == 'POST':
#         # Add a new task
#         task_name = request.form.get('task')
#         task_time = request.form.get('time')
#         task_done = request.form.get('done') == 'on'
#         new_task = {
#             'id': tasks[-1]['id'] + 1 if tasks else 1,
#             'task': task_name,
#             'time': task_time,
#             'done': task_done
#         }
#         tasks.append(new_task)
#         return redirect(url_for('manage_tasks'))
#     return render_template('manage.html', tasks=tasks)

# @app.route('/delete/<int:task_id>')
# def delete_task(task_id):
#     global tasks
#     tasks = [task for task in tasks if task['id'] != task_id]
#     return redirect(url_for('manage_tasks'))

# @app.route('/report')
# def report():
#     completed = [task for task in tasks if task['done']]
#     not_completed = [task for task in tasks if not task['done']]
#     return render_template('report.html', completed=completed, not_completed=not_completed)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, send_file
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = Flask(__name__)

# Sample to-do list
tasks = [
    {'id': 1, 'task': 'Complete assignment', 'time': '10:00 AM', 'done': False},
    {'id': 2, 'task': 'Attend meeting', 'time': '1:00 PM', 'done': True}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/manage', methods=['GET', 'POST'])
def manage_tasks():
    if request.method == 'POST':
        # Add a new task
        task_name = request.form.get('task')
        task_time = request.form.get('time')
        task_done = request.form.get('done') == 'on'
        new_task = {
            'id': tasks[-1]['id'] + 1 if tasks else 1,
            'task': task_name,
            'time': task_time,
            'done': task_done
        }
        tasks.append(new_task)
        return redirect(url_for('manage_tasks'))
    return render_template('manage.html', tasks=tasks)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('manage_tasks'))

@app.route('/report')
def report():
    completed = [task for task in tasks if task['done']]
    not_completed = [task for task in tasks if not task['done']]
    return render_template('report.html', completed=completed, not_completed=not_completed)

# New route to generate and download the PDF report
@app.route('/generate_pdf')
def generate_pdf():
    completed = [task for task in tasks if task['done']]
    not_completed = [task for task in tasks if not task['done']]

    # Create a BytesIO object to hold the PDF data in memory
    buffer = BytesIO()

    # Create a canvas object
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Set title and fonts
    c.setFont("Helvetica", 12)
    c.drawString(30, height - 40, "Task Report")

    # Completed Tasks
    c.drawString(30, height - 60, "Completed Tasks:")
    y_position = height - 80
    for task in completed:
        c.drawString(30, y_position, f"- {task['task']} ({task['time']})")
        y_position -= 20

    # Not Completed Tasks
    y_position -= 30  # Space between sections
    c.drawString(30, y_position, "Not Completed Tasks:")
    y_position -= 20
    for task in not_completed:
        c.drawString(30, y_position, f"- {task['task']} ({task['time']})")
        y_position -= 20

    # Finalize the PDF
    c.save()

    # Get the PDF data from the buffer
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="task_report.pdf", mimetype="application/pdf")

if __name__ == '__main__':
    app.run(debug=True)