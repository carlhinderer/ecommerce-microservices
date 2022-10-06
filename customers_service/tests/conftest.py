import pytest

from application.app import create_app, db


@pytest.fixture(scope='session')
def app():
    app = create_app('testing')
    return app


@pytest.fixture(scope='session')
def database(app):
    # Other setup here    
    with app.app_context():
        db.create_all()
        yield db
        db.drop_all()


@pytest.fixture(scope='session')
def client(app):
    return app.test_client()


@pytest.fixture(scope='session')
def runner(app):
    return app.test_cli_runner()
