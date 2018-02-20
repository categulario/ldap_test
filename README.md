# Ldap connection from python

An example of how one can connect to a LDAP directory server and validate someone's credentials.

## Run yourself

* `git clone https://github.com/categulario/ldap_test.git && cd ldap_test`
* `cp settings.py settings_local.py && nano settings_local.py`
* `virtualenv -p /usr/bin/python3 .env`
* `export LDAP_SETTINGS=$(pwd)/settings_local.py`
* `source .env/bin/activate`
* `pip install -r requirements.txt`
* `python ldaplap.py`
