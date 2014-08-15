#! /usr/bin/python
# Written in python v3.4.1
# Author Name : Snehesh
# Github Repo : https://github.com/snehesh-io/YUI-Compressor-for-whole-directory/
import os
from subprocess import Popen,PIPE
from sys import argv

PATH_YUICOMPRESSOR = 'yuicompressor-2.4.8.jar'

def compressCSS(infile,outfile):
    args = ('java','-jar',PATH_YUICOMPRESSOR,infile,'-o',outfile)
    process = Popen(args, stdout=PIPE,stderr=PIPE)
    output,error = process.communicate()
    return output.decode('utf-8'),error.decode('utf-8')

def main(folder,rename_suffix):
    directoryList = os.listdir(folder)
    if rename_suffix == False :
        for infile in directoryList :
            output,error = compressCSS(folder+'/'+infile, folder+'/'+infile)
            displayError(infile, error)
    else:
        for infile in directoryList :
            outfile = infile.replace('.css','')+'-'+rename_suffix+'.css'
            output,error = compressCSS(folder+'/'+infile, folder+'/'+outfile)
            displayError(infile, error)

def displayError(infile,error):
    if error != '':
        print('Error occured with {0} :)'.format(infile))
        print('Ref:'+'/n')
        print(error)
    else:
        print('Compressing {0} is successful'.format(infile))
    return None

def help():
    print('Usage ::')
    print('python minifiCSS.py FOLDER_NAME {None | Output file Suffix}'+'\n')
    print('for example...')
    print('\t'+'python minfiCSS.py tmpfolder min')
    print('\t'+'style.css (40kb) ==> style-min.css (35kb)'+'\n')
    print('\t'+'python minifiCSS.py tmpfolder')
    print('\t'+'style.css (40kb) ==> style.css (35kb)')


if __name__=='__main__':
    if len(argv)==3:
        script_name = argv[0]
        folder = argv[1]
        renamefile = argv[2]
        main(folder,renamefile)
    elif len(argv)==2:
        script_name = argv[0]
        folder = argv[1]
        main(folder,False)
    else:
        help()