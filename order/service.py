# coding=utf-8

import constants
from order.models import Order, OrderMember, OrderEquipment


def get_event_fee(event, persons):
    return event.price * len(persons)

def get_equipment_rent(equipments, equip_rent):
    return sum([ eqpmnt.rent * equip_rent[eqpmnt.id] for   eqpmnt in equipments])

def get_order_status(status):
    return constants.ORDER_STATUS.get(status, '未知')

def equipment_avaliable(equip, start_dt, end_dt):
    oes = equip.orderequipment_set.filter(status=1,
                start_dt__lte=end_dt, end_dt__gte=start_dt)

    num_out = sum(i.number for i in oes)
    if equip.storage > num_out:
        return equip.storage - num_out
    else:
        return 0
