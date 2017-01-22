#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-06-09

@author: zw
'''

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from mydecorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
import json
from django.http import HttpResponse
import logging
import random
import traceback
import datetime
import json
import copy
from config import global_conf
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from util.fields_validation import _valid_fields, _fields_comment

logger = logging.getLogger('default')


@login_required
def field_list(request):
    if request.method == 'GET':
        for k in _valid_fields:
            _valid_fields[k]['name'] = _fields_comment[k]
            for k1 in _valid_fields[k]['properties']:
                _valid_fields[k]['properties'][k1]['name'] = _fields_comment[k1]

        return JsonResponse(_valid_fields, safe = False)
