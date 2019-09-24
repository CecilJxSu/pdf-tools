#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
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

def add_bookmarks(output, parent, bookmarks):
    for b in bookmarks:
        p = output.addBookmark(b['name'], b['page'] - 1, parent)
        if 'children' in b:
            add_bookmarks(output, p, b['children'])
