from pprint import pprint
from itacate import Config
import ldap
import sys
import os

def main(config):
    client = ldap.initialize('ldap://{host}:{port}'.format(host=config['HOST'], port=config['PORT']))
    binddn = config['BIND_DN']
    pw = config['PASSWORD']
    basedn = config['BASE']
    searchFilter = config['USER_FILTER']
    searchAttribute = None
#this will scope the entire subtree under UserUnits
    searchScope = ldap.SCOPE_BASE

#Bind to the server
    try:
        client.protocol_version = ldap.VERSION3
        client.simple_bind_s(binddn, pw)
    except ldap.INVALID_CREDENTIALS:
      print("Your username or password is incorrect.")
      sys.exit(0)
    except ldap.LDAPError as e:
      if type(e.message) == dict and e.message.has_key('desc'):
          print(e.message['desc'])
      else:
          print(e)
      sys.exit(0)

    try:
        res = client.search_s(config['BIND_DN'], searchScope, searchFilter, searchAttribute)

        pprint(res)
    except ldap.LDAPError as e:
        print(e)

    client.unbind_s()

if __name__ == '__main__':
    config = Config(os.path.dirname(os.path.realpath(__file__)))
    config.from_pyfile('settings.py')
    config.from_envvar('LDAP_SETTINGS', silent=False)

    main(config)
