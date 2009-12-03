# -*- coding: utf-8 -*-

"""
neo.io
==================

A collection of classes for reading/writing as many as possible formats for
electrophysiological dataset.

Classes
-------

BaseFile        - abstract class which should be overriden, managing how a file will load/write
                  its data
"""

from baseio import *

all_format = [ ]

try:
    from rawio import RawIO
    all_format += [ 'raw binary' , { 'class' : RawIO  , 'info' :  'Compact raw binary generic file' } ]
except ImportError:
    print "Error while loading RawIO module"



#~ try:
    #~ from pynn import TextFile
    #~ all_format += ['PyNN']
#~ except ImportError:
    #~ print "Error while loading pyNN IO module"

#try:
    #from spike2 import *
    #all_format += ['PyNN']
#except ImportError:
    #pass



#~ if sys.platform =='win32':
	#~ from neurshare import Neuroshare
	#~ all_IOclass += [ Neuroshare ]
