import pytest

from application.models.customer import Customer



@pytest.fixture()
def customer_fixture(database):
    # Add customer record
    customer = Customer(first_name='John',
                        last_name='Doe',
                        email='johndoe@gmail.com',
                        password='pw1234',
                        phone='9876543210')

    database.session.add(customer)
    database.session.commit()

    yield

    # Remove customer record
    database.session.delete(customer)
    database.session.commit()


def test_get_customers(client, customer_fixture):
    response = client.get('/api/v1/customers')
    assert response.status_code == 200
