EpisodeRenamer
==============

This basic python script takes input of a file location and a csv file and renames the files
with the TV episode info located in the CSV. The first and second command line arguments
are the absolute path of the files and the season number. The expectation is that the path
i.e. c:\The Simpsons\ , will have folders "Season 1" and "Season 2" etc under it. Season number
is given as an integer i.e. "1". The third argument is the location of the CSV file to be used,
see the example Simpsons Episodes.csv here.

The python script will rename files like "The Simpsons - S01E02 - Title.mp4" in the same folder
as the input files.