#!/bin/bash
ps -ef | grep monitor.py | awk '{print $2}' | while read pid
do
kill -9 $pid
done

cd /home/ubuntu/monitor
nohup python monitor.py &

