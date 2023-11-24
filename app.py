from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Analista de dados',
    'location': 'Sao Paulo',
    'salary': 'R$ 5,000'
}, {
    'id': 2,
    'title': 'Front-end',
    'location': 'Sorocaba',
    'salary': 'R$ 7,000'
}, {
    'id': 3,
    'title': 'Back-end',
    'location': 'Assis',
    'salary': 'R$ 8,000',
}, {
    'id': 4,
    'title': 'Full-Stack',
    'location': 'Londrina',
    'salary': 'R$ 12,000',
}]


@app.route("/")
def hello_word():
  return render_template('home.html', jobs=JOBS, company_name='Studies')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
