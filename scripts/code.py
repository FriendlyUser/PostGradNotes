#!/usr/bin/env python
# Run in root
### Adding prism style highlighting in docs
import os
# os.chdir('../')
import sys
print(os.getcwd())
lwarpFiles = []
dir_list =  os.listdir()
for full_file_name in dir_list:
    base_nameTemp, extensionTemp = os.path.splitext(full_file_name)
    if extensionTemp == '.html': # then .pdf file --> convert to image!
        lwarpFiles.append(full_file_name)

import re
directory = 'docs'
if not os.path.exists(directory):
    os.makedirs(directory)
for outputFile in lwarpFiles:      
    try:
        base_nameTemp, extensionTemp = os.path.splitext(outputFile)
        finalOutputName = base_nameTemp + extensionTemp
        htmlFile = open(outputFile ,'r',encoding='utf-8')
        htmlSyntaxFile = open(directory + r'/' +finalOutputName,'w',encoding='utf-8')
    except OSError:
        print('Cannot open files, probably because they are being used. \n')
        pass
    # include prismCss and prismjs in the final html final, consider merging the existing css file with prism.css
    prismCss = r'<link rel="stylesheet" href="prism.css" type="text/css">'
    prismJs  = r'<script src="prism.js" type="text/javascript"> </script>'
    
    # Replace the lwarp <pre class="programlisting" >
    # with something that works for prism
    lwarpCodeSyn = r'<pre class="programlisting">' 
    lwarpCodeVerb = r'<pre class="verbatim">'
    matlab ="language-matlab"
    latex = "language-latex"
    python = "language-python"
    cplusplus = "language-cpp"
    json = "language-json"
    bash = "language-bash"
    yaml = "language-yaml"
    golang = "language-go"
    js = "language-javascript"
    sql = "language-sql"
    # Go through each even entry in replacements and then check if a replacement should happen
    replacementTerms = ["Cpp", cplusplus, "Latex Code", latex, "Python Script", python, 
        "Bash Script", bash,"Matlab Script", matlab,"Yaml File", yaml,
        "JSON Output", json, "Golang", golang, "Javascript Program", js,
        "SQL Query", sql, "spaCy", python]
    prismVerbCodeSyn = r'<pre><code class = "' + latex + r'">'
    prismCodeSyn = r'<pre><code class = "' + cplusplus + r'">'
    
    # Determines if the next pre tag should be changed
    changeNextPre = False
    #replacementLine = ""
    for line in htmlFile:
        # Include prism.js and prism.css after the title in the html document 
        newline = re.sub(r'</title>',r'</title>' + '\n' + prismCss + '\n' + prismJs, line)
        
        # CHange if the next pre tag should be changed, if it is not true already.
        if changeNextPre == False:
            for i in range (0, int(len(replacementTerms)/2)):
                # match only matches from the beginning of the string. Your code works fine if you do pct_re.search(line) instead. See https://stackoverflow.com/questions/17680631/python-regular-expression-not-matching
                pattern = re.compile(replacementTerms[i*2])
                changeNextPre = bool(re.search(pattern,newline))
                #print(r'<p>'+replacementTerms[i*2])
                if changeNextPre:
                    #print("Match Found")
                    replacementLine = r'<pre><code class = "' + replacementTerms[2*i+1] + r'">'
                    #print(replacementTerms)
                    break
        
        ## get code syntax highlighting
        if changeNextPre == False:
            # Assume matlab is being used
            newline = re.sub(lwarpCodeSyn, prismCodeSyn, newline)
        else:
            templine = re.subn(lwarpCodeSyn, replacementLine,newline)
            newline = templine[0]
            # if a match occurs reset changeNextPre to false
            if templine[1] > 0:
                changeNextPre = False
        ## since a new code tag is introduced it must be closed
        newline = re.sub(r'</pre>',r'</code>' + '\n' + r'</pre>' + '\n', newline)
        # account for new problem of <pre class="verbatim" > 
        #newline = re.sub( lwarpCodeVerb,  prismVerbCodeSyn, newline)
        htmlSyntaxFile.write(str(newline))
        #print(newline)
    
    htmlFile.close()
    htmlSyntaxFile.close()
print('Script is Done creating files')