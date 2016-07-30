from django.shortcuts import render,render_to_response
from django.http import HttpResponse
import os
import subprocess

# Create your views here.
# Define commands
commands = {
            'hello':'/Users/jcc/PycharmProjects/test_shell/web/hello.sh',
           'hostname':'/Users/jcc/PycharmProjects/test_shell/web/hostname.sh'
          }

def checkurl(request):
    if 'id' in request.GET:
        p_hello=os.popen(commands['hello'])
        p_hostname = os.popen(commands['hostname'])
        a1=p_hello.read()
        a2=p_hostname.read()
        a={'hello':a1,'hostname':a2}
    return render(request,'b.html',locals())
