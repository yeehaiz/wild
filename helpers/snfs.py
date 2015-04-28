'''
single node file system
'''

from django.conf import settings
import hashlib
import os



def save_request_file(file):
    '''
    upload file, return sub url
    '''
    extname = _get_ext_name(file.name)

    hashmd5 = hashlib.md5()
    for chunk in file.chunks():
        hashmd5.update(chunk)

    strmd5 = hashmd5.hexdigest()
    filepath_tuple = _get_filepath_tuple(strmd5, extname)

    fileurl = settings.SNFS_URL + '/'.join(filepath_tuple)
    filepath = apply(os.path.join, (settings.SNFS_DIR, ) + filepath_tuple)

    # file exists, just return
    if os.path.exists(filepath):
        return fileurl

    with open(filepath, 'wb') as f_handler:
        for chunk in file.chunks():
            f_handler.write(chunk)

    return fileurl



def folder_init():
    '''
    create directories for snfs
    '''
    for i in range(100):
        i_str = '%02d' % i
        i_path = os.path.join(settings.SNFS_DIR, i_str)
        if not os.path.exists(i_path):
            os.mkdir(i_path)

        for j in range(100):
            j_str = '%02d' % j
            j_path = os.path.join(i_path, j_str)
            if not os.path.exists(j_path):
                os.mkdir(j_path)


def _get_filepath_tuple(strmd5, extname):
    intmd5 = int(strmd5, 16)
    dir_a = '%02d' % (intmd5 % 99)
    dir_b = '%02d' % ((intmd5 / 99) % 99)
    return (dir_a, dir_b, strmd5 + extname.lower())


def _get_ext_name(filename):
    i = filename.rfind('.')
    if i<0:
        return ''
    return filename[i:]
