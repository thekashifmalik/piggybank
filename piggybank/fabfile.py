from fabric.api import *

env.hosts = ['96.126.122.107']
env.user = 'kalail'

def upload_local_settings():
	put('piggybank/settings/local.py', '~/envs/piggybank/piggybank/piggybank/piggybank/settings', use_sudo=False)
	# code_dir = '/srv/django/myproject'