from nutanixv2api import *
import json, pprint, xlwt




def main():
  wb = xlwt.Workbook()
  ws = wb.add_sheet('Alerts')
  base_url = "https://10.64.35.40:9440/api/nutanix/v2.0/"
  api = nutanixApi(base_url, 'admin', 'Nutanix/1234')
  data = api.get_alerts()
  if data.status_code != 200:
    pprint.pprint(data.text)
    return
  alerts = data.json()
  entities = alerts['entities']
  for num,i in enumerate(entities,start=1):
    if i['resolved'] == False:
      ws.write(num, 1, i['cluster_uuid'])
      ws.write(num, 2, i['alert_title'])
      ws.write(num, 3, i['message'])
  wb.save('test.xls')


if __name__ == "__main__":
  main()