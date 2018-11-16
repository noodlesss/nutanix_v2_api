from nutanixv2api import *
import pprint




def main():
  base_url = "https://10.64.34.85:9440/api/nutanix/v2.0/"
  api = nutanixApi(base_url, 'admin', 'Nutanix/1234')
  vmid = '9518ce20-ab38-44e0-b6c4-18ae8de0ccbe'
  body = {
    "snapshot_specs": [{
      "snapshot_name": "my_vm_snapshot",
      "vm_uuid": vmid
    }]
  }
  snapshot = api.snapshot_vm(body)
  print snapshot.text
  
if __name__ == "__main__":
  main()
