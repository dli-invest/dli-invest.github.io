#!/bin/bash
# Assume running in root
# Go to book directory
cd ibook/_build/html
dir=$(pwd)
for html in $(find $dir -name "*.html")
  do
    echo $html
    sed -i '7i <script data-ad-client="ca-pub-2479144310234386" async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>' $html
  done

cd ../../../