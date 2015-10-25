import subprocess
import sys
import os 
import urllib
import re
import string
import bitshuffle
import random



tag = ""

proc = subprocess.Popen(['sh','./curl.sh'], stdout=subprocess.PIPE)
result = proc.stdout.read()

tokens = result.split()
lengthTokens = len(tokens)
storeToken = False

#Obtain Tags
tagsArray = []
for index in range(0,lengthTokens-1):
	if "[[\"" in tokens[index]:
		storeToken = True
		tagsArray.append(tokens[index])
	elif "\"]]" in tokens[index]:
		storeToken = False
	elif (storeToken):
		tagsArray.append(tokens[index])
	#pass

#Remove all punct and concat

exclude = set(string.punctuation)

concatenated = ''.join(tag for tag in tagsArray if tag not in exclude)
#HACKWADDAp
concatenated = ''.join(ch for ch in concatenated if ch not in exclude)
#you now have the thinggy 

code = "01234567"
code = "".join(random.sample(code, len(code)))

encryptedKey = bitshuffle.encrypt(code ,concatenated)

print encryptedKey


# curl -X POST -d "grant_type=client_credentials" https://SMfnPwPNge6JZMVo4W6T2W8aNkt8YA8nQRlflZm4:Z13dYXRSTWi1V_LRFAPErorrdSSXs84zrLOHxWen@api.clarifai.com/v1/token/

# curl -H "Authorization: Bearer UQneEQYwVQ1RCogfr0PKieXhzfwO0R" https://api.clarifai.com/v1/tag/?url=http://www.clarifai.com/img/metro-north.jpg