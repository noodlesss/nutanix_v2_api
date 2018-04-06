from bublegum_napi import *
import pprint, time



#"task_uuid": "09cf6cfd-5ebd-4d8a-91e2-7136f1cfbfc3"

body = {"memory_mb": 1024, "name": "pida1","num_vcpus": 1}


def main():
  base_url = "https://10.64.34.85:9440/PrismGateway/services/rest/v2.0/" #FOR TASK ID, DOESN'T WORK WITH V1, SHOULD INPUT 2.0
  #base_url = "https://10.64.34.85:9440/PrismGateway/services/rest/v1/"
  api = nutanixApi(base_url, 'admin', 'Nutanix/1234')
  body = {"name": "nurancentosclone", "memory_mb": 2048}
  snaps = api.vm_clone('5cbf0eb4-a29d-4083-89fb-5944b00a6c9f', body)
  print snaps


  
if __name__ == "__main__":
  main()
