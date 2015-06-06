#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  api.py
#
import logging, os, httplib, urllib, json, urllib2, base64
import lib.logger.logger as logger
import lib.config as config

def pushover(push_info):
	user_key, app_token, push_device, pushtitle, pushmsg, url = push_info
	logger.logging.debug ("Sending Pushover notification...")
	conn = httplib.HTTPSConnection("api.pushover.net:443")
	conn.request("POST", "/1/messages.json",
		urllib.urlencode({
			"token": app_token,
			"user": user_key,
			"message": pushmsg,
			"title" : pushtitle,
			"device" : push_device,
			"url": url,
			"url_title": "View commit on Github",
			"html": "1"
		}), { "Content-type": "application/x-www-form-urlencoded" })
	res = conn.getresponse()
	res = json.loads(res.read())
	if res["status"] == 1 :
		logger.logging.info("Pushover notification sent succesfully")
	else:
		logger.logging.error("Pushover failed with following error" + str(res["errors"]))