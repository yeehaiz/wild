# coding: utf-8

'''
创建snfs目录
'''
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from helpers import snfs

import os

class Command(BaseCommand):
    def handle(self, *args, **option):
        if not os.path.exists(settings.SNFS_DIR):
            os.mkdir(settings.SNFS_DIR)

        snfs.folder_init()
        print "success!"
