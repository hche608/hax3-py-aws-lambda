#!/usr/bin/env bash

lambda_output_file=/opt/app/build/lambda.zip

set -e

yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm -y
yum update -y
yum install yum-utils -y
yum install -y cpio python3 python3-pip zip
python3 --version
python3 -m venv env
pip3 install --upgrade pip
. env/bin/activate
pip install --no-cache-dir -r requirements/test.txt

mkdir -p build
zip -r9 $lambda_output_file *.py bin
cd env/lib/python3.7/site-packages
zip -r9 $lambda_output_file certifi chardet idna requests decorator.py
