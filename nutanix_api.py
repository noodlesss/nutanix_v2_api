from bublegum_napi import *
import pprint, time



#"task_uuid": "09cf6cfd-5ebd-4d8a-91e2-7136f1cfbfc3"

body = {"memory_mb": 1024, "name": "pida1","num_vcpus": 1}


def main():
  base_url = "https://10.64.34.85:9440/PrismGateway/services/rest/v2.0/" #FOR TASK ID, DOESN'T WORK WITH V1, SHOULD INPUT 2.0
  #base_url = "https://10.64.34.85:9440/PrismGateway/services/rest/v1/"
  api = nutanixApi(base_url, 'admin', 'Nutanix/1234')
  #body = {"nic_id": "50-6b-8d-28-42-9b","nic_spec": { "network_uuid": "565784d2-7a68-4a16-a1bd-92473760f607"}, "uuid": "901aa0ee-26af-41ce-b589-b11801a20922"}
  #vmid = "6d29a0f3-80b5-4d3c-bfb7-24b400325d19"
  vmnapid = '2597073d-80ff-4457-b802-1faf073361e3'
  body = {"restore_network_configuration": False, "snapshot_uuid": vmnapid}
  vmid = api.get_vm_uuid('nuranfromsnap')
  print vmid
  snaps = api.vm_restore(vmid, body)
  #print snaps.text, snaps.content
  snaps = api.get_task_status(snaps['task_uuid'])
  print snaps


  
if __name__ == "__main__":
  main()


