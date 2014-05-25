# get token
# if not token 
#     request username and password
#     get token
#     save token to file

import ConfigParser
import os.path
import requests

auth_section = 'authentication'

def getToken(ini_file,debug=False):
    result = None
    try:
        config = ConfigParser.RawConfigParser()
        config.read(os.path.expanduser(ini_file))
        result = config.get(auth_section,'token')
    except Exception, e:
        if debug:
            print e
    finally:
        return result
    
def createToken(username,password):
    r = requests.post('https://api.github.com/authorizations', auth=(username, password), data='{"scopes": ["repo"], "note": "github-flow token"}')
    if r.status_code == 201:
        return r.json()['token']
    elif r.status_code == 401:
        print "Error:"+r.json()['message']
    else:
        print r.text

def saveToken(ini_file,token):
    config = ConfigParser.SafeConfigParser()
    config.add_section(auth_section)
    config.set(auth_section, 'token', token)

    # Writing our configuration file to 'example.cfg'
    with open(os.path.expanduser(ini_file), 'w+b') as configfile:
        config.write(configfile)