from nutanixv2api import *
import pprint




def main():
  base_url = "https://10.64.34.85:9440/api/nutanix/v2.0/"
  api = nutanixApi(base_url, 'admin', 'Nutanix/1234')
  vmid = 'ffbe6c05-1dbf-4ee2-a5f4-f51f0972256a'
  body = {
	"retore_network_configuration" : "false",
	"snapshot_uuid": "b40e94f7-ae44-44cf-9a3a-20505d640ede"
  }
  vmrestore = api.vm_restore(vmid, body)
  print vmrestore.text
  
if __name__ == "__main__":
  main()
