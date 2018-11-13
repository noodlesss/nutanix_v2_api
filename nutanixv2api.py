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


    def get_vm_list(self):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.get(self.base_url + 'vms', verify=False)
        return data    


    def get_vm(self, vm_uuid, include_vm_disk_config=False, include_vm_nic_config=False):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.get(self.base_url + 'vms/%s' %vm_uuid, params={'include_vm_disk_config': include_vm_disk_config, 'include_vm_nic_config': include_vm_nic_config},
         verify=False)
        return data


    def vm_create(self, body):
        '''required params in body:
            {"memory_mb": 1024, "name": "pida","num_vcpus": 1}
        '''
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        print body
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.post(self.base_url + 'vms', json=body, verify=False)
        return data


    def vm_delete(self, vm_uuid):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.delete(self.base_url + 'vms/%s' %vm_uuid, verify=False)
        return data


    def vm_update(self, vm_uuid, body=None):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.put(self.base_url + 'vms/%s' %vm_uuid, json=body, verify=False)
        return data


    def vm_clone(self, vm_uuid, body=None):
        ''' body(required) = clone machine parameters'''
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.post(self.base_url + 'vms/%s/clone' %vm_uuid, json=body, verify=False)
        return data



    def vm_migrate(self, vm_uuid, host_uuid):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        body = {"hostUuid": host_uuid}
        data = s.post(self.base_url + 'vms/%s/migrate/' %vm_uuid, json=body, verify=False)
        return data