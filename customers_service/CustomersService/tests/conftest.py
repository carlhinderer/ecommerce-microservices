import pytest

from app import create_app, db


@pytest.fixture(scope='session')
def app():
    app = create_app('testing')

    # Other setup here    
    app.app_context().push()
    db.create_all()

    yield app

    # Cleanup here
    db.drop_all()


@pytest.fixture(scope='session')
def client(app):
    return app.test_client()


@pytest.fixture(scope='session')
def runner(app):
    return app.test_cli_runner()
