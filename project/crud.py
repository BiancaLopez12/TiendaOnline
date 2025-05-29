from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def create_order(db: Session, customer_id: int, order_data: schemas.OrderCreate):
    new_order = models.Order(customer_id=customer_id)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    for item in order_data.products:
        product = get_product(db, item.product_id)
        if not product:
            raise Exception(f"Product {item.product_id} not found")
        order_item = models.OrderItem(
            order_id=new_order.id, product_id=item.product_id, quantity=item.quantity
        )
        db.add(order_item)
    db.commit()
    return new_order

def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()

def update_order_status(db: Session, order: models.Order, status: str):
    order.status = status
    order.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(order)
    return order

def get_orders_by_customer(db: Session, customer_id: int):
    return db.query(models.Order).filter(models.Order.customer_id == customer_id).all()
