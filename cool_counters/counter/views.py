from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from pkg_resources import to_filename
import requests
import folium
import traveltimepy as ttpy
import os
import json
from datetime import datetime #for examples
#store your credentials in an environment variable

os.environ["TRAVELTIME_ID"] = '14e7615d'
os.environ["TRAVELTIME_KEY"] = 'ff3fa17dc4ac511b62a1f5019c8dd66d'

def index(request):
    if len(Counter.objects.filter(key='counter')) == 0:
        counter = Counter(key='counter', value=0)
        counter.save()
    else:
        counter = get_object_or_404(Counter, key='counter')
    
    counter.value+=1
    counter.save()
    context = {'value': counter.value}
    return render(request, 'counter/index.html', context)

def makeMap(request):
    result = dict()
    post_data = json.loads(request.body)
    try:
        frm = post_data["fromLocation"]
        to = post_data["toLocation"]
        vehicle_type = post_data["vehicleType"]

        frm_gc = ttpy.geocoding(frm)
        to_gc = ttpy.geocoding(to)
        # print(frm_gc)
        frmlatlongarr = frm_gc["features"][0]["geometry"]["coordinates"]
        tolatlongarr = to_gc["features"][0]["geometry"]["coordinates"]
        # print(frmlatlongarr)

        
        #create api_object
#         api_object = {
#     "locations": [
#       {
#         "id": "from",
#         "coords": {
#           "lat": frmlatlongarr[0],
#           "lng": frmlatlongarr[1]
#         }
#       },
#       {
#         "id": "to",
#         "coords": {
#           "lat": tolatlongarr[0],
#           "lng": tolatlongarr[1]
#         }
#       }
#     ],
#     "arrival_searches": [
#       {
#         "id": "Trip Plan",
#         "arrival_location_id": "to",
#         "departure_location_ids": ["from"],
#         "arrival_time": "2021-09-28T09:00:00Z",
#         "properties": ["route"],
#         "transportation": {
#           "type": "driving"
#         }
#       }
#     ]
#   }

        api_object={
    "locations": [
      {
        "id": "Home",
        "coords": {
          "lat": 51.5815890,
          "lng": -0.235871
        }
      },
      {
        "id": "Office",
        "coords": {
          "lat": 51.511933,
          "lng": -0.1277888
        }
      }
    ],
    "arrival_searches": [
      {
        "id": "Morning Commute",
        "arrival_location_id": "Office",
        "departure_location_ids": ["Home"],
        "arrival_time": "2021-09-28T09:00:00Z",
        "properties": ["route"],
        "transportation": {
          "type": "driving"
        }
      }
    ]
  }

        # print("----------------------------------------------",api_object)
        headers={"X-Application-Id": "14e7615d", "X-Api-Key":"ff3fa17dc4ac511b62a1f5019c8dd66d"}

        resp = requests.post('https://api.traveltimeapp.com/v4/routes', headers=headers, json=api_object, timeout=10).json()
        
        # print("------------------------Resp----------------------",resp)
        
        a = resp["results"][0]["locations"][0]["properties"][0]["route"]["parts"]
        c = []                              
        ct = 0
        for i in a:
            for j in i["coords"]:
                c.append((float(j["lat"]),float(j["lng"])))

        p = []
        for k in c:
            ct += 1
            if(ct>100):
                petrolpumps = requests.get('https://developer.nrel.gov/api/alt-fuel-stations/v1/nearest.geojson?api_key=0CThobryleULJT5qooysq1LJpvOEgIMNTPLgvrV1&latitude=39.743078&longitude=-105.152278', timeout=10).json()
                ct=0
                if(len(petrolpumps["features"]) != 0):
                    for x in petrolpumps["features"]["geometry"]["coordinates"]:
                        p.append((float(x[0]),float(x[1])))

        print("---------------------Petrol Pump Map Coords-------------------------",p)
        
        # print("---------------------Final Map Coords-------------------------",c, len(c))          #plot
        
        map = folium.Map((c[0][0],c[0][1]), zoom_start=13)
        for pt in c:
            marker = folium.Marker([pt[0], pt[1]]) #latitude,longitude
            map.add_child(marker)
        map.save("map2.html")

        result["htmlmap"] = map.get_root().render()

    except Exception as e:
        result['result'] = "FAILURE"
        result['exist'] = "NO"
        result['error_reason'] = str(e)
    return JsonResponse(result)

