from sqlalchemy import create_engine, text

engine = create_engine(
  "mysql+pymysql://cgjdzsqwwfyfhsxuzynk:pscale_pw_lKB4MzUEQY9ppSnMY28j0vPUyEPgBEBOGH5wClpXza7@aws.connect.psdb.cloud/sumit?charset=utf8mb4",
  connect_args={"ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
  }},
  pool_pre_ping=True)
with engine.connect() as conn:
  result = conn.execute(text("select * from projects"))
  projects = []
for u in result.all():
  projects.append(u._asdict())
print(projects)


def add_contact_to_db(data):
  with engine.connect() as conn:
    query = text(
      "INSERT INTO contact(first_name, last_name, email, organization_name,additional_info) VALUES (:first_name, :last_name, :email, :organization_name, :additional_info)"
    )

    conn.execute(
      query, {
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'email': data['email'],
        'organization_name': data['organization_name'],
        'additional_info': data['additional_info']
      })
