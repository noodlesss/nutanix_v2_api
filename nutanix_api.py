from bublegum_napi import *
import pprint, time



#"task_uuid": "09cf6cfd-5ebd-4d8a-91e2-7136f1cfbfc3"

body = {"memory_mb": 1024, "name": "pida1","num_vcpus": 1}


def main():
  base_url = "https://10.64.34.85:9440/PrismGateway/services/rest/v2.0/" #FOR TASK ID, DOESN'T WORK WITH V1, SHOULD INPUT 2.0
  #base_url = "https://10.64.34.85:9440/PrismGateway/services/rest/v1/"
  api = nutanixApi(base_url, 'admin', 'Nutanix/1234')
  vm_name = 'nuranfromsnap'
  task_id = '09cf6cfd-5ebd-4d8a-91e2-7136f1cfbfc3'
  vm = api.get_vm_uuid(vm_name)
  #vm_snaps = api.get_protection_domains()
  vm_snaps = api.get_protection_domain_snapshots('luca_159471_appc_1')
  pdsnaps = vm_snaps['entities']
  for ent in pdsnaps:
  	print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ent['snapshot_create_time_usecs']/1000000))
  	for vm in ent['vms']:
  		print vm['vm_name']
  for ent in pdsnaps:
  	if ent['snapshot_create_time_usecs'] < 1496404383606885:
  		print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ent['snapshot_create_time_usecs']/1000000))
  #print ent['snapshot_uuid'] + '---' + ent['vm_name'] + '---' + str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ent['snapshot_create_time_usecs']/1000000)))
'''  print vm
  vminfo = api.get_vm(vm)
  print vminfo
  vmset = api.vm_change_power_state(vm, "RESET")
  print vmset
  vm = api.get_task_status(vmset['task_uuid'])
  print vm
  time.sleep(1)
  vm = api.get_task_status(vmset['task_uuid'])
  print vm'''


  
if __name__ == "__main__":
  main()
