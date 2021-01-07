#!/usr/bin/env python
"""
Merges three PDF documents input from the command line.
"""
from __future__ import print_function

from os import pardir
from os.path import abspath, dirname, join
import os
from sys import argv, path

from PyPDF4 import PdfFileMerger, PdfFileReader

SAMPLE_CODE_ROOT = dirname(__file__)
SAMPLE_PDF_ROOT = join(SAMPLE_CODE_ROOT, "pdfsamples")

path.append(abspath(join(SAMPLE_CODE_ROOT, pardir)))


FLAG_HELP = {"-h", "--help"}
USAGE = """\
Merges three PDF documents input from the command line.
%(progname)s: <PDF 1> <PDF 2> <PDF 3> [output filename]
%(progname)s: [-h | --help]
""" % {
    "progname": argv[0]
}


def main(what):
    output = f"{what}/final.pdf"


    files = sorted([f"{what}/{zw}" for zw in os.listdir(what) if ".pdf" in zw and not zw in output])
    # files=[what+"/page1.pdf",what+"/page2.pdf"]

    print("merging",*files)

    reader1 = PdfFileReader(files[0])
    merger = PdfFileMerger()

    inp=[open(fil,"rb") for fil in files]


    for zw in inp:merger.append(zw)


    merger.write(open(output, "wb"))
    print("Output successfully written to", output)

    merger.close()


if __name__ == "__main__":
    main("amsterdam")