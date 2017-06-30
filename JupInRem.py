#!/usr/bin/env python3
#import pdb; pdb.set_trace()
from nbconvert import HTMLExporter
from io import StringIO

def CleanHTML(InFile):
    '''Elimina inputs de htmls de jupyter'''
    #seccion que convierte a HTML un python NoteBook
    exporter = HTMLExporter(template_file='full.tpl')
    output, resources = exporter.from_filename(InFile)
    output = StringIO(output)
    #state flag 
    state = 0
    #Solo imprime si se encuentra afuera de un class=input div 
    for line  in output:
        if '<div class="input">' in line:
            state = 1
            pass
        elif '<div class="output_wrapper">' in  line:
            state = 0

        if state == 0:
            print(line)

def main():
    #Ejemplo parametro es Python NoteBook
    #Uso: ./JupInRem.py > out.html
    CleanHTML('YourNoteBook.ipynb')

if __name__ == '__main__':
    main()
