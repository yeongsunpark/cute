import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import glob

import win32com.client as win32

for path, dirs, files in os.walk('E:\workspace\83\ys\cute\law\\new'):
    files = glob.glob('E:\workspace\83\ys\cute\law\\new\*.doc')

    for fname in files:
        word = win32.Dispatch("Word.Application")
        # word.Visible = 0

        doc1 = word.Documents.Open(fname)

        DocContents = str(doc1.Content.Text)
        DocContents = DocContents.replace('\r', '\n')
        print(DocContents)
        word.ActiveDocument.Close()
        word.Quit()
        doc1 = ''
        DocContents = ''
