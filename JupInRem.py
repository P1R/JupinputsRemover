#!/usr/bin/env python3

from nbconvert import HTMLExporter
from io import StringIO
from argparse import ArgumentParser
from os.path import splitext

def getArgs():
    parser = ArgumentParser()
    parser.add_argument('filename')
    return parser.parse_args()

def CleanHTML(filename):
    '''Elimina inputs de htmls de jupyter'''
    #seccion que convierte a HTML un python NoteBook
    exporter = HTMLExporter(template_file='full.tpl')
    output, resources = exporter.from_filename(filename)
    output = StringIO(output)
    #Solo escribe lo que se encuentra afuera de un div class="input"
    text = output.read()
    init = text.find('<div class="input">')
    fin = text.find('<div class="output_wrapper">')
    
    res = text[:init] + text[fin:]
    
    outName = splitext(filename)[0] + '.html'
    with open(outName, 'w') as outFile:
        outFile.write(res)
    
def main():
    args = getArgs()
    CleanHTML(args.filename)

if __name__ == '__main__':
    main()
