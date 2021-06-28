@echo off

set flag=%1
set fn=%2

python -u "[path to setup.py]" %flag% %fn%

