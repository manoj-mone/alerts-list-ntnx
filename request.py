'''
Replace the Prism Element IP address (ip) and cluster login credentials (auth) in the function below. 

Here is an example:

def request_details():
  ip = '1.2.3.4'
  auth = HTTPBasicAuth('admin', 'Nutanix/1234')
  return ip,auth

'''

from requests.auth import HTTPBasicAuth

def request_details():
  ip = ''
  auth = HTTPBasicAuth('', '')
  return ip,auth
