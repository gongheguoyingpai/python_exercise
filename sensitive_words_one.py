# -*- coding: utf-8 -*-

import os
import sys
import chardet

def read_file(file_path):
    if not os.path.exists(file_path) or \
       not os.path.isfile(file_path):
        print "%s is not exists or not a file!" % file_path
        sys.exit(1)
        
    with open(file_path, "r") as f:
        content = f.read()
        return content
        
def make_sensitive_wordlist(content):
    words = content.split()
    print words
    return words
    
def contain_sensitive_word(content, words):
    for word in words:
        if content.find(word) != -1:
             return True
    return False
    
def print_user_input(content, words):
    content = content.decode('gbk').encode('utf-8')
    if contain_sensitive_word(content, words):
        print "Freedom"
    else:
        print "Human Rights"
        
def sensitive_words_init(file_path, words):
    content = read_file(file_path)
    words.extend(make_sensitive_wordlist(content))
    
def main():
    file_path = raw_input('sensitive word file path?')
    words = []
    sensitive_words_init(file_path, words)
    while True:
        content = raw_input('what input?(q will quit)')
        content = content.lower()
        if content == 'q':
            break
        print_user_input(content, words)
    print "Finished!"
    
if __name__ == "__main__":
    main()
    