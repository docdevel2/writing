'''
File name: testfunc.py
This script is intended to test python functions.
'''

def main():
    """Experiment with iTunes XML"""
    # Begin main function
    import os
    import webbrowser
    import urllib.request
    import xml.etree.ElementTree as ET
    #
    # Set XML input file
    xmlinfile = "Divas27.xml" # Contains 18 songs.
    #
    # Set XML output file
    xmloutfile = "testxmloutfile.txt"
    #
    tree = ET.parse(xmlinfile)
    root = tree.getroot()
    main_dict = root.findall('dict')
    #
    # Diagnostic variables
    # TBD
    #
    # Descendants from XML root
    dict_gen1 = root.find('dict') # 1st level dictionary
    dict_gen2 = dict_gen1.find('dict') # 2nd level dictionary track list   
    #
    # Show root & 1st gen children for article
    dict_gen1_list = list(dict_gen1)
    dict_gen2_list = list(dict_gen2)
    for item in dict_gen1:
        print( 'gen1_item.tag: ', item.tag )
    print( '\n' )
    for item in dict_gen2:
        print( 'gen2_item.tag: ', item.tag )
    #
    tracklist = list( dict_gen2.findall('dict') ) # Each song/track is a dict
    #
    # Print len and a few keys/values to examine tracklist
    #
    itunes_music = []
    for item in tracklist:
        x = list(item)
        for i in range( len(x) ):
            if x[i].text == "Artist":
                itunes_music.append( list(item) )
    #
    print( "len(itunes_music): ", len(itunes_music) )
    #
    # Test "for loop" modified for diagnostics
    # This code gets the key/value strings for database
    #
    for i in range(5):
    #for i in range( len(itunes_music) ):
        for j in range( len(itunes_music[i]) ):
            if tagtrue( itunes_music[i][j].text ):
                print( j, ':', itunes_music[i][j].text \
                       , ' = ', itunes_music[i][j+1].text )
    #
    print('\nThis is the testfunc.py script\n')
    # End main function
    #
def tagtrue(arg):
    if (arg == 'Artist' or \
        arg == 'Album' or \
        arg == 'Album Artist' or \
        arg == 'Genre' or \
        arg == 'Name' or \
        arg == 'Track Number' or \
        arg == 'Year'):
        trueorfalse = True
    else:
        trueorfalse = False
    return trueorfalse


# Run "main" function
print ("Run testfunc.py script\n")
main()
