#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import pandas as pd
import sys
import tkinter.filedialog as tkfd

def ext_desc(ext):
    try:
        desc = ext
    except KeyError:
        desc = ''
    else:
        pass
    return desc

def generate_index(path=None, max=500):
    # stops generating index whenever there are more than 500 records, to test if the script works
    # use 'max=0' to generate the full index
    
    path = path if path else tkfd.askdirectory() # Request path if not provided

    df = pd.DataFrame(columns=['название файла','расширение файла','папка в которой лежит файл'])
    for root, _ , files in os.walk(path):
        files = [f for f in files if not f.startswith('~') and f!='Thumbs.db']
        exts = [os.path.splitext(f)[1][1:].lower() for f in files]
        filetypes = [ext_desc(ext) for ext in exts]
        paths = [os.path.join(root, f) for f in files]
        folders = [os.path.dirname(p) for p in paths]
        df1 = pd.DataFrame({'название файла': files,
                            'расширение файла': filetypes,
                            'папка в которой лежит файл': folders})
        df = df.append(df1)
        if max and (df.shape[0]>max):
            break
    df = df.reset_index(drop=True)
    return df
  
if __name__ == '__main__':
    df = generate_index(max=0)
    df.to_excel('result.xlsx')



