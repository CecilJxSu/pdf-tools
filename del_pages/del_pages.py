#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
from PyPDF2 import PdfFileWriter, PdfFileReader
from utils import get_bookmarks, add_bookmarks

def minus_pages(page, bookmarks):
    if isinstance(bookmarks, list):
        for i in bookmarks:
            minus_pages(page, i)
        return
    if page <= bookmarks['page']:
        bookmarks['page'] -= 1
        if 'children' in bookmarks:
            minus_pages(page,bookmarks['children'])

def main():
    # create in, out stream
    input = PdfFileReader(open(sys.argv[1], 'rb'))
    output = PdfFileWriter()

    del_pages = sys.argv[2].split(",")

    bookmarks = get_bookmarks(input, input.outlines)

    pages = input.getNumPages()

    deled_pages = []
    for i in range(pages):
        if str(i + 1) in del_pages:
            deled_pages.append(i+1)
            continue
        pageObj = input.getPage(i)
        output.addPage(pageObj)

    deled_pages.sort(reverse=True)

    for i in deled_pages:
        minus_pages(i, bookmarks)

    if isinstance(bookmarks, dict):
        bookmarks = [bookmarks]
    add_bookmarks(output, None, bookmarks)

    output.write(open(sys.argv[3], 'wb'))

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: del_pages.py <pdf_file> <page1,page2,...> <out_pdf_file>')
        exit(1)
    main()
