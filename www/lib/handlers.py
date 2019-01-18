#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Haojie'

' url handlers '

import re, time, json, logging, hashlib, base64, asyncio

from lib.coroweb import get, post
from lib.apis import Page, APIValueError, APIResourceNotFoundError

from control.home import Home

def get_page_index(page_str):
    p = 1
    try:
        p = int(page_str)
    except ValueError as e:
        pass
    if p < 1:
        p = 1
    return p

@get('/')
async def index(*, page='1'):

	home = Home()

	page_index = get_page_index(page)
	num  = await home.list()
	page = Page(num)

	return {
        '__template__': 'index.html',
        'page': page,
        'blogs': [{
            'name': '测试',
            'summary': '这是一条测试',
            'created_at': time.time()
        }],
    }
