###################################################################################
# RECIPES - ANALYSIS
# Last updated 141004 LZ

# Clear up and import libraries
rm(list=ls())
library(rgl)
library(ggplot2)
library(reshape)
library(data.table)

# Set paths
setwd("/Users/leonzucchini/Dropbox/03_Research and Teaching/Recipes/02_Analysis/")
dataPathLinks = "/Users/leonzucchini/Dropbox/03_Research and Teaching/Recipes/03_Data/recipeLinks_data.csv"
dataPathLinkMap = "/Users/leonzucchini/Dropbox/03_Research and Teaching/Recipes/03_Data/datamap_recipe_links.csv"
dataSavePath = "/Users/leonzucchini/Dropbox/03_Research and Teaching/Recipes/03_Data/recipeLinks_unique.csv"

# =================================================================================
# READ DATA

# Read file with data col formats
dataMapLinks = read.csv(dataPathLinkMap, header=T, sep=";")
colClass = as.character(dataMapLinks[,3])

# Read data (if this gets much bigger think about using scan)
dat = read.csv(dataPathLinks, sep = ";", header = T, stringsAsFactors= F)#, colClasses=colClass)
#lapply(dat,class) #check classes of columns

# =================================================================================
# BASIC CLEANING AND ANALYSIS

# Check for and remove duplicate URLS - recipes are listed in more than one category
dim(dat)[1]/length(unique(dat$url))  #there about 2.8 obs for every recipe link
dat = dat[!(duplicated(dat$url)),] #remove duplicates

# Check how many obs by category
table(dat$category) #seems reasonable

# Fix data formats
dat$category = as.factor(dat$category)
dat$difficulty = as.factor(dat$difficulty)

# Fix date formats
foo = as.character(dat$date) #not nice because missing leading 0s and as.Date not behaving
for(i in which(lapply(foo,nchar)==5)){foo[i] = paste("0",foo[i],sep="")}
foo[which(lapply(foo,nchar)==2)]=NA #there are 4 NAs that mess with the date format
dat$date = as.Date(foo, '%d%m%y')
dat = dat[!is.na(dat$date),] #the NAs are going to drive me crazy

# Write table of unique urls for reading infos
write.table(dat, dataSavePath, append=F, sep=";", col.names=F)

