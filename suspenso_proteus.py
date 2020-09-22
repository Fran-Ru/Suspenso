import datetime
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(13, GPIO.OUT )
GPIO.setup(18, GPIO.OUT )
est1="OFF"
est2="OFF"
 
   
def on_message(client, obj, msg):
    print( msg.payload.decode( "utf-8"))
 
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.username_pw_set("saturno101@outlook.com","10prmillcoma")
mqttc.connect("maqiatto.com" , 1883)
mqttc.subscribe("saturno101@outlook.com/test1", 0)
rc=0
print("inicio...")

def sensor1():	
   global est1

   estado = GPIO.input(11)
   if estado == False:
      GPIO.output(13, True)  
      est1="ON"
      print("Sensor 1 ON")
      time.sleep(0.3)
   if estado == True:
      GPIO.output(13, False)  
      est1="OFF"
      time.sleep(0.3)
      
def sensor2():	
   global est2

   estado = GPIO.input(7)
   if estado == False:
      GPIO.output(18, True)  
      est2="ON"
      print("Sensor 2 ON")
      time.sleep(0.3)
#      F =open("texto.txt","w")
#	    y=datetime.datetime.now()
#	    fecha =str(y)
#	    print(fecha)
#	    F.write(fecha)
#	    F.close()
   if estado == True:
      GPIO.output(18, False)   # Enciende el LED
      est2="OFF"
      time.sleep(0.3)

x=0
      
while True:
     
    estado1=est1
    se1=sensor1()
    se2=sensor2()
    estado2=est2
    time.sleep(1)
    mqttc.publish("saturno101@outlook.com/test","sensor1="+estado1+"="+estado2)
    if estado1=="ON" and estado2=="ON":
	    F =open("texto.txt","a")
	    y=datetime.datetime.now()
	    fecha =str(y)
	    print(fecha)
	    F.write(fecha)
	    F.write( " LED1 _"+estado1)
	    F.write(" LED2_"+estado2)
	    F.write('\n')
	    F.close()

	 