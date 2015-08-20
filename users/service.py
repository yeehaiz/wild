# coding: utf-8

from users import models
from helpers import utils

def user_info(request):
    return {
        'admin': request.session.get('admin', 0),
        'id': request.session.get('uid', 0),
        'name': request.session.get('username', ''),
        'mobile': request.session.get('mobile', ''),
    }

def get_frequent_members(user_id):
    return [{
        'id': fm.id,
        'name': fm.name,
        'mobile': fm.mobile,
        'cert_type': fm.cert_type,
        'cert': fm.cert,
        'sex': fm.sex,
        'birthday': utils.df(fm.birthday),

    } for fm in models.FrequentMember \
                      .objects.filter(user_id=user_id)]



def save_frequent_members(user, persons):
    for p in persons:
        if models.FrequentMember.objects.filter(name=p['name'], user_id=user.id).count() == 0:
            fm = models.FrequentMember(
                user = user,
                name = p['name'],
                mobile = p['mobile'],
                cert_type = p['cert_type'],
                cert = p['cert'],
                sex = p['sex'],
                birthday = p['birthday']
            )
            fm.save()
