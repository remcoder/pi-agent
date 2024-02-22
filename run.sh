#!/bin/bash


WORK_DIR="/home/pi/agent"
VENV_PATH="$WORK_DIR/agent/bin/activate"
PYTHON="/usr/bin/python"

echo "Running agent - $(date)" >> $WORK_DIR/log.txt

source "$VENV_PATH"

cd $WORK_DIR
(python report.py | python gpt.py | python notify.py) >> $WORK_DIR/agent.log 2>&1

deactivate
