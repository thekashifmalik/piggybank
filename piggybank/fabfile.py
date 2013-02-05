from fabric.api import *

env.hosts = ['96.126.122.107']
env.user = 'kalail'

def upload_settings():
	put('piggybank/settings/local.py', '~/envs/piggybank/piggybank/piggybank/piggybank/settings', use_sudo=False)

def deploy():
	# Pull from github
	with cd('envs/piggybank/piggybank'):
		run('git pull')
	# Copy over local settings
	put('piggybank/settings/local.py', '~/envs/piggybank/piggybank/piggybank/piggybank/settings', use_sudo=False)
