#!/usr/bin/env bash 

echo "Running Script in "
pwd
cd ../
ls
mkdir -p docs
cp prism/prism.js prism.js
cp prism/prism.css prism.css
# pwd
# cd ../
# pwd
for f in *.js
 do
   filename="${f##*/}" 
 echo ${filename}        
         echo "moving files..."
         cp "${f}" docs/
done
for f1 in *.css 
 do
   filename2="${f1##*/}" 
 echo ${filename2}        
      if [[ "${f1}" == *c* ]]
         then 
         echo "moving files..."
         cp "${f1}" docs/
       fi
done

cp -R chapters docs/
#cp -R Images docs/
cp -R ceng4AN-images docs/
cp -R images docs/
python scripts/code.py
#cp -R tutorials docs/