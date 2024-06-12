import gobnb
import json
currency="USD"
check_in = "2024-06-20"
check_out = "2024-06-28"
ne_lat = 9.97252
ne_long = -84.04564
sw_lat = 9.90958
sw_long = -84.14884
zoom_value = 2
results = gobnb.Search_all(check_in,check_out,ne_lat,ne_long,sw_lat,sw_long,zoom_value, currency,"")
details_data = []
progress = 1
jsondata = json.dumps(results)
f = open("results.json", "w")
f.write(jsondata)
f.close()
for result in results[:10]:
    data = gobnb.Get_from_room_id(result["room_id"],currency,"")
    details_data.append(data)
    print("len results: ",progress, len(results))
    progress=progress+1
    
details_data_json = json.dumps(details_data)
f = open("details_data.json", "w")
f.write(details_data_json)
f.close()