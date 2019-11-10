from firebase import firebase

firebase = firebase.FirebaseApplication('https://vehnavi.firebaseio.com/')

boundry = firebase.get('/Location',None)
print("Boundry System : ",boundry)

