<strong>YUI Compressor for bulk CSS files compression</strong>

Written in Python 3.4.1

Usage :

    python minfiCSS.py FOLDER_NAME {  | Suffix_for_Output_file }

    for example...
        python minfiCSS.py tmpfolder min
        style.css (40kb) ==> style-min.css (35kb)

        python minifiCSS.py tmpfolder
        style.css (40kb) ==> style.css (35kb)