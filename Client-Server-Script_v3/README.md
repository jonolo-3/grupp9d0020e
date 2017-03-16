# grupp9 d0020e WeBeddit Client-Server_Script_v3
The main file here used in this projekt is the ClientScript_v3.x file.
The rest of the files in this folder were only used to be able to debug the client-script while creating it and 'real' versions of the 
SampleDjangoFormScript and SampleServer are implemented in the projects django server using django channels to send the data received from the client-script to the different graphs.

##Basic concepts about ClientScript.py
Make sure that you've opened port 10001 in your router and firewall since the client listens for incomming connections on that port.
Once the django server connects to the ClientScript on port 10001, the client connects back to the django server on port 10000 and starts to send data to the server. The 'SampleServer.py' script was simply used to emulate the django server script that receives the data and the 'SampleDjangoFormScript.py' file emulates the website-form used to fill in the client ip address and connect to the client to make it start/stop the data transfer. Similar versions with some modifications of these two files are implemented on our django server.

### How to run ClientScript.py
```
1. Make sure port 10001 is open for incomming connections.
2. Start the ClientScript.py file.
3. Use our django server website to connect to the ip-address running the ClientScript.py file
3.1. if you only want to test the client without using django, start both 'SampleServer' and 'SampleDjangoFormScript' and run the start(ip,session_id) function in the SampleDjangoForm with the ip address to the client and an arbitrary integer as session_id.
4. Client should now start to send data to the django server (or SampleServer file).
```
### ClientScript.py Setup Procedure
The connection procedure for the ClientScript to the django server looks like:
```
1. Django server connects to ClientScript on port 10001.
2. Django server sends the session id, x, to the ClientScript.
3. The ClientScript creates two new session id's based on the received session id: x, x+1, x+2.
4. ClientScript connects back to the django server on port 10000
5. ClientScript sends these three session id's back to the django server that establishes three unique channels for the ClientScript (three separate graphs)
6. ClientScript now starts to send data to the django server.
```
## ClientScript.py API
A certain pattern needs to be followed if you want to modify or create your own ClientScript.

--Coming soon

