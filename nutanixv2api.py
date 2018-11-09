import json, requests
 



class nutanixApi(object):
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password


    def get_vm_uuid(self, vm_name):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.get(self.base_url + 'vms', verify=False).json()
        for vm in data['entities']:
            if vm_name == vm['name']:
                return vm['uuid']
        return 'no such vm'

