from sqlalchemy.orm import Session
from project import models, database, auth

db = database.SessionLocal()

# Crear productos
if not db.query(models.Product).all():
    products = [
        models.Product(name="Camiseta", price=20),
        models.Product(name="Pantalón", price=40),
        models.Product(name="Zapatos", price=60),
    ]
    db.add_all(products)
    db.commit()

# Crear cliente demo
if not db.query(models.Customer).filter_by(email="cliente@example.com").first():
    hashed_password = auth.get_password_hash("password123")
    customer = models.Customer(name="Cliente Demo", email="cliente@example.com", hashed_password=hashed_password)
    db.add(customer)
    db.commit()

db.close()
