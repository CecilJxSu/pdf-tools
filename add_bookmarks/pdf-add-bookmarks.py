#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import toml
from PyPDF2 import PdfFileWriter, PdfFileReader

def add_bookmarks(output, parent, bookmarks):
    for b in bookmarks:
        p = output.addBookmark(b['name'], b['page'] - 1, parent)
        if 'children' in b:
            add_bookmarks(output, p, b['children'])

def main():
    # get bookmarks config
    bookmarks = toml.load(sys.argv[2])['bookmarks']
    # create in, out stream
    input = PdfFileReader(open(sys.argv[1], 'rb'))
    output = PdfFileWriter()

    pages = input.getNumPages()

    for i in range(pages):
        output.addPage(input.getPage(i))

    add_bookmarks(output, None, bookmarks)

    output.write(open(sys.argv[3], 'wb'))

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: pdf-add-bookmars.py <pdf_file> <bookmarks_config_file> <out_file>')
        exit(1)
    main()
