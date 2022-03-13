from fastapi import Depends, status, HTTPException, APIRouter

from typing import List

from sqlalchemy.orm import Session
from db.database import get_db

import models, schemas

router = APIRouter(
    prefix = '/api/orders',
    tags=['Orders']
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.Order)
def create_users(order: schemas.Order, db: Session = Depends(get_db)): 
    try:
        new_order = models.Orders(
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

@router.get('/',  response_model=List[schemas.Order])
def get_all_orders(db: Session = Depends(get_db)):
    order = db.query(models.Orders).all()
    if not order:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Could not find orders')
    return order

@router.get('/{order_id}', response_model=schemas.ShowUser)
def get_order(order_id, db: Session = Depends(get_db)):
    newOrder = db.query(models.Orders).filter(models.Orders.id == order_id).first()
    if not newOrder:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with order id: {newOrder}')
    return newOrder

@router.put('/{order_id}', status_code=status.HTTP_202_ACCEPTED)
def update_order(order_id, user: schemas.User, db: Session = Depends(get_db)):
    order = db.query(models.Orders).filter(models.Orders.id == order_id).update({
        'id': order.id,
        'userId': order.userId,
        'orderDate': order.orderDate,
        'subtotal': order.subtotal,
        'shipping': order.shipping
    })
    if not order:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with order: {order_id}')
    db.commit()
    return {'detail': f'Update user {order}'}

@router.delete('/')
def delete_order(order_id, db: Session = Depends(get_db)):
    order = db.query(models.Orders).filter(models.Orders.id == order_id).first()
    if not order:
        raise HTTPException(status.HTTP_204_NO_CONTENT, f'No query found with username: {order_id}')
    db.delete(order)
    db.commit()
    return {'detail': f'Deleted user {order_id}'}