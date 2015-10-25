import urllib2
data = 
url = "https://api.clarifai.com/v1/tag/?url=http://i.stack.imgur.com/wzjnO.gif"
req = urllib2.Request(url,data)



import subprocess
import os
import sys



subprocess.Popen(
    'curl',
    '-H',
    '"Authorization: Bearer UQneEQYwVQ1RCogfr0PKieXhzfwO0R"',
    'https://api.clarifai.com/v1/tag/?url=http://i.stack.imgur.com/wzjnO.gif',
    shell = True
	)
tmp = proc.stdout.read()

# proc = subprocess.Popen('ls', stdout=subprocess.PIPE) tmp = proc.stdout.read()

