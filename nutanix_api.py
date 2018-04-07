from bublegum_napi import *
import pprint, time



#"task_uuid": "09cf6cfd-5ebd-4d8a-91e2-7136f1cfbfc3"

body = {"memory_mb": 1024, "name": "pida1","num_vcpus": 1}


def main():
  base_url = "https://10.64.34.85:9440/PrismGateway/services/rest/v2.0/" #FOR TASK ID, DOESN'T WORK WITH V1, SHOULD INPUT 2.0
  #base_url = "https://10.64.34.85:9440/PrismGateway/services/rest/v1/"
  api = nutanixApi(base_url, 'admin', 'Nutanix/1234')
  body = {"vm_disks": [
    {
      "disk_address": {
        "device_bus": "SCSI",
        "device_index": 0,
      }      
      "is_thin_provisioned": True,
      "vm_disk_create": {
        "size": 10,
        "storage_container_uuid": "506fb3b2-06c0-403e-8861-6e35cc41a07c"
      }
    }
      
      ]
      }
  vmid = api.get_vm_uuid('nurancentos')
  snaps = api.vm_disks_attach(vmid, body)
  print snaps


  
if __name__ == "__main__":
  main()
