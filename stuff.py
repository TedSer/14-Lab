from app import db


class Stuff(db.Model):
    __tablename__ = "stuff_ted"  # зміни на назву своєї таблиці
    id = db.Column('id', db.Integer, primary_key=True)
    price = db.Column('price', db.Integer)
    amount = db.Column('amount', db.Integer)
    name = db.Column('name', db.String(20))

    def __str__(self):
        return str("stuff id: " + str(self.id) + "\nprice: " + str(
            self.price) + "\namount: " + str(self.amount) + "\nname: " + str(
            self.name))
