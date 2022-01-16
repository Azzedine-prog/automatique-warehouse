"""Python MQTT Subscription client - No Username/PasswordThomas Varnish (https://github.com/tvarnish), (https://www.instructables.com/member/Tango172)Written for my Instructable - "How to use MQTT with the Raspberry Pi and ESP8266""""import paho.mqtt.client as mqttimport time as t# Don't forget to change the variables for the MQTT broker!mqtt_topic = "esp/ismail"mqtt_broker_ip = "192.168.1.111"client = mqtt.Client()# These functions handle what happens when the MQTT client connects# to the broker, and what happens then the topic receives a messagedef on_connect(client, userdata, flags, rc):    # rc is the error code returned when connecting to the broker    print("Connected!", str(rc))        # Once the client has connected to the broker, subscribe to the topic    client.subscribe(mqtt_topic)    def on_message(client, userdata, msg):    # This function is called everytime the topic is published to.    # If you want to check each message, and do something depending on    # the content, the code to do this should be run in this function        print("Topic: ", msg.topic + "\nMessage: " + str(msg.payload))        # The message itself is stored in the msg variable    # and details about who sent it are stored in userdata# Here, we are telling the client which functions are to be run# on connecting, and on receiving a messageclient.on_connect = on_connectclient.on_message = on_message# Once everything has been set up, we can (finally) connect to the broker# 1883 is the listener port that the MQTT broker is usingclient.connect(mqtt_broker_ip, 1883)client1= mqtt.Client("control1")                           #create client object#client1.on_publish = on_publish                          #assign function to callbackclient1.connect(mqtt_broker_ip,1883)i=0               start = 954031end = 785693                 def senddata(data):	msg = str(start)	ret= client1.publish("from/raspberry",msg) 	for i in data:		msg = str(i)		ret= client1.publish("from/raspberry",msg)		#i = i+1 		t.sleep(0.5)	msg = str(end)	ret= client1.publish("from/raspberry",msg)# Once we have told the client to connect, let the client object run itself#senddata([15,12,27])client.loop_forever()client.disconnect()