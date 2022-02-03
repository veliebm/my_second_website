from project import db

from project.models import User

# Create the database and the db tables.
db.create_all()

# Insert.
db.session.add(User("ben", "ben@ben.com", "sekrit"))
db.session.add(User("admin", "admin@admin.com", "admin"))

# Commit the changes.
db.session.commit()
