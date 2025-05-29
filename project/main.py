from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database
from .auth import get_current_user


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/orders/")
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    order_db = crud.create_order(db, customer_id=user_id, order_data=order)
    return {"order_id": order_db.id, "status": order_db.status, "created_at": order_db.created_at}


@app.get("/orders/{order_id}/status")
def get_order_status(order_id: int, db: Session = Depends(get_db)):
    # Lógica para obtener el estado del pedido
    return {"order_id": order_id, "status": "Enviado"}

@app.put("/orders/{order_id}/status")
def update_order_status(order_id: int, status_update: schemas.StatusUpdate, db: Session = Depends(get_db)):
    # Lógica para actualizar el estado
    return {"order_id": order_id, "status": status_update.status, "updated_at": "2025-03-09T14:00:00Z"}

@app.get("/orders/")
def list_orders(db: Session = Depends(get_db)):
    # Lógica para listar pedidos del cliente autenticado
    return [
        {"order_id": 456, "status": "Entregado", "created_at": "2025-03-09T12:00:00Z"},
        {"order_id": 789, "status": "Pendiente", "created_at": "2025-03-10T15:30:00Z"}
    ]
