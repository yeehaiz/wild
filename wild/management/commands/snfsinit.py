# coding: utf-8

'''
创建snfs目录
'''

from django.core.management.base import BaseCommand, CommandError
from helpers import snfs

class Command(BaseCommand):
    def handle(self, *args, **option):
        snfs.folder_init()
        print "success!"
