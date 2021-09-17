# Server-Client-Python-Calculator-using-TCP

Bring the Server Up:

In this section, first, you need a Unix-like command line environment.
Give the command below to run the server:

# java -jar PythonProject.jar [Your Python Program]

For example, if the PythonProject.jar and your Python program example.py are in the same directory, you should type:

# java -jar PythonProject.jar example.py

Then the server will run and listen on port 8888. If there is no message coming to 8888 in 10 secs, the server will exit and display a message “Socket Time Out”. Before running the server, please make sure that the port 8888 is free. If you make changes to your program, please run the server again and get a new flag.

Server Behavior:

When you connect to the server via TCP socket, the server will send you a welcome message. Hello there!\n
Once you receive the welcome message, you need to send your information with “HELLO” header to the server.

HELLO [name]\n
