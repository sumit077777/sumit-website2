from flask import Flask, render_template, jsonify, request
from database import engine, add_contact_to_db
from sqlalchemy import text

app = Flask(__name__)


def load_projects_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from projects"))
    projects = []
    for row in result.all():
      projects.append(row._asdict())
  return projects


@app.route("/")
def hello_world():
  return render_template('home.html')


@app.route("/projects")
def projects_page():
  projects = load_projects_from_db()
  return render_template('projects.html', jobs=projects)


@app.route("/contact")
def contact_page():
  return render_template('contact.html')


@app.route("/resume")
def resume_page():
  return render_template('resume.html')


@app.route("/api/projects")
def list_jobs():
  return jsonify(load_projects_from_db())


@app.route("/contact/submissions", methods=['post'])
def apply_to_job():
  data = request.form
  print(data)
  add_contact_to_db(data)
  return render_template('submitted.html', application=data)


def load_blogs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from blogs"))
    blogs = []
    for row in result.all():
      blogs.append(row._asdict())
  return blogs


@app.route("/blogs")
def blogs_page():
  blogs = load_blogs_from_db()
  return render_template('blog.html', blogs=blogs)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
