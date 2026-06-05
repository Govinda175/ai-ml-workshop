# # from flask import Flask, render_templete

# # app = Flask(__name__)

# # @app.route('/')
# # def home():
# #     return '''

# # <h1> Student Score Prediction </h1>


# # '''



# from flask import Flask, render_template, request

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('index.html')


# @app.route('/about')
# def about():
#     return render_template('about.html')


# @app.route('/test')
# def test():
#     return "<h2>Flask Server Running Successfully!</h2>"


# @app.route('/predict', methods=['POST'])
# def predict():

#     student_id = request.form['student_id']
#     hours_studied = float(request.form['hours_studied'])
#     previous_score = float(request.form['previous_score'])
#     attendance = float(request.form['attendance'])
#     sleep_hours = float(request.form['sleep_hours'])
#     extracurricular = int(request.form['extracurricular'])
#     parent_education = int(request.form['parent_education'])
#     internet_access = int(request.form['internet_access'])

#     # Simple prediction formula
#     predicted_score = (
#         previous_score * 0.5 +
#         hours_studied * 2 +
#         attendance * 0.2 +
#         sleep_hours * 1.5 +
#         extracurricular * 3 +
#         parent_education * 2 +
#         internet_access * 2
#     )

#     predicted_score = min(round(predicted_score, 2), 100)

#     return render_template(
#         'result.html',
#         student_id=student_id,
#         score=predicted_score
#     )


# if __name__ == '__main__':
#     app.run(debug=True)
# app.py - Flask app with templating for UI/UX Notebook

from flask import Flask, render_template

# Create Flask app instance
app = Flask(__name__)

# =====================================================
# DUMMY DATA (Simulating a database)
# In a real app, this would come from a database
# =====================================================

# List of UI/UX topics from your BCA syllabus
topics = [
    {"id": 1, "name": "Fundamentals of UX and UI", "description": "Basic concepts of User Experience and User Interface design", "hours": 4},
    {"id": 2, "name": "UX vs UI", "description": "Differences between UX and UI designers and their roles", "hours": 2},
    {"id": 3, "name": "UX Principles", "description": "Usability, Accessibility, Simplicity", "hours": 3},
    {"id": 4, "name": "Core UX Disciplines", "description": "User research, IA, Interaction design, Visual design", "hours": 5},
    {"id": 5, "name": "User Interfaces Types", "description": "CLI, GUI, VUI, Menu-driven, NLP-based", "hours": 3},
]

# Sample user data for dynamic profile page
users = {
    "priya": {"name": "Priya Sharma", "role": "BCA Student", "batch": "2nd Sem"},
    "ram": {"name": "Ram KC", "role": "UI/UX Learner", "batch": "2nd Sem"},
    "default": {"name": "Guest", "role": "Visitor", "batch": "Unknown"}
}

# =====================================================
# ROUTES (URLs that users can visit)
# =====================================================

@app.route('/')
def home():
    """Homepage - shows welcome message"""
    # render_template() looks for HTML files inside the 'templates' folder
    # We pass the 'title' variable to be used in the template
    return render_template('index.html', title="Home - UI/UX Notebook")

@app.route('/about')
def about():
    """About page - explains this project"""
    return render_template('about.html', title="About - UI/UX Notebook")

@app.route('/user/<username>')
def user_profile(username):
    """Dynamic user profile page"""
    # Get user data if exists, otherwise use 'default'
    user_data = users.get(username, users["default"])
    # Pass user data to the template
    return render_template('user.html', title=f"{user_data['name']}'s Profile", user=user_data, username=username)

@app.route('/topics')
def topics_list():
    """Show all UI/UX topics"""
    # Pass the entire topics list to the template
    return render_template('topics.html', title="Topics - UI/UX Syllabus", topics=topics)

@app.route('/topic/<int:topic_id>')
def topic_detail(topic_id):
    """Show details of a single topic"""
    # Find the topic with matching id
    topic = None
    for t in topics:
        if t["id"] == topic_id:
            topic = t
            break
    
    # If topic not found, show error page (or 404)
    if topic is None:
        return render_template('404.html', title="Topic Not Found"), 404
    
    return render_template('topic_detail.html', title=f"{topic['name']} - UI/UX Notebook", topic=topic)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
    