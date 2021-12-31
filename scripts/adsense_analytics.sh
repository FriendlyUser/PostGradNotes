 #!/usr/bin/env bash 
for f in *.html
 do
   filename="${f##*/}" 
   echo ${filename}
   $REPLACE='<script src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js", "data-ad-client": "ca-pub-2479144310234386" async: true></script>'
   ESCAPED_REPLACE=$(printf '%s\n' "$REPLACE" | sed -e 's/[\/&]/\\&/g')
    sed -i '8i $ESCAPED_REPLACE' $filename

    sed -i '9i \<script async src="https://www.googletagmanager.com/gtag/js?id=G-452Q9YNE0N"></script><script>window.dataLayer = window.dataLayer || [];function gtag(){dataLayer.push(arguments);}gtag("js", new Date());gtag("config","G-452Q9YNE0N");
</script>' $filename
done