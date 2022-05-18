#!/usr/bin/env bash
ACCEPTOR_MAIN_LOCAL_PATH="$(pwd)"

export ACCEPTOR_RUN_PLATFORM="remote"
export ACCEPTOR_SELENIUM_URL="http://0.0.0.0:4444/wd/hub"
export ACCEPTOR_MAIN_LOCAL_PATH

export ACCEPTOR_BROWSERS_LIST="chrome,firefox"
