from .exts import db

class Meal(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(),nullable=False)
    price=db.Column(db.Integer,nullable=False)
    description=db.Column(db.Text())


    def __repr__(self):
        return f"<Food {self.name}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls,id):
        return cls.query.get_or_404(id)

    @classmethod
    def get_by_name(cls,name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_meals_descending(cls):
        return cls.query.order_by(cls.id.desc()).all()