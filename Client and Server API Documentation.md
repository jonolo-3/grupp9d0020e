# Client & Server API Documentation

## Overview
The client and server architecture consist of three components
1. A server script that executes commands from the websites form input to send data to a given listening client, to make it start / stop sending data to the server database.
2. A client that when enabled connect back to the main server, and while enabled continuously send data to the main server over a threaded client channel.
3. A server script (PythonServerScript) that keep track of client connections and dispatches messages to corresponding client graph.

## Client API
The client uses ports 10000 and 10001 to send continuous data to the server, and receive start and stop signals respectively.
Transmitted data is plain text encoded as byte strings.
Messages send to the server should consist of an initial identifier followed by the message string.

When a client is first enabled it should establish a connection to the back end server script (PythonServerScript).
Upon succesful connection an initial information message need to be send to the server before being able to send the data.

See Client-Server-Script_v3 for full implementation details.

## Client Demo
There is a client demo python script (ClientScript_v3.0.py) that you can run on the client. 
Make sure that the IP gets forwarded correctly and there should be no issue running this on a client as is.
