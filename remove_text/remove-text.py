#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
from PyPDF2 import PdfFileWriter, PdfFileReader

def main():
    # create in, out stream
    input = PdfFileReader(open(sys.argv[1], 'rb'))
    output = PdfFileWriter()

    pages = input.getNumPages()

    for i in range(pages):
        pageObj = input.getPage(i)
        del pageObj.get('/Resources').get('/XObject')['/Fm0']
        del pageObj.get('/Resources').get('/XObject')['/Fm1']
        output.addPage(pageObj)

    output.write(open(sys.argv[2], 'wb'))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: remove-text.py <pdf_file> <out_pdf_file>')
        exit(1)
    main()
