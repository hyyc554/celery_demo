from __future__ import absolute_import, unicode_literals

from django.shortcuts import render

# Create your views here.

import json

from django.http import HttpResponse
# Create your views here.
from app01.tasks import add,fence


def index(request):
    print('1 + 1 = ?')
    r = add.delay(1, 1)
    # b = fence.delay()
    # print(b)
    print('r.get() = %s ' % r.get())
    resp = {'errorcode': 100, 'detail': 'Get success'}
    return HttpResponse(json.dumps(resp), content_type="application/json")
