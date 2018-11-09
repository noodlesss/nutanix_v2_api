from bublegum_napi import *
import pprint, time



#"task_uuid": "09cf6cfd-5ebd-4d8a-91e2-7136f1cfbfc3"
#28 network uuid = 8c9f265d-80a2-4b27-8f06-edd5382cb8ec
body = {"memory_mb": 1024, "name": "pida1","num_vcpus": 1}


def main():
  base_url = "https://10.64.34.85:9440/PrismGateway/services/rest/v2.0/" #FOR TASK ID, DOESN'T WORK WITH V1, SHOULD INPUT 2.0
  #base_url = "https://10.64.34.85:9440/PrismGateway/services/rest/v1/"
  api = nutanixApi(base_url, 'admin', 'Nutanix/1234')
  #body = {"nic_id": "50-6b-8d-28-42-9b","nic_spec": { "network_uuid": "565784d2-7a68-4a16-a1bd-92473760f607"}, "uuid": "901aa0ee-26af-41ce-b589-b11801a20922"}
  #vmid = "6d29a0f3-80b5-4d3c-bfb7-24b400325d19"
  vmnapid = '2597073d-80ff-4457-b802-1faf073361e3'
  vmid = api.get_vm_uuid('nurandisktest')
  vmid = api.get_vm(vmid, include_vm_disk_config=True)
  print vmid
  print '#######################################'
  vmid = api.get_vm_list()
  vmid = vmid['entities'][0]
  print vmid
  
if __name__ == "__main__":
  main()


