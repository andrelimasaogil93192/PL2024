import re

def mD_to_html(md):

        #Headers
        md = re.sub(r'^# (.*)$',r'<h1>\1<h1>',md,flags=re.MULTILINE)
        md = re.sub(r'^## (.*)$',r'<h2>\1<h2>',md,flags=re.MULTILINE)
        md = re.sub(r'^### (.*)$',r'<h3>\1<h3>',md,flags=re.MULTILINE)

        #Bold
        md = re.sub(r'\*\*(.*?)\*\*',r'<b>\1<b>',md)

        #Italic
        md = re.sub(r'\*(.*?)\*',r'<i>\1<i>',md)

        #Numbered list
        md = re.sub(r'^\d+\. (.*)$', r'<1. li>\1</li>', md, flags=re.MULTILINE)
        md = '<ol>\n' + md + '\n</ol>'

        #Link

        md = re.sub(r'\[(.?)\]\((.*?)\)',r'<a href="\2">\1</a>',md)

        #Imagem

        md =  re.sub(r'!\[(.*?)\]\((.*?)\)',r'<img src="\2" alt="\1"/',md)

        return md


line = input()
md = mD_to_html(line)
print(md)

