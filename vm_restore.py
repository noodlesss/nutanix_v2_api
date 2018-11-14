from nutanixv2api import *
import pprint




def main():
  base_url = "https://10.64.34.85:9440/api/nutanix/v2.0/"
  api = nutanixApi(base_url, 'admin', 'Nutanix/1234')
  vmid = 'b89db76e-77a7-4fef-9368-81fa64473b30'
  body = {
	"retore_network_configuration" : "true",
	"snapshot_uuid": "3f1b6c08-eb5b-4e20-b454-71cd41d89ada"
  }
  vmrestore = api.vm_restore(vmid, body)
  print vmrestore.text
  
if __name__ == "__main__":
  main()