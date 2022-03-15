from fastapi import Depends, status, HTTPException, APIRouter

from typing import List

from sqlalchemy.orm import Session
from db.database import get_db

import models.orders as model
import schemas.orders as schema

router = APIRouter(
    prefix = '/api/orders',
    tags=['Orders']
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schema.Orders)
def create_users(order: schema.Orders, db: Session = Depends(get_db)): 
    try:
        new_order = model.Orders(
            id = order.id,
            userId = order.user_id,
            orderDate = order.orderDate,
            subtotal = order.subtotal,
            shipping = order.shipping
        )  
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
        return new_order
    except Exception:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Order already exists')

@router.get('/',  response_model=List[schema.Orders])
def get_all_orders(db: Session = Depends(get_db)):
    order = db.query(model.Orders).all()
    if not order:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Could not find orders')
    return order

@router.get('/{order_id}', response_model=schema.Orders)
def get_order(order_id, db: Session = Depends(get_db)):
    newOrder = db.query(model.Orders).filter(model.Orders.id == order_id).first()
    if not newOrder:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with order id: {newOrder}')
    return newOrder

# @router.put('/{order_id}', status_code=status.HTTP_202_ACCEPTED)
# def update_order(order_id, user: schema.User, db: Session = Depends(get_db)):
#     order = db.query(model.Orders).filter(model.Orders.id == order_id).update({
#         'id': order.id,
#         'userId': order.userId,
#         'orderDate': order.orderDate,
#         'subtotal': order.subtotal,
#         'shipping': order.shipping
#     })
#     if not order:
#         raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with order: {order_id}')
#     db.commit()
#     return {'detail': f'Update user {order}'}

@router.delete('/')
def delete_order(order_id, db: Session = Depends(get_db)):
    order = db.query(model.Orders).filter(model.Orders.id == order_id).first()
    if not order:
        raise HTTPException(status.HTTP_204_NO_CONTENT, f'No query found with username: {order_id}')
    db.delete(order)
    db.commit()
    return {'detail': f'Deleted user {order_id}'}