import googlemaps
from firebase import firebase

firebase = firebase.FirebaseApplication('https://vehnavi.firebaseio.com/')

dest = firebase.get('/Location',None)
newdest=dest
print("Waiting for destination")
while(newdest==dest):
    dest = firebase.get('/Location',None)
    print(end="")


client = googlemaps.Client("AIzaSyAdis3Ww-4VVS-K8fq1CEF-VmD-JsQiBsA")

#dest=raw_input("Where do you wanna go?")

search = client.geocode(dest)
latdes=search[0]['geometry']['location']['lat']
longdes=search[0]['geometry']['location']['lng']
reverse = client.reverse_geocode((latdes, longdes))
r1=reverse[0]['formatted_address']
turn=(client.directions((18.499034, 73.820753), "Mumbai")[0]['legs'][0]['steps'][1]['maneuver'])
print(client.directions((18.499034, 73.820753), "Mumbai")[0]['legs'][0]['steps'][0]['distance']['text'])
turn1=turn.split('-')
        dist1=dist.split()
        dis=int(dist1[0])
print(r1)
