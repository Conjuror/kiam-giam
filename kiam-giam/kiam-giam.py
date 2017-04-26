from github3 import authorize
from getpass import getuser, getpass

user = getuser()
password = ''

while not password:
    password = getpass('Password for {0}'.format(user))

note = 'kiam-giam app'
note_url = 'https://github.com/Conjuror/kiam-giam'
scopes = ['repo', 'repo:status', 'write:repo_hook']

