@echo off

echo CEN4010 - RESTAPI - BOOKSTORE SETUP

set dir_venv="venv"

IF exist %dir_venv% (
    echo VIRTUAL ENVIRONMENT EXISTS - SKIPPING
) ELSE (
    echo BUILDING VIRTUAL ENVIRONMENT
    CALL python3 -m venv %dir_venv%
)

echo ACTIVATING VIRTUAL ENVIRONMENT
CALL venv\Scripts\activate.bat

echo INSTALLING DEPENDENCIES
pip install -r requirements.txt

echo RUN UVICORN SERVER
uvicorn app\main:app --reload