from nutanixv2api import *
import pprint




def main():
  base_url = "https://10.64.34.85:9440/api/nutanix/v2.0/"
  api = nutanixApi(base_url, 'admin', 'Nutanix/1234')
  body = {
      "annotation": "nuran_net160",
      "ip_config": {
        "default_gateway": "10.10.160.1",
        "dhcp_options": {
          "domain_name_servers": "8.8.8.8,4.4.4.4"
        },
        "network_address": "10.10.160.0",
        "pool": [
          {
            "range": "10.10.160.10 10.10.160.20"
          }
        ],
        "prefix_length": 24
      },
      "name": "nuran_net_160",
      "vlan_id": 160
    }

  network = api.network_create(body)
  print network.text
  
if __name__ == "__main__":
  main()
