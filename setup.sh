#!/bin/bash

echo 'CEN4010 - RESTAPI - BOOKSTORE SETUP'

dir_venv="venv"

if [ ! -d dir_venv]
then
    echo "BUILDING VIRTUAL ENVIRONMENT"
    python3 -m venv dir_venv

echo 'ACTIVATING VIRTUAL ENVIRONMENT'
source ./venv/bin/activate

echo 'INSTALLING DEPENDENCIES'
pip install -r requirements.txt

echo 'RUNNING UVICORN SERVER'
uvicorn app/main:app --reload