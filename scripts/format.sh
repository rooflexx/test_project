#!/bin/bash -e
set -x

black test_project config
isort test_project config
