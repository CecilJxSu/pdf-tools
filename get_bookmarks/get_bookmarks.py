#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import toml
import re
from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.generic import Destination

def get_title(outline):
    return re.sub(r"\x00", "", outline.get("/Title")).strip()

def get_page_number(input, outline):
    return input.getDestinationPageNumber(outline) + 1

def get_bookmarks(input, outline):
    if isinstance(outline, Destination):
        return {
            "name": get_title(outline),
            "page": get_page_number(input, outline)
        }

    children = []
    for one in outline:
        bookmark = get_bookmarks(input, one)
        if isinstance(bookmark, dict):
            children.append(bookmark)
        else:
            children[len(children) - 1]['children'] = bookmark
    return children

def main():
    # create in stream
    input = PdfFileReader(open(sys.argv[1], 'rb'))

    # create bookmarks list
    bookmarks = get_bookmarks(input, input.outlines)

    # write to toml file
    toml.dump({"bookmarks": bookmarks}, open(sys.argv[2], "w"))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: get_bookmarks.py <pdf_file> <out_toml_file>')
        exit(1)
    main()
