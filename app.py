from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Amsterdam, The Netherlands',
    'salary': 'Rs. 15,000,000'
  },
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Amsterdam, The Netherlands',
    'salary': 'Rs. 15,000,000'
  },
  {
      'id': 1,
      'title': 'Data Analyst',
      'location': 'Amsterdam, The Netherlands',
      'salary': 'Rs. 15,000,000'
    }
]

@app.route("/")
def hello_world():
  return  render_template('home.html', 
                          jobs=JOBS)

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)



  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  
