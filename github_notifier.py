#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  github_notifier.py
#
# github notifications

import os.path, re, httplib, urllib
import sys
import json
import lib.feedparser as feedparser
import lib.logger.logger as logger
import lib.config as config
import lib.api as api
import lib.misc as misc

file_name = os.path.join(os.path.dirname(sys.argv[0]), "last_run")
d = feedparser.parse(config.feed_url)

logger.logging.info("Opening URL: " + config.feed_url)
if d.status == 301:
	logger.logging.error("Feed is moved, new link is " + d.href)
	sys.exit()

if d.status == 401:
	logger.logging.error("Feed is gone, exiting")
	sys.exit()

if d.status == 200:
	logger.logging.info("Status: Ok!")

if os.path.exists(file_name):
	with open (file_name, "r") as lastrun:
		lastid=lastrun.read().replace('\n', '')
	logger.logging.debug("Found " + file_name + " lastid = " + lastid)
else:
	lastid = d.entries[1].id
	logger.logging.debug(file_name + " does not exist, using lastid = " + lastid)

thisid = d.entries[0].id
if lastid == thisid:
	logger.logging.info("Nothing to do, exiting")
	sys.exit()
else:
	if not "pushed" in d.entries[0].title:
		logger.logging.info("No pushes found, exiting")
		f = open(file_name, 'w' )
		f.truncate()
		f.write( d.entries[0].id + '\n' )
		f.close()
		sys.exit()
	content = d.entries[0].content[0].value
	content = re.compile( "<blockquote>(.*)</blockquote>",re.S|re.M ).search( content ).group( 1 )
	content = content.replace('\n', ' ').replace('\r', '').lstrip(' ')
	logger.logging.info("New Item: " + d.entries[0].id + " - " + d.entries[0].title + ": " + content)
	f = open(file_name, 'w' )
	f.truncate()
	f.write( d.entries[0].id + '\n' )
	f.close()

push_info = (config.user_key, config.app_token, config.push_device, d.entries[0].title, content, d.entries[0].link)
api.pushover(push_info)
misc.access_log_for_all()