#!/usr/bin/env bash

. ~/.profile
. $RC_DIR/python.rc
#set -x
echo $PATH
which pyenv
if test 0 -eq $? -a -f .python-version; then
  pyenv activate $(cat .python-version)
fi
#set +x

bump2version --verbose --commit --tag patch
