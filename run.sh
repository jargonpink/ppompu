#!/bin/bash

BASEPATH=$( dirname "${BASH_SOURCE[0]}" )
VENVPATH="/Users/esnaute/.virtualenvs/ppomppu"

cd $BASEPATH

source $VENVPATH/bin/activate
$VENVPATH/bin/python $BASEPATH/spider.py
