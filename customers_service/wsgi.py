import os

from application.app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


# from application.app import db
# from app.models.customer import Customer

# @app.shell_context_processor
# def make_shell_context():
#     return dict(db=db, Customer=Customer)
