import time 
import paho.mqtt.client as mqtt
import sqlite3
mss=0

def on_connect(client,userdata,flag,rc):
    #print("connected with code"+str(rc))
    client.subscribe("dhtsensor")
    #print("Client subscribed")
def on_message(client,userdata,msg):
    global mss
    mss=msg.payload

client = mqtt.Client()


with sqlite3.connect("IIITDM.db") as db:
        cursor=db.cursor()
#cursor.execute("delete from mydata1;") 
cursor.execute('''
    CREATE TABLE IF NOT EXISTS mydata1(
    temperature INTEGER(20) NOT NULL,
    humidity INTEGER(20) NOT NULL);
    ''')

client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("jczytaef","-xKcLL-mab9Q")
client.connect("tailor.cloudmqtt.com", 14837,60)

client.loop_start()
s=0
while s!=10:
    temperature=int(mss)//100
    humidity=int(mss)%100
    if(temperature!=0 and humidity!=0):
    	cursor.execute("insert into mydata1 (temperature,humidity) values (?,?)",(temperature,humidity))
    db.commit()
    #print(mss)
    time.sleep(2)
    s+=1

client.loop_stop()


cursor.execute("DELETE FROM mydata1 WHERE temperature IS NULL;") 

mydata=0
cursor.execute("SELECT * FROM mydata1 where temperature is not null;")
mydata=cursor.fetchall()
print(mydata)
 #   print(i[0])

