from bublegum_napi import *
import pprint, time



#"task_uuid": "09cf6cfd-5ebd-4d8a-91e2-7136f1cfbfc3"

body = {"memory_mb": 1024, "name": "pida1","num_vcpus": 1}


def main():
  base_url = "https://10.64.34.95:9440/PrismGateway/services/rest/v2.0/" #FOR TASK ID, DOESN'T WORK WITH V1, SHOULD INPUT 2.0
  #base_url = "https://10.64.34.85:9440/PrismGateway/services/rest/v1/"
  api = nutanixApi(base_url, 'admin', 'Nutanix/1234')
  body =   {"operation": "MOUNT",
  "override_guest": True}
  vmid = "6d29a0f3-80b5-4d3c-bfb7-24b400325d19"
  #vmid = api.get_vm_uuid('nurancentos')
  print vmid
  snaps = api.vm_manage_guesttools(vmid, body)
  print snaps
  snaps = api.get_task_status(snaps['task_uuid'])
  print snaps


  
if __name__ == "__main__":
  main()
