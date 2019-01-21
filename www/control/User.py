#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.control import control
from service.user import user
from lib.models import User, Comment, Blog, next_id
    
class User(control):

	def __init__(self, name='user'):
		super(User, self).__init__()
		self.name = name
		
	def do(self):
		
		print('user do')