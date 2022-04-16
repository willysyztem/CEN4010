@echo off

echo CEN4010 - RESTAPI - BOOKSTORE SETUP

set dir_venv="venv"

IF exist %dir_venv% (
    echo VIRTUAL ENVIRONMENT EXISTS - SKIPPING
) ELSE (
    echo BUILDING VIRTUAL ENVIRONMENT
    CALL python -m venv %dir_venv%)

echo ACTIVATING VIRTUAL ENVIRONMENT
CALL venv\Scripts\activate.bat

echo INSTALLING DEPENDENCIES
pip install -r "D:\CEN4010Main\CEN4010\CEN4010\requirements.txt"

echo RUN UVICORN SERVER
d:
cd "D:\CEN4010Main\CEN4010\CEN4010\app"
uvicorn main:app --reload