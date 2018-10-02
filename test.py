#!/usr/bin/python3
# A small utility to check what the position to take a picture is
import requests, json, time

url = "http://IP_ADDRESS/api/v1/printer/heads/0/position"

headers = {
    'Accept': "application/json",
    'Cache-Control': "no-cache"
    }
tick = 0
while True:

	response = requests.request("GET", url, headers=headers)
	print(tick)
	tick=tick+1
	# print(json.loads(response.text)[0]["extruders"][0]["hotend"]["offset"]["state"])
	print("::",json.loads(response.text)["x"],json.loads(response.text)["y"])

	time.sleep(1)


# Ultimaker S5 Test Results
#330.0 237.0 <--- Going with this one first
#330.0 219.0

