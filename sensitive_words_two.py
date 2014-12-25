# -*- coding: utf-8 -*-

import os
import sys
import chardet


DEFAULT_SIGN = '*'

def read_file(file_path):
    if not os.path.exists(file_path) or \
       not os.path.isfile(file_path):
        print "%s is not exists or not a file!" % file_path
        sys.exit(1)
        
    with open(file_path, "r") as f:
        content = f.read().decode('utf-8')
        return content
        
def make_sensitive_wordlist(content):
    words = content.split()
    return words
    
def contain_sensitive_word(content, words):
    for word in words:
        pos = content.find(word)
        if pos != -1:
             return pos, len(word)
    return len(content), 0
    
def make_replace_word(sign, length):
    return sign * length
    
def print_user_input(content, words):
    content = content.decode('gbk')
    right_content = u""
    start = 0
    content_len = len(content)
    while True:
        uncheck_content = content[start:]
        pos, length = contain_sensitive_word(uncheck_content, words)
        if length:
            replace_content = DEFAULT_SIGN * length
            right_content += uncheck_content[:pos] + replace_content
            start += pos + length
        else:
            right_content += uncheck_content
        if len(right_content) == content_len:
            break
    print right_content.encode('gbk')
    
def print_user_input_one(content, words):
    content = content.decode('gbk')
    content_len = len(content)
    while True:
        pos, length = contain_sensitive_word(content, words)
        if length != 0:
            replace_content = DEFAULT_SIGN * length
            sensitive_word = content[pos:pos+length]
            content = content.replace(sensitive_word, replace_content)
        else:
            break
    print content.encode('gbk')
    
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
        print_user_input_one(content, words)
    print "Finished!"
    
if __name__ == "__main__":
    main()
    