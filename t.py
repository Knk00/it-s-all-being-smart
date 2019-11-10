import googlemaps
import re

client = googlemaps.Client("Your API key")
#print(client.directions("Pune", "Mumbai")[0]['legs'][0]['steps'][0]['html_instructions'])
#print(re.findall('<b>[\w,-]+</b>', client.directions("Pune", 
#"Mumbai")[0]['legs'][0]['steps'][0]['html_instructions'])[0].replace('<b>', "").replace('</b>', ''))
print(client.directions((18.499034, 73.820753), "Mumbai")[0]['legs'][0]['steps'][1]['maneuver'])
print(client.directions((18.499034, 73.820753), "Mumbai")[0]['legs'][0]['steps'][0]['distance']['text'])
#turn=(client.directions(source1,destination1)[0]['legs'][0]['steps'][1]['maneuver'])
#dist=(client.directions((18.499034, 73.820753), "Mumbai")[0]['legs'][0]['steps'][0]['distance']['text'])
#dis=(client.directions(18.499034, 73.820753), "Mumbai")[0]['legs'][0]['steps'][0]['distance']['value'])
#print(dis)
#print(dist)
turn_distance=client.directions("Pune", "Mumbai")[0]['legs'][0]['steps'][0]['distance']['text']

print(type(turn_distance))
turn=turn_distance.split()
print(float(turn[0]))
