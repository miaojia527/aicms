#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class user(object):
	"""docstring for user"""
	def __init__(self, arg="service"):
		super(user, self).__init__()
		self.arg = arg

	def do(self):
		print('service')
		