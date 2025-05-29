from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import enum

class OrderStatus(str, enum.Enum):
    pendiente = "Pendiente"
    enviado = "Enviado"
    entregado = "Entregado"

class ProductBase(BaseModel):
    id: int
    name: str
    price: int

    class Config:
        from_attributes = True

class OrderItemBase(BaseModel):
    product_id: int
    quantity: int

class OrderCreate(BaseModel):
    products: List[OrderItemBase]

class OrderOut(BaseModel):
    order_id: int
    status: OrderStatus
    created_at: datetime

    class Config:
        from_attributes = True

class StatusUpdate(BaseModel):
    status: OrderStatus
