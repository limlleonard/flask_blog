from flaskblog import app, db
from flaskblog.models import Benutzer, Post
from sqlalchemy import inspect

with app.app_context():
    db.create_all()  # Ensures that the tables are created
    # user4=User(username='test3', email='bca@gmail.com', password='wdag')
    # db.session.add(user4)
    db.session.commit() # create tables

    pass
    # print(User.query.all())
    # print(Post.query.all())

with app.app_context():
    inspector = inspect(db.engine)
    table_names = inspector.get_table_names()

    for table_name in table_names:
        print(f"\nContents of table '{table_name}':")