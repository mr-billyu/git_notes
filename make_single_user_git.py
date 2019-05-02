#!/usr/bin/env python3

import subprocess

# Create HTML with Code Highlighting and Sidebar
cmd = 'pandoc -o /home/pi/Desktop/single_user_git.html single_user_git.md -s --self-contained --toc -c /home/pi/Applications/Markdown/sidebar.css --template=/home/pi/Applications/Markdown/toc.template'
cmd = cmd.split()
results = subprocess.check_output(cmd)
print(str(results, encoding='UTF-8'))

