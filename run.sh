#!/usr/bin/env bash

rm -rf ./files/*
wget "https://en.wikipedia.org/wiki/Main_Page/" -re robots=off --follow-tags a -nd -U "Security Testing" -P files &
WGETPID=$!
sleep 10
kill $WGETPID

python3 markov.py
