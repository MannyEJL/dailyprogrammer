'''
Created on 2014-06-28

@author: Emanuel

http://www.reddit.com/r/dailyprogrammer/comments/299hvt/6272014_challenge_168_easy_string_index/
'''
import re

def indexer(string_to_index, position):
    #print "looking for {}th word".format(position)
    answer = re.findall("[a-zA-Z0-9]+", string_to_index)
    answer.insert(0,"")
    if 0 < position < len(answer):
        print answer[position],

s = "The lazy cat slept in the sunlight"
s2 = """...You...!!!@!3124131212 Hello have this is a --- 
        string Solved !!...? to test @\n\n\n#!#@#@%$**#$@ 
        Congratz this!!!!!!!!!!!!!!!!one ---Problem\n\n"""
        
#word_index = raw_input("Enter the word positions you wish to find: ").split(" ")
word_index = "12 -1 1 -100 4 1000 9 -1000 16 13 17 15".split(" ")

for i in word_index:
    indexer(s2,int(i))