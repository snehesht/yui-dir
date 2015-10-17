#!/usr/bin/python3
import os
from subprocess import Popen,PIPE
from sys import argv

PATH_YUICOMPRESSOR = 'yuicompressor-2.4.8.jar'

def compressCSS(infile,outfile):
    args = ('java','-jar',PATH_YUICOMPRESSOR,infile,'-o',outfile)
    process = Popen(args, stdout=PIPE,stderr=PIPE)
    output,error = process.communicate()
    return output.decode('utf-8'),error.decode('utf-8')

def main(folder,file_type,rename_suffix):
    directoryList = os.listdir(folder)
    file_type = '.'+file_type
#    if rename_suffix == False :
#        for infile in directoryList :
#            output,error = compressCSS(folder+'/'+infile, folder+'/'+infile)
#            displayError(infile, error)
#    else:
#        for infile in directoryList :
#            outfile = infile.replace(file_type,'')+'-'+rename_suffix+file_type
#            output,error = compressCSS(folder+'/'+infile, folder+'/'+outfile)
#            displayError(infile, error)

    for infile in directoryList:
        if file_type in infile:
            if rename_suffix ==False :
                output,error = compressCSS(folder+'/'+infile, folder+'/'+infile)
                displayError(infile, error)
            else:
                outfile = infile.replace(file_type,'')+'-'+rename_suffix+file_type
                output,error = compressCSS(folder+'/'+infile, folder+'/'+outfile)
                displayError(infile, error)
        else:
            continue


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
    print('python minifiCSS.py { css | js }FOLDER_NAME {None | Output file Suffix}'+'\n')
    print('for example...')
    print('\t'+'python minfiCSS.py tmpfolder min')
    print('\t'+'style.css (40kb) ==> style-min.css (35kb)'+'\n')
    print('\t'+'python minifiCSS.py tmpfolder')
    print('\t'+'style.css (40kb) ==> style.css (35kb)')


if __name__=='__main__':
    if len(argv)==4:
        script_name = argv[0]
        file_type = argv[1]
        folder = argv[2]
        renamefile = argv[3]
        main(folder,file_type,renamefile)
    elif len(argv)==3:
        script_name = argv[0]
        file_type = argv[1]
        folder = argv[2]
        main(folder,file_type,False)
    else:
        help()
