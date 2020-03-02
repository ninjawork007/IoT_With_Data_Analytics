from flask import Flask, render_template, request,redirect
import paho.mqtt.client as mqtt
import time
import sys
import os
import sqlite3
import subprocess
import re 
#from connect import mydata
#The sensor is connected to GPIO17 on Pi
app = Flask(__name__)

#mess=""



@app.route("/", methods=['GET', 'POST'])
def d():
    
    #print(request.method)
    
    '''broker ="tailor.cloudmqtt.com"
    port = 14837
    username = "jczytaef"
    password = "-xKcLL-mab9Q"
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message'''
    result=temp=humidity=[]

    if request.method == 'POST':
        if request.form.get('Show') == 'Show':
            gg=getdata()
            result=re.findall(r'\d+',gg)
            temp=[result[i] for i in range(len(result)) if(i%2==0)]
            humidity=[result[i] for i in range(len(result)) if(i%2!=0)]  
            
        #elif  request.form.get('ON') == 'ON':
            #print("ON")
         #       result+=on(broker,port,username,password,client)
            #return redirect(url_for('index'))
        else:
                # pass # unknown
            return render_template("index.html")
    elif request.method == 'GET':
            # return render_template("index.html")
        print("No Post Back Call")
    return render_template("index.html",temp=temp,humidity=humidity,l=len(temp))





def getdata():
    mydata=os.popen("python connect.py").read()
    #print(type(mydata))
    return mydata
    

def temp(broker,port,username,password,client,cursor,db):

    client.username_pw_set(username,password)
    client.connect(broker,port,60)
    

    
    #humidity, temperature = Adafruit_DHT.read_retry(sensor_name, sensor_pin)
    #print(mess)
    temperature,humidity=mess,5
    cursor.execute("insert into user (temperature,humidity) values (?, ?)",(temperature,humidity))
    db.commit()
    
    #s=("Temperature: %f & Humidity: %f"%(temperature,humidity))
    #ret = client.publish("Status",ss)
    cursor.execute("SELECT * FROM user")
    #ss=cursor.fetchall()
    return cursor.fetchall()

def on(broker,port,username,password,client):
    client.username_pw_set(username,password)
    client.connect(broker,port)
    ret = client.publish("Status","Light glowing")
    return "Led Turned On"




if __name__ == '__main__':
    app.run()

