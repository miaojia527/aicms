#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'HaoJie Li'

from lib.control import control

class Home(control):
	"""docstring for Home"""
	def __init__(self, arg={}):
		super(Home, self).__init__()
		self.arg = arg

	async def list(self):

		return 10