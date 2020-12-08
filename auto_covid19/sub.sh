#!/bin/sh
source /home/wukang/ENVIRONMENT/anaconda3/bin/activate base
echo "activate base"
python /home/wukang/auto_covid19/auto_submission.py > /home/wukang/auto_covid19/info.log 2>&1
echo "finished"
