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
from util.util import *

logger = logging.getLogger('default')


@login_required
def field_list(request):
    if request.method == 'GET':
        return JsonResponse({"field_list":_valid_fields, "fields_comment":_fields_comment}, safe = False)


@login_required
def current_user(request):
    if request.method == 'GET':
        return JsonResponse({"username":request.user.username, "realname":request.user.first_name + request.user.last_name}, safe = False)

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        res = handle_uploaded_file(request.FILES['file'])
        return JsonResponse({"url":res[0], "name":res[1]})
    else:
        return JsonResponse({"error":1}, status=status.HTTP_400_BAD_REQUEST)

