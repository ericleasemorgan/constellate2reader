#!/usr/bin/env python

# constellate2reader.py - given a JSONL file of a specific shape, output a zip file suitable for the Distant Reader

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# September 1, 2021 - first investigations; while in Lancaster


# configure
CSV    = 'metadata.csv'
HEADER = 'author\ttitle\tdate\tfile\n'
SIZE   = 50
TXT    = '.txt'

# require
from io      import StringIO
from pathlib import Path
from shutil  import make_archive
import              json
import              pandas as pd
import              sys

# sanity check
if len( sys.argv ) != 3 :
	sys.stderr.write( 'Usage: ' + sys.argv[ 0 ] + " <jsonl> <carrel>\n" )
	quit()

# get input
jsonl  = sys.argv[ 1 ]
carrel = sys.argv[ 2 ]

# initialize
carrel = Path( carrel )
carrel.mkdir( exist_ok=True )

# loop through the input
with open( jsonl ) as handle :

	# initialize
	index    = 0
	metadata = HEADER
	
	# process forever
	while True:
	
		# get the next record, and check for sanity
		line = handle.readline()
		if not line : break
		
		# re-initialize
		record = json.loads( line )
	
		# parse; creator
		try :
			if record[ 'creator' ] : author = record[ 'creator' ][ 0 ]
		except KeyError : author = 'unknown'
		
		# title
		try :
			if record[ 'title' ] :
			
				# parse and limit size
				title = record[ 'title' ]
				title = title[ 0:SIZE ]
				
		except KeyError : title = 'unknown'
		
		# date
		try :
			if record[ 'datePublished' ] : date = record[ 'datePublished' ]
		except KeyError : date = 'unknown'
		
		# increment and create a file name
		index    += 1
		filename  = ( '%0.4d' % index ) + TXT
			
		# full text
		try :
			fulltext = ''
			for item in record[ 'fullText' ] : fulltext += ' ' + item
			fulltext = fulltext.replace( '\n', ' ' )
		except KeyError : continue

		# debug
		sys.stderr.write( '   creator: ' + author  + '\n' )
		sys.stderr.write( '     title: ' + title    + '\n' )
		sys.stderr.write( '      date: ' + date     + '\n' )
		sys.stderr.write( '  filename: ' + filename + '\n' )
		sys.stderr.write( '\n' )
		sys.stderr.write( fulltext )
		sys.stderr.write( '\n' )
		sys.stderr.write( '\n' )
		
		# output plain text
		with open( carrel/filename, 'w' ) as subhandle : subhandle.write( fulltext )
		
		# update metadata
		metadata += '\t'.join( [ author, title, date, filename ] ) + '\n'

# create a dataframe from the metadata, and save it
metadata = pd.read_csv( StringIO( metadata ), sep='\t' )
metadata.to_csv( carrel/CSV, index=False )

# zip up the carrel and done
make_archive( carrel, 'zip', carrel )
exit()

