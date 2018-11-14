from nutanixv2api import *
import pprint




def main():
  base_url = "https://10.64.34.85:9440/api/nutanix/v2.0/"
  api = nutanixApi(base_url, 'admin', 'Nutanix/1234')
  vmid = 'b89db76e-77a7-4fef-9368-81fa64473b30'
  body = {
  "spec_list": [
    {
      "network_uuid": "565784d2-7a68-4a16-a1bd-92473760f607"
    }
  ]
}
  data = api.vm_add_nics(vmid, body)
  print data.text
  
if __name__ == "__main__":
  main()