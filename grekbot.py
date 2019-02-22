import praw
import pdb
import re
import os
import csv
import random
import inspect
#from google_images_download import google_images_download
#This will download 60 images from google image search for 'Greekgodx fat'
#def greekImages(): #Downloads 60 images of Greekgodx Fat from google
	#response = google_images_download.googleimagesdownload() #class instantiation
	#arguments = {"keywords":"Greekgodx Fat","limit":60,"print_urls":True}
	#paths = response.download(arguments)


reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('fatimage = print(os.path.abspath(image))')

def submissionCount(): #Counts how many posts grekbot has made on reddit
	list = []
	for submission in reddit.redditor('grekbot').submissions.top('all'):
		list.append(submission.title)
	return(len(list))

title = 'Weekly reminder that Grek is fat. Week #' + str(submissionCount())


#Picks a random file from grekbot/images
path = r"C:\Users\Ben\Documents\PYTHON\scripts\grekbot\images"
random_filename = random.choice([
	x for x in os.listdir(path)
	if os.path.isfile(os.path.join(path, x))
])
#Relative path of the .jpg
grekimage = (os.path.relpath(random_filename))

reddit.subreddit('testingground4bots').submit_image(title, 'C:/Users/Ben/Documents/PYTHON/scripts/grekbot/images/' + addon)

