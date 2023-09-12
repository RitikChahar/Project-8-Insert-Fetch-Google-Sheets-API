from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("mypmoproj-c375f99686b4.json",scope)
client = gspread.authorize(creds)

sheet = client.open_by_key('1cYpnbP9JWC9zKHmSlS4B99J6Ez_rUQWyOx-JgC-DGlk').sheet1

def write_row(values):
    sheet.append_row(values)

def get_rows():
    return sheet.get_all_records()

@csrf_exempt 
def insert(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            dataList = []
            for i in data.keys():
                dataList.append(data[i])
            write_row(dataList)
            output = {
                "message" : f"Saved successfully.",
                "success": True
            }
        except :
            output = {
                "message" : f"Unable to Save, there is some issue.",
                "success": False
            }
        return JsonResponse(output)
    else:
        return HttpResponse("Method Not Allowed")

@csrf_exempt 
def fetch(request):
    if request.method == 'GET':
        uid = request.GET.get('uid', None)
        print(uid)
        if uid is not None:
            try:
                record = {}
                all_data = get_rows()
                print(all_data)
                for i in all_data:
                    if i['UID'] == uid:
                        record = i
                if (len(record)>0):
                    output = {
                        "message" : f"Record Found.",
                        "data": record,
                        "success": True
                    }
                else:
                    output = {
                        "message" : f"Record Not Found.",
                        "success": True
                    }
            except :
                output = {
                    "message" : f"Unable to fetch, there is some issue.",
                    "success": False
                }
            return JsonResponse(output)
        else:
            return HttpResponse("Provide a Query parameters.")
    else:
        return HttpResponse("Method Not Allowed")