from app import ma


class StuffStructure(ma.Schema):
    class Meta:
        fields = ('id', 'price', 'amount', 'name')
