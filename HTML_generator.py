'''
Created on 2014-06-27

@author: Emanuel
'''
import webbrowser

def template(title, para):
    f = open('kanye.html', 'w')
    
    content = """<!DOCTYPE html>
<html>
    <head>
        <title>{0}</title>
    </head>
    
    <body>
        <p>{1}</p>
    </body>
</html>
    """.format(title, para)
    
    f.write(content)
    f.close()
    
    webbrowser.open_new_tab('kanye.html')


print """Select an option:
1. Create new html file
2. Edit existing file
"""

choice = int(raw_input(">"))

if choice == 1:
    title = raw_input("Page title: ")
    para = raw_input("Page contents: ")
    template(title, para)
elif choice == 2:
    print "i dont know how to do that yet"