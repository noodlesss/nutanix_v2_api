import json
import requests
 



class nutanixApi(object):
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password


#------ TESETS
########
    def get_vm_v1(self, vm_uuid):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.get(self.base_url + 'vms/%s' %vm_uuid, verify=False).json()
        return data

#------ Virtual Machine Operations  
########

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
        data = s.get(self.base_url + 'vms', verify=False).json()
        return data


    def get_vm(self, vm_uuid):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.get(self.base_url + 'vms/%s' %vm_uuid, verify=False).json()
        return data


    def vm_create(self, body):
        '''body consist at least below parameters:
            {"memory_mb": 1024, "name": "pida","num_vcpus": 1}
        '''
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        print body
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.post(self.base_url + 'vms', json=body, verify=False).json()
        return data


    def vm_delete(self, vm_uuid):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.delete(self.base_url + 'vms/%s' %vm_uuid, verify=False).json()
        return data


    def vm_update(self, vm_uuid, body=None):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        try:
            data = s.put(self.base_url + 'vms/%s' %vm_uuid, json=body, verify=False).json()
        except Exception as e:
            print e
            data = s.put(self.base_url + 'vms/%s' %vm_uuid, json=body, verify=False)
        return data


    def vm_clone(self, vm_uuid, body=None):
        ''' body(optional) = clone machine parameters'''
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.post(self.base_url + 'vms/%s/clone' %vm_uuid, json=body, verify=False).json()
        return data


    def vm_disks_attach(self, vm_uuid, body):
        ''' body(required) = nfo about the virtual disks or CD-Roms to be attached'''
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.post(self.base_url + 'vms/%s/disks/attach' %vm_uuid, json=body, verify=False).json()
        return data



    def vm_change_power_state(self, vm_uuid, power_state):
        power_state_list = { 'ON': 'ON', 'OFF': 'OFF', "POWERCYCLE": 'POWERCYCLE', "RESET": 'RESET',
      "PAUSE": 'PAUSE', "SUSPEND": 'SUSPEND', "RESUME": "RESUME",
      "ACPI_SHUTDOWN": "ACPI_SHUTDOWN", "ACPI_REBOOT": "ACPI_REBOOT"
             }
        if power_state not in power_state_list:
            return 'please choose power state from: %s' %power_state_list
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        body = {'transition': power_state}
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.post(self.base_url + 'vms/%s/set_power_state/' %vm_uuid, json=body, verify=False).json()
        #print data.text
        return data


#---------> Task Operations 
#####
    def get_task_status(self, task_id):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.get(self.base_url + 'tasks/%s' %task_id, verify=False).json()
        return data

    def get_tasks_list(self):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.post(self.base_url + 'tasks/list', verify=False).json()
        return data

    def get_tasks_poll(self):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.post(self.base_url + 'tasks/poll', verify=False).json()
        return data

#-----------> Snapshot Operations
#####
    def get_snapshots(self, vm_uuid=None):
        '''vm_uuid can be sent to see snapshots of vm'''
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        print vm_uuid
        data = s.get(self.base_url + 'snapshots/', params={'vm_uuid': vm_uuid}, verify=False).json()
        return data

    def delete_snapshots(self, snapshot_uuid):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.delete(self.base_url + 'snapshots/%s' %snapshot_uuid, verify=False).json()
        return data


    def get_snapshot_by_name(self, snapshot_name):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.get(self.base_url + 'snapshots/', verify=False).json()
        for snap in data['entities']:
            if snap.get('snapshot_name') == snapshot_name:
                return snap
        return 'no matching snapshot name found'

#-------------> Protection Domain Operations
#####
    def get_protection_domains(self):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        parameters = {"count": count}
        data = s.get(self.base_url + 'protection_domains/', verify=False).json()
        return data


    def get_protection_domain_snapshots(self, pd_name, count=10, filter_criteria=None, sort_criteria=None):
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        parameters = {"count": count}
        try:
            data = s.get(self.base_url + 'protection_domains/%s/dr_snapshots' %pd_name, verify=False).json()
        except Exception as e:
            print e
            data = s.get(self.base_url + 'protection_domains/%s/dr_snapshots' %pd_name, verify=False)
        return data

    