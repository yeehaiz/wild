# coding=utf-8

def get_event_fee(event, persons):
    return event.price * len(persons)

def get_equipment_rent(equipments, equip_rent):
    return sum([ eqpmnt.rent * equip_rent[eqpmnt.id] for   eqpmnt in equipments])
