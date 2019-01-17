#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class base(object):
	"""docstring for base"""
	def __init__(self, arg="base"):
		super(base, self).__init__()
		self.arg = arg

	def do(self):
		print('base')
