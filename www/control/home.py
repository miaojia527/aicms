#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'HaoJie Li'

from lib.control import control
from lib.models import User, Comment, Blog, next_id
from lib.apis import Page, APIValueError, APIResourceNotFoundError

class Home(control):
	"""docstring for Home"""
	def __init__(self, arg={}):
		super(Home, self).__init__()
		self.arg = arg

	async def list(self):
		num = await Blog.findNumber('count(id)')
		page = Page(num)
		if num == 0:
			blogs = []
		else:
			blogs = await Blog.findAll(orderBy='created_at desc', limit=(page.offset, page.limit))
		return {
			"page":page,
			"blogs":blogs
		}