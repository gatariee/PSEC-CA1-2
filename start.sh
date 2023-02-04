#!/bin/bash

VENV_BIN_PATH="env/bin/activate"
VENV_SCRIPTS_PATH="env/Scripts/activate"

if [ -d "env" ]; then
    if [ -f "$VENV_BIN_PATH" ]; then
        source "$VENV_BIN_PATH"
    elif [ -f "$VENV_SCRIPTS_PATH" ]; then
        source "$VENV_SCRIPTS_PATH"
    else
        echo "Cannot find virtual environment activate script. Aborting."
        exit 1
    fi
    echo "Virtual Environment already exists! Skipping install..."
else
    echo "Starting Virtual Environment..."
    python3 -m venv env
    if [ -f "$VENV_BIN_PATH" ]; then
        source "$VENV_BIN_PATH"
    elif [ -f "$VENV_SCRIPTS_PATH" ]; then
        source "$VENV_SCRIPTS_PATH"
    else
        echo "Cannot find virtual environment activate script. Aborting."
        exit 1
    fi
    echo "Installing Python Dependencies..."
    pip install -r requirements.txt
fi
