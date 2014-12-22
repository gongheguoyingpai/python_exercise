# -*- coding: utf-8 -*-

import os
import sys
import shutil
from contextlib import nested

def is_utf8_with_bom(chars):
    bom_chars = [0xEF, 0xBB, 0xBF]
    for ch, bom_ch in zip(chars, bom_chars):
        if ord(ch) != bom_ch:
            return False
    return True

def trans_utf8_withbom_to_utf8(filepath):
    if not os.path.exists(filepath) or \
       not os.path.isfile(filepath):
        print "%s is not exists or not a file!"
        sys.exit(1)
    with nested(open(filepath, 'rb'), open(filepath + '.bak', 'wb')) as (in_f, out_f):
        content = in_f.read()
        head_chars = content[0:3] if content and len(content) >= 3 else ""
        if is_utf8_with_bom(head_chars):
            content = content[3:]
        out_f.write(content)
    shutil.move(filepath+".bak", filepath)
 
def main():
    filepath = raw_input("file path:") 
    trans_utf8_withbom_to_utf8(filepath)
    
if __name__ == "__main__":
    main()
    