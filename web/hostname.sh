#!/bin/bash
HOSTNAME=`hostname`
IPADDR=`ifconfig en0 | grep 'inet ' | awk '{print $2}'`
DATE=`date '+%d%M%Y'`
#echo $HOSTNAME
#echo $IPADDR
#echo $DATE
cp /Users/jcc/PycharmProjects/test_shell/web/hello.sh /Users/jcc/PycharmProjects/test_shell/web/hello.sh.$DATE
if [ $? -eq 0 ];then
	#echo "copied"
	echo '/Users/jcc/PycharmProjects/test_shell/web/hello.sh.'$DATE
	exit 0
else
	echo "error"
	exit 1
fi
