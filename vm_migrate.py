from nutanixv2api import *
import pprint




def main():
  base_url = "https://10.64.34.85:9440/api/nutanix/v0.8/"
  api = nutanixApi(base_url, 'admin', 'Nutanix/1234')
  vmid = '0d8c5462-3ef6-410a-9d59-5abc77d5aa3c'
  host_uuid = '6ca5b2a3-d039-48f2-8058-4d7ebb9b9a68'
  vmigrate = api.vm_migrate(vmid, host_uuid)
  print vmigrate.text
  
if __name__ == "__main__":
  main()