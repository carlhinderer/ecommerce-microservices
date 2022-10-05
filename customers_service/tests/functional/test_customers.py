import pytest

from app import db
from app.models.customer import Customer



@pytest.fixture()
def customer_fixture():
    # Add customer record
    customer = Customer(first_name='John',
                        last_name='Doe',
                        email='johndoe@gmail.com',
                        password='pw1234',
                        phone='9876543210')

    db.session.add(customer)
    db.session.commit()

    yield

    # Remove customer record
    db.session.delete(customer)
    db.session.commit()


def test_get_customers(client, customer_fixture):
    response = client.get('/api/v1/customers')
    assert response.status_code == 200
