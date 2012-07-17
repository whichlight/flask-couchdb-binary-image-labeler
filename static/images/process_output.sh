#!/bin/bash

#run this script to take the instagram urls and download them into this folder
cat ../../data/output.txt | sort | uniq | grep "insta" > ../../data/images_links.txt;
wget -i ../../data/images_links.txt;
