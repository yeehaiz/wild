def user_info(request):
    return {
        'admin': request.session.get('admin', 0),
        'id': request.session.get('uid', 0),
        'name': request.session.get('username', ''),
    }
