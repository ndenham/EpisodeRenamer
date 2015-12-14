import os
import glob
import csv
import sys
titles = []
path = sys.argv[1]
season = sys.argv[2]
globpath = path+"\\Season "+season+"\\*.mp4"
files = glob.glob(globpath)
with open('Simpsons Episodes.csv') as csvfile:
	reader = csv.DictReader(csvfile, delimiter = ',')
	for row in reader:
		seasonnum = row['SeasonNum']
		episodenum = row['SeasonEpisode']
		title = row['Title']
		if str(season) == row['SeasonNum']:
			newtitle = path+"\\Season "+seasonnum+"\\The Simpsons - S0"+seasonnum+"E"+episodenum.zfill(2)+" - "+title+".mp4"
			titles.append(newtitle)
print files
print titles
counter = 0
for filename in files:
	os.rename(filename, titles[counter])
	counter=counter+1
