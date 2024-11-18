"""This code is licensed under the GPL-3.0 license
Written by masajinobe-ef
"""

from fastapi import APIRouter, Depends
from icecream import ic
from ..auth.config import current_user
from .tasks import send_email_report_hello


tasks_router = APIRouter(prefix='/report', tags=['Tasks'])


@tasks_router.get('/email')
def send_email_report(user=Depends(current_user)):
    try:
        send_email_report_hello.delay(user.username)
        return {
            'status': 'Success',
            'data': None,
            'details': 'Email has been sent',
        }
    except Exception as e:
        ic(e)
