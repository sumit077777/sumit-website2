from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengaluru',
  'salary': 1000000
}, {
  'id': 2,
  'title': 'Front End Engineer',
  'location': 'Remote',
  'salary': 1000000
}, {
  'id': 3,
  'title': 'Backend-Engineer',
  'location': 'Noida',
  'salary': 10000
}, {
  'id': 4,
  'title': 'Data scientist',
  'location': 'Bengaluru',
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
