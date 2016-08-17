#!/usr/bin/env python

import time
import re

def nowTime():
	oneTime = time.strftime("%Y-%m-%d")
	twoTime = time.strftime("%H:%M")
	creTime = '{0} {1}'.format(oneTime, twoTime)
	return creTime

def crePost():
	Title = input('Enter title:')
	while True:
		checkAuthors = input('This post writer name is iPixelOldC,Yes?[Y/n]:').lower()
		if checkAuthors == 'y' or checkAuthors == 'n':
			break
		else:
			print('Please enter y or n!')
	if checkAuthors == 'n':
		Authors = input('enter name:')
	else:
		Authors = 'iPixelOldC'
	creFile = open('{0}.md'.format(Title), 'w+')
	Category = input('Enter Category:')
	if Category == '':
		Category = 'Post'
	creFile.write('Title: {0}\nDate: {1}\nCategory: {2}\nAuthors: {3}'.format(Title, nowTime(), Category, Authors))
	while True:
		needTags = input('Need tag?[Y/n]:').lower()
		if needTags == 'y' or needTags == 'n':
			break
		else:
			print('Please enter y or n!')
	if needTags == 'y':
		print("If you need more tag,you can use ',' or ' ' split tags!(Bad English QAQ)")
		enterTags = input('enter tag:')
		TagsRe = re.compile(r'[, ]+')
		Tags = TagsRe.split(enterTags)
		num = 0
		creFile.write('\nTags: ')
		for i in Tags:
			creFile.write('%s ' %Tags[num])
			num += 1
	
	while True:
		needSlug = input('Need slug?[Y/n]:').lower()
		if needSlug == 'y' or needSlug == 'n':
			break
		else:
			print('Please enter y or n!')
	if needSlug == 'y':
		Slug = input('Enter slug:')
		creFile.write('\nSlug: {0}'.format(Slug))

	while True:
		needSummary = input('Need summary?[Y/n]:').lower()
		if needSummary == 'y' or needSummary == 'n':
			break
		else:
			print('Please enter y or n!')
	if needSummary == 'y':
		creFile.write('\nSummary: ')
	
	creFile.write('\n\n')
	creFile.close()

print("iPixelOldC's Initialize Pelican Post - Blog:hoc117.top")
crePost()

