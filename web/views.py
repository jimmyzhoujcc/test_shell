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

#hostinfo=[]
def checkurl(request):
    if 'id' in request.GET:
        p_hello=os.popen(commands['hello'])
        child = subprocess.Popen(['/bin/bash', '-c', '/Users/jcc/PycharmProjects/test_shell/web/hostname.sh'],
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = child.stdout.readlines()
        for line in out:
            print line.strip()
            a1=line.strip()
            #hostinfo.append(line.strip())
        #p_hostname = os.popen(commands['hostname'])
        #a2=p_hostname.read()
        #p1=p_hello.read()
        #hello=p1.strip()
        a=a1
        #a={'Hello return value':hello,'Host info return value':hostinfo}
    return render(request,'b.html',locals())
    #return render(request,'c.html', locals())
