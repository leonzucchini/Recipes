# ======================================================================
# Scraping script for chefkoch.de
# Downloads recipe contents using previously obtained links to recipe pages
# 141017 LZ
#

# Import libraries
import requests, sys, os, re, time, random
from bs4 import BeautifulSoup

#s = requests.Session()
#r = s.get('http://www.chefkoch.de/rezepte/1324581237330785/Cape-Town-Chicken-Curry.html')
#print r.headers
##print r.headers['set-cookie']
#
#r = s.get('http://www.chefkoch.de/rezepte/1324581237330785/Cape-Town-Chicken-Curry.html')
#print r.headers

## ======================================================================
## SET UP PATHS AND OUTPUT FILES
#
## Define output and output paths
#os.chdir('/Users/leonzucchini/Dropbox/03_Research and Teaching/Recipes/')   # Change current working directory
##inputFile = '/Users/leonzucchini/Dropbox/03_Research and Teaching/Recipes/03_Data/recipeLinks_unique.csv'
#inputFile = '03_Data/recipeLinks_test.csv'
#recipeInfoFile = '03_Data/recipeDetails_raw.csv'
#ingredientsFile = '03_Data/recipeIngredients_raw.csv'
#log = '03_Data/recipeLog.csv'
#
## Define which lines to read in the URL file 
#start = 1
#end = 10000
#reportInterval = 1000
#
## Define boundaries for pause mechanism (to avoid getting blocked by website)
#fastest = 0 #at least 1 sec pause between calls
#slowest = 0
#
## Open output files and write headers if the files do not already exist (recipeDetails, recipeIngredients, and recipeLog)
#if os.path.isfile(recipeInfoFile):
#	outputRecipeInfos = open(recipeInfoFile,'a')
#else:
#	outputRecipeInfos = open(recipeInfoFile,'a')
#	outputRecipeInfos.write('id;url;\
#	rating;votes;read;saved;printed;sent;photoCount;\
#	numberIngredients;instructionLength;\
#	authorName;authorPage;onumberComments;\
#	preparationTime;restingTime;difficulty;calories\n')
#
#if os.path.isfile(ingredientsFile):
#	outputIngredients = open(ingredientsFile,'a')
#else:
#	outputIngredients = open(ingredientsFile,'a')
#	outputIngredients.write('id;ingredient;amount\n')
#
#if os.path.isfile(log):
#	outputLog = open(log,'a')
#else:
#	outputLog = open(log,'a')
#	outputLog.write('id;url;status\n')
#
## Define values for timer and iteration counter
#iterationCounter = 0
#starttime = time.time()
#n = sum(1 for line in open(inputFile, 'rU'))
#
## ======================================================================
## OPEN FILE LINES FROM FILE WITH RECIPE URLS
#
## Loop over previously downloaded recipe urls
#f = open(inputFile, 'rU') #note the U to handle line breaks correctly on OSX	
#for thisLine, line in enumerate(f):
#
#	# Check we are within block boundaries (for segmented reading)
#	if thisLine < start:
#		continue
#	elif thisLine > (end-1):
#		break
#	else:
#		# Read line from input file
#		l = line.split(';')
#		recipePage = l[2]
#		rID = l[0]
#        
#		# Print timer and status report to console
#		iterationCounter += 1
#		errorIndicator = 0
#		if iterationCounter%reportInterval==0:
#			elapsed = int(round((time.time() - starttime))/60)
#			print("Starting page "+str(iterationCounter)+" of "+str(end-start)+" ("+str(round(iterationCounter/float(end-start),2)*100)+"%) in "+str(elapsed)+" min.")
#		else:
#			pass
#
#		# ======================================================================
#		# RETRIEVE INFORMATION FROM SERVER
#
#		# Timer to sleep requests for random periods (avoiding catches)
#		time.sleep(random.randint(fastest,slowest))
#
#		# Retrieve recipe page from server, checking for html errors
#		r = requests.get('http://www.chefkoch.de/' + recipePage)
#        print r.cookies
#		# ======================================================================
#		# GATHER INFORMATION
#
#		if r.status_code != requests.codes.ok:
#			outputLog.write(str(rID)+';'+str(recipePage)+';server response '+str(r.status_code)+'\n')
#			continue
#		else:
#			soup = BeautifulSoup(r.text)
#
#			try:
#				# Get information on recipe popularity and rating
#				ratingText = repr(soup.findAll('div',{'id' : 'recipe-statistic'}))
#				ratingInfos = re.findall('<td>(.*?)</td>',ratingText,re.MULTILINE)
#				rating = ratingInfos[1].replace(',','.') #Durchschnittliche Wertung = average user rating, note replacement of German decimal comma with a decimal point
#				votes = re.findall('class="votes">(.*?)</span>',ratingText)[0].replace('.','') #Abgegebene Stimmen = number of votes, note removal of German 1000-point
#				read = re.findall('(.*?) ',ratingInfos[4])[0].replace('.','') #gelesen = number of views, note removal of German 1000-point, same for next three integers
#				saved = re.findall('(.*?) ',ratingInfos[6])[0].replace('.','') #gespeichert = number of times saved (using the site's functionality)
#				printed = re.findall('(.*?) ',ratingInfos[8])[0].replace('.','') #gedruckt = number of times printed (using the site's functionality)
#				sent = re.findall('(.*?) ',ratingInfos[10])[0].replace('.','') #verschickt = number of times sent (using the site's functionality)
#
#				# Get number of photos
#				try:
#					photoCountText = repr(soup.findAll('img',{'class' : 'slideshow-image'})[0])
#					photoCount = re.findall('title=\'1/(.*?):',photoCountText)[0]
#				except:
#					photoCount = 0
#
#				# Get amounts of ingredients
#				ingredientsText = soup.findAll('tr',{'class','ingredient'})
#				ingredientAmountText = soup.findAll('td',{'class','amount'})
#				ingredientAmounts = []
#				for zutat in ingredientAmountText:
#					ingredientAmounts.append(repr(zutat.contents[0].strip()).replace('\\xa0',' ').replace('\'','').lstrip('u'))
#
#				# Get names of ingredients
#				ingredientNameText = soup.findAll('td',{'class','name'})
#				ingredientNames = []
#				for zutat in ingredientNameText:
#					if (len(zutat.contents)>1): #need to dodge links in names
#						target = repr(zutat.contents).replace('\n','').replace('\t','')
#						ingredientNames.append(re.findall('>(.*?)<',target)[0].strip())
#					else:
#						ingredientNames.append(repr(zutat.contents[0].strip()).lstrip('u').replace('\'',''))
#				
#				# Get number of ingredients
#				numberIngredients = (len(ingredientAmounts))
#
#				# Get instruction text and length of text
#				instructionText = soup.findAll('div',{'class','instructions'})
#				instructionText = repr(instructionText[0])
#				instructionText = ''.join(BeautifulSoup(instructionText).findAll(text=True))
#				instruction = instructionText.replace('\n','').replace('\t','')
#				instruction = repr(instruction).lstrip('u\'').rstrip('\'')
#				instructionLength = len(instruction)
#
#				# Get author name and page
#				authorText = soup.findAll('div',{'class', 'user-details'})
#				authorPage = re.findall('<a href="(.*?)">',repr(authorText))[0]
#				authorName = re.findall('author\">(.*?)<', repr(authorText))[0]
#
#				# Get number of comments (note I have not gathered the commenter's identities for now)
#				commentsText = soup.findAll('div',{'class', 'comment-text'})
#				commentsText = repr(commentsText).replace('<br>','').replace('</br>','')
#				comments = re.findall('<div.*?>(.*?)</div>',commentsText) #list of comment texts
#				numberComments = len(comments) #number of comments; note this includes comments by the author themselves
#
#				# Get difficulty and preparation time
#				detailsText = repr(soup).replace('\n','').replace('\t','')
#				
#				preparationTime = re.findall('Arbeitszeit:</strong>(.*?)<span',detailsText) #careful indexing these lists: they may be empty
#				if len(preparationTime)>0:
#					preparationTime = preparationTime[0]
#				else:
#					preparationTime = ""
#				
#				restingTime = re.findall('Ruhezeit:</strong>(.*?)/',detailsText)
#				if len(restingTime)>0:
#					restingTime = restingTime[0]
#				else:
#					restingTime = ""
#				
#				difficulty = re.findall('Schwierigkeitsgrad:</strong>(.*?)/',detailsText)
#				if len(difficulty)>0:
#					difficulty = difficulty[0]
#				else:
#					difficulty = ""
#				
#				calories = re.findall('Kalorien p. P.:</strong>.*?calories\">(.*?)</',detailsText)
#
#				if len(calories)>0:
#					calories = calories[0]
#				else:
#					calories = ""
#
#			except (IndexError):
#				print 'Index error: Probably index out of bounds due to an empty list.'
#				outputLog.write(str(rID)+';'+str(recipePage)+';IndexError\n')
#				errorIndicator = 1
#
#			# ======================================================================
#			# WRITE OUTPUT TO FILE
#			
#			# Ingredients
#			if len(ingredientNames)!=len(ingredientAmounts): #print error to log if outputs are differnt lengths
#				outputLog.write(str(rID)+';'+str(recipePage)+';Ingredients: Names='+str(len(ingredientNames))+'Amounts='+str(len(ingredientAmounts))+'\n')
#				errorIndicator = 1
#			else:
#				for i in range(0, len(ingredientAmounts)): #save in long format
#					outputIngredients.write(str(rID)+';'+str(ingredientNames[i])+';'+str(ingredientAmounts[i])+'\n')
#			
#			# Recipe Infos
#			outputRecipeInfos.write(\
#				str(rID)+';'+\
#				str(recipePage)+';'+\
#				str(rating)+';'+\
#				str(votes)+';'+\
#				str(read)+';'+\
#				str(saved)+';'+\
#				str(printed)+';'+\
#				str(sent)+';'+\
#				str(photoCount)+';'+\
#				str(numberIngredients)+';'+\
#				str(instructionLength)+';'+\
#				authorName+';'+\
#				authorPage+";"+\
#				str(numberComments)+';'+\
#				preparationTime+';'+\
#				restingTime+';'+\
#				difficulty+';'+\
#				calories+'\n'\
#				)
#
#			if errorIndicator == 0:
#				outputLog.write(str(rID)+';'+str(recipePage)+';completed\n')
#			else:
#				pass
#
## Close output fils
#outputRecipeInfos.close()
#outputIngredients.close()
#outputLog.close()
