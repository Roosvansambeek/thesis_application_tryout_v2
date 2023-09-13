from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
    })

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = []
        for row in result.all():
            row_dict = row._asdict()
            jobs.append(row_dict)
        return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM jobs WHERE id = :val"),
            {"val": id}
        )
        row = result.fetchone()  # Use fetchone to get a single row
        if row is None:
            return None
        else:
            return row._asdict()  # Convert the single row to a dictionary

def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url) VALUES (:job_id, :full_name, :email, :linkedin_url)")
        conn.execute(query,
                     job_id=job_id,
                     full_name=data['full_name'],  # Corrected variable name here
                     email=data['email'],  # Corrected variable name here
                     linkedin_url=data['linkedin_url'])  # Corrected variable name here
