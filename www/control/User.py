#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.control import control
from service.user import user
    
class User(control):

	def __init__(self, name='user'):
		super(User, self).__init__()
		self.name = name
		
	def do(self):
		print('user do')
		_user = user()
		_user.do()
		