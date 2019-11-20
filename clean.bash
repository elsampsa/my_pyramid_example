#!/bin/bash
rm -rf dist
rm -rf build
rm -rf *.egg-info
rm -f *.deb
# clear docker dirs
rm docker/simple/*.ini
rm docker/simple/*.tar.gz

