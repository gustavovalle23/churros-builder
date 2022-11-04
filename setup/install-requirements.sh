#! /bin/bash

#!/bin/sh
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 ../part-2.py
rm install-requirements.sh