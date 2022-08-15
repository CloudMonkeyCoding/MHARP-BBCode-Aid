# This is meant to allow for you to input a post and a hexcode and it will automatically apply your color code to all spoken parts.

import re

print("Paste Post")
post = input()                  #post imput


#fix " since the curly version from gDocs isn't the same thing ¯\_(ツ)_/¯
find_it = '“'
repl_it = '"'
post = post.replace(find_it, repl_it)

find_it = '”'
repl_it = '"'
post = post.replace(find_it, repl_it)



print('Text Color')
P_Color = ('[color=#' + input() + ']')             #text color input

quotes_list = [m.start() for m in re.finditer('"', post)]

quotes_list.reverse()                           #list of all quotes created



#Quote Start
i=1
while i< len(quotes_list):
    q_start = quotes_list[i]
    post = post[:q_start] + P_Color + post[q_start:]
    i = i + 2


#Repeat of quotes search due to everything shifting during above Quote Start
quotes_list = [m.start() for m in re.finditer('"', post)]
quotes_list.reverse()

#quote End
i=0
while i< len(quotes_list):
    q_end = quotes_list[i]+1
    post = post[:q_end] + '[/color]' + post[q_end:]
    i = i + 2
    



print(post)

"""#turn into a loop later
speak_S = post.find("\"")
speak_E = post.find("\"", speak_S +1)
speak = post[speak_S + 1: speak_E]

print: str(speak)"""
