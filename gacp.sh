#! /bin/bash

git add . || echo "nothing to add"
git commit -m "$1"
git push
