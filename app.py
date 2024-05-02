from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form.get('task')
    tasks.append(task)
    return redirect(url_for('index'))

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_task(index):
    if request.method == 'GET':
        if 0 <= index < len(tasks):
            task = tasks[index]
        else:
            task = None
        return render_template('edit.html', index=index, task=task)
    elif request.method == 'POST':
        new_task = request.form.get('task')
        if 0 <= index < len(tasks):
            tasks[index] = new_task
        return redirect(url_for('index'))

@app.route('/delete/<int:index>', methods=['POST'])
def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
