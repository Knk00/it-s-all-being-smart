
import googlemaps
import re
import RPi.GPIO as GPIO
import time
import random
from firebase import firebase
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
import tkinter as tk
from PIL import ImageTk, Image

def close_escape(event=None):
    print("escaped")
    window.destroy()

client = googlemaps.Client("AIzaSyAdis3Ww-4VVS-K8fq1CEF-VmD-JsQiBsA")
firebase = firebase.FirebaseApplication('https://vehnavi.firebaseio.com/')

dest = firebase.get('/Location',None)
newdest=dest
print("Waiting for destination")
while(newdest==dest):
    dest = firebase.get('/Location',None)
    continue   
#------------------------------------------------------- 
window = tk.Tk()
window.title("Directions")
window.geometry("460x316+0+0")
window.configure(background='grey')
window.overrideredirect(True)
#pad=3
#window.geometry("{480}x{320}+0+0".format(window.winfo_screenwidth()-pad,window.winfo_screenheight()-pad))
time.sleep(1)

img1 = ImageTk.PhotoImage(Image.open("uturn.jpg"))
img2 = ImageTk.PhotoImage(Image.open("straight.jpg"))
img3 = ImageTk.PhotoImage(Image.open("right.jpg"))
img4 = ImageTk.PhotoImage(Image.open("left.jpg"))
img5 = ImageTk.PhotoImage(Image.open("rr.jpg"))
img6 = ImageTk.PhotoImage(Image.open("grey.jpg"))

