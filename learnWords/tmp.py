import re
import os
import sys
import time
import random

def put(s):
    sys.stdout.write(s)
    sys.stdout.flush()
    
def blit(s):
    for word in s.split():
        put(word + ' ')
        time.sleep(0.05)
    
def ppr(aString, lineLen):
    start = 0
    end = 0
    
    while True:

        if end + lineLen  > len(aString) - 1:
            put('  ')
            blit(aString[start:])
            break

        end = aString.rfind(' ', start, start + lineLen)

        put('  ')
        blit(aString[start:end])
        put('\n')
        start = end + 1
        
class txtObj(object):
    def __init__(self, txt):
        self.text = txt
        
    def blit(self):
        ppr(self.text, 78)

def playtext(fp):

    # Open file and split into groups
    fp = open(fp)
    
    groups = re.split("\n{2,9}", fp.read()) # groups = fp.read().split("\n\n")

    groups.pop(0)
    # random.shuffle(groups)
    
    fp.close()

    # Play Every group (group split into lines)

    for group in groups:
    
        os.system("cls")
        print '- ' * 39 + '\n'  # - - - - - Seperate line - - - - - - - 
    
        lines = group.split("\n")
    
        # For every line, play it.
        for line in lines:
            x = txtObj(line)
            x.blit()
            time.sleep(4.5 + 0.2 * len(line))
            print '\n'        
            
def Run():
    while True:
        try:
            playtext("C:/learn/words.txt")
        except Exception, e:
            print e

if __name__ == '__main__':
    Run()
