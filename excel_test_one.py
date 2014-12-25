# -*- coding: utf-8 -*-

import os
import sys
import json
import xlwt

def read_file(file_path):
    if not os.path.exists(file_path) or \
       not os.path.isfile(file_path):
        print '%s is not exist or not a file!' % file_path
        sys.exit(1)
        
    with open(file_path, 'rb') as f:
        return f.read()
        
def trans_to_python_struct(content):
    return json.JSONDecoder().decode(content)

def get_data(file_path):
    content = read_file(file_path)
    data = trans_to_python_struct(content)
    if isinstance(data, dict):
        data = sorted(data.iteritems(), key=lambda d: d[0])
    return data
    
def write_data_one(sheet, data):
    row = 0
    for key, person in data:
        col = 0
        for val in person:
            sheet.write(row, col, val)
            col += 1
        row += 1
        
def write_data_two(sheet, data):
    row = 0
    for key, city in data:
        sheet.write(row, 0, key)
        sheet.write(row, 1, city)
        row += 1
    
def write_data_three(sheet, data):
    row = 0
    for row_data in data:
        col = 0
        for col_data in row_data:
            sheet.write(row, col, col_data)
            col += 1
        row += 1
        
def write_to_excel(input_file_path, output_file_path):
    data = get_data(input_file_path)
    xls = xlwt.Workbook()
    sheet = xls.add_sheet('students')
    # write_data_one(sheet, data)
    # write_data_two(sheet, data)
    write_data_three(sheet, data)
    xls.save(output_file_path)
    print 'finished!'
    
def main():
    input_file_path = raw_input('input file path?')
    output_file_path = raw_input('output file path?')
    write_to_excel(input_file_path, output_file_path)
    
if __name__ == '__main__':
    main()
    