from app import db


class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    phone = db.Column(db.String(10))

    def __repr__(self):
        return f'Customer: {email}'

    def to_json(self):
        json_customer = {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone
        }
        return json_customer

    @staticmethod
    def from_json(json_customer):
        email = json_customer.get('email')
        first_name = json_customer.get('first_name')
        last_name = json_customer.get('last_name')
        password = json_customer.get('phone')
        phone = json_customer.get('phone')

        return Customer(email=email,
                        first_name=first_name,
                        last_name=last_name,
                        street_address=street_address,
                        city=city,
                        state=state,
                        zip_code=zip_code,
                        phone=phone
                        )
