# Scraping script for chefkoch.de
# Downloads links to recipes

import requests
import csv
import dys
import os 
from bs4 import BeautifulSoup as bs

# Define output path and maximum iterations
output = '/Users/leonzucchini/Dropbox/03_Research and Teaching/Recipes/03_Data/recipeLinks.csv'
maxIter = 10**5 #maximum iteratinos for one category to avoid infinite loop between pages

# Remove previous output versions
try:
 	os.remove(output)
 	print('Old output removed. You\'re good to go.')
except OSError:
	print('No previous output found so none removed (duh).')

# Define recipe category headers and prepare file
categories = [ #title, subpage address, number of pages (approx)
	['Backen und Suessspeisen Rezepte', '/rs/s0g47/Suessspeisen-Backen-Rezepte.html', 2272],
	['Getraenke Rezepte', '/rs/s0g102/Getraenke.html', 343],
	['Menueart Rezepte', '/rs/s0g1/Menueart.html', 5420],
	['Regional Rezepte', '/rs/s0g85/Rezepte-nach-Laendern.html', 1520],
	['Saisonal Rezepte', '/rs/s0g53/saisonale-Rezepte.html', 2301],
	['Spezielles Rezepte', '/rs/s0g32/Speisearten.html', 4800],
	['Zubereitungsarten Rezepte', '/rs/s0g61/Zubereitungsarten.html', 7176]
]

# Write header to file
output = open(output,'a')
output.write('id;category;url;title;description;time;difficulty;views;date\n')

rID = 0 #recipe id

# Loop over recipe categories, reading all pages in each category
for categoryNum in range(0,len(categories)):

	# Open category first page of category
	subpage = categories[categoryNum][1]

	breakloop = 0
	while breakloop < maxIter: #catch for infinite loops between pages

		# Get page and interpret with beautifulsoup
		r = requests.get('http://www.chefkoch.de/' + subpage)
		soup = BeautifulSoup(r.text)
		
		 # Loop over all recipes on that page
		tr_elements = soup.tbody.find_all('tr') #basic recipe infos are stored in tr tags

		for i in range(0,len(tr_elements)):

			# Store recipe id and category number for easier referencing
			rID += 1
			recipeInfo = [str(rID)] #recipe id
			recipeInfo.append(str(categoryNum+1)) #category number
			recipeInfo.append(tr_elements[i]['data-url'].lstrip('u')) #store recipe url
			
			# Store recipe parts, stripping unwanted characters at the same time
			for string in tr_elements[i].stripped_strings: #loop over recipe infos in tr tag
				info = repr(string)
				info = info.lstrip('u\'').rstrip('\'') #remove leading 'u' and trailing '\u'
				info = info.replace(';',"-").replace('\"','') #remove characters that misbehave in csv format
				info = info.replace('.','').replace(' Min', '') #remove 1000-dot and "Min." for easier recognition as integers
				recipeInfo.append(info) #append to storage list, stripping out superfluous characters

			for j in range(0,len(recipeInfo)):
				if j < (len(recipeInfo)-1):
					output.write(recipeInfo[j]+';') #write recipe information to csv file separated by semicolon
				else:
					output.write(recipeInfo[j]+'\n') #write last column separated by newline

		# Find next page in category, if it doesn't exist break to next category; report progress
		b = soup.findAll("a", {"class" : "pagination-item pagination-next"}) #find next page
		if len(b) > 0: #check whether there is a next page
			subpage = b[0]['href'] #update subpage
			breakloop +=1

			# Report progress
			if breakloop%10 == 0:
 				perc = round((float(breakloop) / float(categories[categoryNum][2])) * 100,0)
 				print categories[categoryNum][0] + ' ' + str(breakloop) + ' of ' + str(categories[categoryNum][2]) + ': ' + str(perc) + '%'
		else:
			break

output.close()

# Define main()
def main():
	print 'hi leon'

# Boilerplate to call main()
if __name__ == '__main__':
  main()
