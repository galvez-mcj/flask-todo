from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create the app
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# Create the extension
with app.app_context():
    db = SQLAlchemy(app)

# Create database model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

##################################################################
# MAIN APP
##################################################################
@app.route("/", methods=["POST", "GET"])
def index():

    if request.method == "POST":
        # Get the task from the form input
        task_content = request.form['task']
        new_task = Todo(content=task_content)

        try:
            # Adds the new task to the database
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except:
            return 'There was an issue adding the new task...'
        
    else:
        # Returns all the tasks
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)

##################################################################
# DELETING A TASK
##################################################################
@app.route("/delete/<int:id>")
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        # Deletes task from the database
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect("/")
    except:
        return 'There was an issue deleting the task. Try again later.'


##################################################################
# UPDATING A TASK
##################################################################
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    task = Todo.query.get_or_404(id)
    
    if request.method == 'POST':
        task.content = request.form['task']

        try:
            db.session.commit()
            return redirect("/")
        except:
            return 'There was a problem updating the task. Try again later.'
        
    else:
        return render_template('update.html', task=task)



# Run the app
if __name__ == "__main__":
    app.run(debug=True)