#------------------------------------------------------- 
usecho=1
vcc=21
ust=12
lr=16
ll=20
GPIO.setup(lr,GPIO.OUT)
GPIO.setup(vcc,GPIO.OUT)
GPIO.setup(ll,GPIO.OUT)
GPIO.setup(usecho,GPIO.IN)
GPIO.setup(ust,GPIO.OUT)
GPIO.output(lr,GPIO.LOW)
GPIO.output(ll,GPIO.LOW)
#GPIO.output(ll,GPIO.HIGH)
def ultrasound():
    #GPIO.output(usecho,GPIO.LOW)
    return 11
    GPIO.output(ust,GPIO.LOW)
    time.sleep(1)
    GPIO.output(ust,GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(ust,GPIO.LOW)
    while GPIO.input(usecho)==False :
        a=time.time()  
    while GPIO.input(usecho)==True :
        b=time.time()    
    c=b-a
    s=17150
    d=round(s*c,2)
    


search = client.geocode(dest)
latdes=search[0]['geometry']['location']['lat']
longdes=search[0]['geometry']['location']['lng']
reverse = client.reverse_geocode((latdes, longdes))
r1=reverse[0]['formatted_address']
destination1=(latdes,longdes)
print(r1)
my_route_demo=[(18.517770, 73.815042),
(18.517770, 73.815060),
(18.517772, 73.815071),
(18.517775, 73.815084),
(18.517776, 73.815097),
(18.517776, 73.815103),
(18.517776, 73.815129),
(18.517775, 73.815134),
(18.517776, 73.815150),
(18.517775, 73.815154),
(18.517775, 73.815165),
(18.517777, 73.815176),
(18.517778, 73.815198),
(18.517781, 73.815224),
(18.517782, 73.815257),
(18.517782, 73.815286),
(18.517786, 73.815331),
(18.517784, 73.815351),
(18.517786, 73.815399),
(18.517789, 73.815415),
(18.517788, 73.815461),
(18.517790, 73.815507),
(18.517791, 73.815534),
(18.517791, 73.815553),
(18.517791, 73.815601),
(18.517794, 73.815718),
(18.517795, 73.815766),
(18.517795, 73.815803),
(18.517797, 73.815853),
(18.517796, 73.815859),
(18.517794, 73.815878),
(18.517793, 73.815918),
(18.517786, 73.815934),
(18.517775, 73.815957),
(18.517762, 73.815968),
(18.517760, 73.815971),
(18.517746, 73.815978),
(18.517738, 73.815976),
(18.517691, 73.815983),
(18.517508, 73.815982),
(18.517508, 73.815982),
(18.517477, 73.815980),
(18.517445, 73.815986),
(18.517401, 73.815985),
(18.517363, 73.815989),
(18.517301, 73.816007),
(18.517288, 73.816015),
(18.517271, 73.816026),
(18.517262, 73.816041),
(18.517261, 73.816067),
(18.517261, 73.816098),
(18.517262, 73.816132),
(18.517268, 73.816156),
(18.517273, 73.816185),
(18.517293, 73.816223),
(18.517304, 73.816238),
(18.517325, 73.816257),
(18.517349, 73.816259),
(18.517349, 73.816259),
(18.517369, 73.816262),
(18.517369, 73.816262),
(18.517405, 73.816262),
(18.517403, 73.816259),
(18.517434, 73.816258),
(18.517498, 73.816260),
(18.517551, 73.816260),
(18.517607, 73.816255),
(18.517676, 73.816257),
(18.517752, 73.816254),
(18.517862, 73.816264),
(18.517936, 73.816264),
(18.518027, 73.816268),
(18.518076, 73.816292),
(18.518107, 73.816343),
(18.518115, 73.816381),
(18.518112, 73.816507),
(18.518104, 73.816627),
(18.518098, 73.816682),
(18.518101, 73.816668),
(18.518102, 73.816774),
(18.518086, 73.816884),
(18.518080, 73.817010),
(18.518077, 73.817105),
(18.518072, 73.817228),
(18.518006, 73.817349),
(18.517788, 73.817381),
(18.517704, 73.817402),
(18.517651, 73.817411),
(18.517602, 73.817415),
(18.517591, 73.817420),
(18.517501, 73.817426),
(18.517439, 73.817428),
(18.517333, 73.817438),
(18.517188, 73.817453),
(18.517101, 73.817457),
(18.517050, 73.817462),
(18.517022, 73.817465),
(18.516952, 73.817472),
(18.516884, 73.817477),
(18.516801, 73.817487),
(18.516780, 73.817491),
(18.516669, 73.817507),
(18.516598, 73.817514),
(18.516572, 73.817517),
(18.516545, 73.817520),
(18.516511, 73.817524),
(18.516455, 73.817526),
(18.516376, 73.817543),
(18.516322, 73.817548),
(18.516250, 73.817554),
(18.516079, 73.817566),
(18.515995, 73.817566),
(18.515938, 73.817568),
(18.515938, 73.817568),
(18.515795, 73.817582),
(18.515728, 73.817583),
(18.515655, 73.817583),
(18.515607, 73.817591),
(18.515504, 73.817609),
(18.515317, 73.817654),
(18.515111, 73.817700),
(18.515017, 73.817731),
(18.514808, 73.817820),
(18.514808, 73.817820),
(18.513856, 73.818165),
(18.513740, 73.818204),
(18.513740, 73.818204),
(18.513725, 73.818215),
(18.513506, 73.818291),
(18.513461, 73.818308),
(18.513248, 73.818384),
(18.513182, 73.818410),
(18.513105, 73.818431),
(18.512975, 73.818486),
(18.512880, 73.818516),
(18.512847, 73.818531),
(18.512834, 73.818541),
(18.512829, 73.818552),
(18.512815, 73.818614),
(18.512794, 73.818780),
(18.512785, 73.818876),
(18.512751, 73.818958),
(18.512731, 73.819007),
(18.512668, 73.819094),
(18.512614, 73.819190),
(18.512569, 73.819316),
(18.512539, 73.819397),
(18.512526, 73.819475),
(18.512502, 73.819725),
(18.512485, 73.819853),
(18.512485, 73.819900),
(18.512479, 73.819921),
(18.512460, 73.819920),
(18.512422, 73.819922),
(18.512366, 73.819920),
(18.512245, 73.819915),
(18.512160, 73.819914),
(18.511979, 73.819912),
(18.511805, 73.819910),
(18.511685, 73.819909),
(18.511615, 73.819909),
(18.511569, 73.819909),
(18.511423, 73.819904),
(18.511389, 73.819906),
(18.511368, 73.819900),
(18.511308, 73.819863),
(18.511195, 73.819805),
(18.511102, 73.819747),
(18.511004, 73.819689),
(18.510945, 73.819658),
(18.510921, 73.819646),
(18.510908, 73.819647),
(18.510896, 73.819662),
(18.510878, 73.819699),
(18.510849, 73.819752),
(18.510793, 73.819856),
(18.510776, 73.819890),
(18.510680, 73.820052),
(18.510639, 73.820130),
(18.510579, 73.820248),
(18.510538, 73.820334),
(18.510538, 73.820334),
(18.510538, 73.820334),
(18.510538, 73.820334),
(18.510313, 73.820767),
(18.510261, 73.820851),
(18.510212, 73.820923),
(18.510156, 73.821012),
(18.510112, 73.821074),
(18.510099, 73.821097),
(18.510096, 73.821094),
(18.510096, 73.821094),
(18.509975, 73.821218),
(18.509908, 73.821287),
(18.509871, 73.821324),
(18.509772, 73.821428),
(18.509697, 73.821509),
(18.509629, 73.821583),
(18.509573, 73.821633),
(18.509407, 73.821812),
(18.509199, 73.821996),
(18.509194, 73.822005),
(18.509066, 73.822120),
(18.508981, 73.822195),
(18.508883, 73.822291),
(18.508799, 73.822364),
(18.508633, 73.822498),
(18.508548, 73.822572),
(18.508439, 73.822663),
(18.508364, 73.822718),
(18.508200, 73.822852),
(18.508063, 73.822958),
(18.508018, 73.823000),
(18.507860, 73.823130),
(18.507832, 73.823156),
(18.507818, 73.823170),
(18.507797, 73.823185),
(18.507774, 73.823209),
(18.507727, 73.823245),
(18.507554, 73.823386),
(18.507441, 73.823473),
(18.507308, 73.823585),
(18.507238, 73.823645),
(18.507144, 73.823723),
(18.506975, 73.823860),
(18.506894, 73.823920),
(18.506815, 73.823986),
(18.506685, 73.824101),
(18.506511, 73.824253),
(18.506361, 73.824393),
(18.506370, 73.824379),
(18.506312, 73.824446),
(18.506267, 73.824509),
(18.506212, 73.824571),
(18.506153, 73.824677),
(18.506098, 73.824804),
(18.506073, 73.824926),
(18.506038, 73.825055),
(18.506021, 73.825175),
(18.506003, 73.825301),
(18.505999, 73.825410),
(18.506009, 73.825535),
(18.506017, 73.825571),
(18.506001, 73.825576),
(18.505982, 73.825577),
(18.505929, 73.825569),
(18.505877, 73.825549),
(18.505849, 73.825539),
(18.505818, 73.825490),
(18.505781, 73.825390),
(18.505750, 73.825288),
(18.505711, 73.825170),
(18.505672, 73.825054),
(18.505639, 73.824918),
(18.505628, 73.824849),
(18.505624, 73.824806),
(18.505609, 73.824798),
(18.505556, 73.824808),
(18.505489, 73.824821),
(18.505419, 73.824831),
(18.505368, 73.824840),
(18.505262, 73.824859),
(18.505160, 73.824881),
(18.505101, 73.824889),
(18.505011, 73.824916),
(18.504921, 73.824933),
(18.504819, 73.824976),
(18.504779, 73.824985),
(18.504718, 73.825001),
(18.504659, 73.825020),
(18.504626, 73.825030),
(18.504580, 73.825040),
(18.504552, 73.825048),
(18.504538, 73.825061),
(18.504545, 73.825069),
(18.504547, 73.825120),
(18.504542, 73.825235),
(18.504540, 73.825364),
(18.504540, 73.825393),
(18.504531, 73.825410),
(18.504495, 73.825429),
(18.504421, 73.825457),
(18.504294, 73.825504),
(18.504189, 73.825549),
(18.504094, 73.825592),
(18.503959, 73.825646),
(18.503825, 73.825701),
(18.503652, 73.825780),
(18.503552, 73.825831),
(18.503430, 73.825887),
(18.503338, 73.825936),
(18.503235, 73.825980),
(18.503153, 73.826017),
(18.503057, 73.826066),
(18.502919, 73.826135),
(18.502858, 73.826165),
(18.502766, 73.826208),
(18.502670, 73.826253),
(18.502581, 73.826293),
(18.502514, 73.826334),
(18.502458, 73.826360),
(18.502341, 73.826413),
(18.502193, 73.826480),
(18.502058, 73.826552),
(18.501952, 73.826601),
(18.501816, 73.826672),
(18.501750, 73.826707),
(18.501655, 73.826754),
(18.501624, 73.826770),
(18.501594, 73.826786),
(18.501567, 73.826772),
(18.501555, 73.826746),
(18.501514, 73.826664),
(18.501482, 73.826575),
(18.501465, 73.826540),
(18.501454, 73.826528),
(18.501427, 73.826534),
(18.501363, 73.826546),
(18.501278, 73.826558),
(18.501196, 73.826569),
(18.501045, 73.826591),
(18.500966, 73.826599),
(18.500888, 73.826611),
(18.500755, 73.826634),
(18.500641, 73.826643),
(18.500532, 73.826668),
(18.500426, 73.826680),
(18.500354, 73.826693),
(18.500202, 73.826715),
(18.500113, 73.826731),
(18.500019, 73.826740),
(18.499890, 73.826762),
(18.499751, 73.826782),
(18.499626, 73.826795),
(18.499513, 73.826813),
(18.499429, 73.826831),
(18.499216, 73.826853),
(18.499037, 73.826882),
(18.498991, 73.826890),
(18.498958, 73.826898),
(18.498878, 73.826906),
(18.498728, 73.826921),
(18.498594, 73.826944),
(18.498461, 73.826959),
(18.498262, 73.826972),
(18.498127, 73.826986),
(18.498090, 73.826990),
(18.498068, 73.826994),
(18.498061, 73.826980),
(18.498062, 73.826967),
(18.498066, 73.826913),
(18.498075, 73.826837),
(18.498085, 73.826736),
(18.498108, 73.826540),
(18.498127, 73.826442),
(18.498192, 73.826135),
(18.498206, 73.826080),
(18.498154, 73.826026),
(18.498100, 73.825969),
(18.498068, 73.825910),
(18.498035, 73.825770),
(18.498093, 73.825560),
(18.498063, 73.825436),
(18.497941, 73.825288),
(18.497927, 73.825271),
(18.497913, 73.825252),
(18.497913, 73.825252),
(18.497874, 73.825058),
(18.497866, 73.824947),
(18.497858, 73.824757),
(18.497870, 73.824655),
(18.497870, 73.824655),
(18.497925, 73.824375),
(18.497938, 73.824243),
(18.497955, 73.824090),
(18.497907, 73.823858),
(18.497878, 73.823723),
(18.497854, 73.823645),
(18.497840, 73.823580),
(18.497835, 73.823558),
(18.497852, 73.823539),
(18.498001, 73.823439),
(18.498162, 73.823337),
(18.498324, 73.823226),
(18.498476, 73.823136),
(18.498669, 73.823028),
(18.498799, 73.822941),
(18.498871, 73.822900),
(18.498908, 73.822879),
(18.498919, 73.822861),
(18.498911, 73.822851),
(18.498898, 73.822807),
(18.498877, 73.822682),
(18.498876, 73.822556),
(18.498878, 73.822333),
(18.498897, 73.822156),
(18.498912, 73.821937),
(18.498926, 73.821761),
(18.498935, 73.821666),
(18.498950, 73.821449),
(18.498971, 73.821208),
(18.498992, 73.821092),
(18.499010, 73.820904),
(18.499028, 73.820819),
(18.499032, 73.820772),
(18.499034, 73.820753)]
distus=0
while(1):
    count =0
    
    
   # print("yoyo")
    #window.bind("<Escape>", close_escape)

    
    for source1 in my_route_demo:
        count=count+1
        print(count)
        turn=(client.directions(source1,destination1)[0]['legs'][0]['steps'][1]['maneuver'])
        dist=(client.directions(source1,destination1)[0]['legs'][0]['steps'][0]['distance']['text'])
        dis=(client.directions(source1,destination1)[0]['legs'][0]['steps'][0]['distance']['value'])
        #distus=ultrasound()
        turn1=turn.split('-')
        dist1=dist.split()
        dis=float(dist1[0])
        distus=ultrasound()
        
        if(distus<10):
            panel = tk.Label(window, image = img5)
            panel.place(x=0,y=201)
            window.update()
            panel.configure(image=img5)
            panel.image=img5
            window.update()
        if(distus>10):
            panel = tk.Label(window, image = img6)
            panel.place(x=0,y=201)
            window.update()
            panel.configure(image=img6)
            panel.image=img6
            window.update()
            
        
        
        if ( turn == "turn-left" ):
           # print("H")
            GPIO.output(lr,GPIO.LOW)
            panel = tk.Label(window, image = img4)
            panel.place(x=0,y=0)
            text=tk.Text(window,height=2,width=30)
            text.place(x=220,y=100)
            text.insert(tk.END,("Distance = ",dist))
            window.update()
            panel.configure(image=img4)
            panel.image=img4
            window.update()
            time.sleep(1)
            if(distus<10):
                panel = tk.Label(window, image = img5)
                panel.place(x=0,y=201)
                window.update()
                panel.configure(image=img5)
                panel.image=img5
                window.update()
            if(distus>10):
                panel = tk.Label(window, image = img6)
                panel.place(x=0,y=201)
                window.update()
                panel.configure(image=img6)
                panel.image=img6
                window.update()
            if((dis<20 and dist1[1]=='m')or(dis<0.2 and dist[1]=='km')):
                GPIO.output(lr,GPIO.LOW)
                GPIO.output(ll,GPIO.HIGH)
                time.sleep(1)
                GPIO.output(ll,GPIO.HIGH)
        
        

        if ( turn == "turn-right" ):
            #print("He")
            GPIO.output(ll,GPIO.LOW)
            panel = tk.Label(window, image = img3)
            panel.place(x=0,y=0)
            text=tk.Text(window,height=2,width=30)
            text.place(x=220,y=100)
            text.insert(tk.END,("Dist = ",dist))
            window.update()
            panel.configure(image=img3)
            panel.image=img3
            window.update()
            #panel.pack(side = "bottom", fill = "both", expand = "yes")
            time.sleep(1)
            if((dis<20 and dist1[1]=='m')or(dis<0.2 and dist[1]=='km')):
                GPIO.output(lr,GPIO.HIGH)
                GPIO.output(ll,GPIO.LOW)
                time.sleep(1)
                GPIO.output(ll,GPIO.HIGH)
            if(distus<10):
                panel = tk.Label(window, image = img5)
                panel.place(x=0,y=201)
                window.update()
                panel.configure(image=img5)
                panel.image=img5
                window.update()
            if(distus>10):
                panel = tk.Label(window, image = img6)
                panel.place(x=0,y=201)
                window.update()
                panel.configure(image=img6)
                panel.image=img6
                window.update()
            
        
    #tk.update()
    
        if ( turn == "uturn-right" ):
           # print("Hel")
            panel = tk.Label(window, image = img1)
            panel.place(x=0,y=0)
            text=tk.Text(window,height=2,width=30)
            text.place(x=220,y=100)
            text.insert(tk.END,("Distance = ",dist))
            window.update()
            #panel.pack(side = "bottom", fill = "both", expand = "yes")
            panel.configure(image=img1)
            panel.image=img1
            window.update()            
            time.sleep(1)
            if(distus<10):
                panel = tk.Label(window, image = img5)
                panel.place(x=0,y=201)
                window.update()
                panel.configure(image=img5)
                panel.image=img5
                window.update()
            if(distus>10):
                panel = tk.Label(window, image = img6)
                panel.place(x=0,y=201)
                window.update()
                panel.configure(image=img6)
                panel.image=img6
                window.update()
            if((dis<20 and dist1[1]=='m')or(dis<0.2 and dist[1]=='km')):
                GPIO.output(lr,GPIO.HIGH)
                GPIO.output(ll,GPIO.LOW)
                time.sleep(1)
                GPIO.output(ll,GPIO.HIGH)
        
        #tk.update()
        
        if ( turn =="straight" ):
            #print("Hell")
            panel = tk.Label(window, image = img2)
            panel.place(x=0,y=0)
            text=tk.Text(window,height=2,width=30)
            text.place(x=220,y=100)
            text.insert(tk.END,("Distance = ",dist))
            window.update()
            panel.configure(image=img2)
            panel.image=img2
            window.update()
          # panel.pack(side = "bottom", fill = "both", expand = "yes")
            time.sleep(1)
            if(distus<10):
                panel = tk.Label(window, image = img5)
                panel.place(x=0,y=201)
                window.update()
                panel.configure(image=img5)
                panel.image=img5
                window.update()
            if(distus>10):
                panel = tk.Label(window, image = img6)
                panel.place(x=0,y=201)
                window.update()
                panel.configure(image=img6)
                panel.image=img6
                window.update()
    
    
    
    
        
        
    



