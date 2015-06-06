import os.path
import sys
import os
import lib.logger.logger as logger


# Try importing Python 2 modules using new names
try:
    import ConfigParser as configparser

# On error import Python 3 modules
except ImportError:
    import configparser

# Get values from config_file
config = configparser.RawConfigParser()
config_filename = os.path.join(os.path.dirname(sys.argv[0]), "settings.cfg")

if not os.path.isfile(config_filename):
	logger.logging.error (config_filename + " doesn\'t exist")
	logger.logging.error ("copy /rename " + config_filename + ".sample and edit")
	sys.exit(1)


else:
	try:
		with open(config_filename, "r") as fp:
			config.readfp(fp)

		try:
			feed_url = config.get("General", "feed_url")
			user_key = config.get("Pushover" , "user_key")
			app_token = config.get("Pushover", "app_token")
			push_device = config.get("Pushover" , "push_device")


		except (configparser.NoOptionError, ValueError):
			logger.logging.exception("exception:")
			pass


	except EnvironmentError:
		e = sys.exc_info()[1]
		logger.logging.error ("Could not read configuration file: " + str(e))
		# There was a config_file, don't use default values but exit
		sys.exit(1)