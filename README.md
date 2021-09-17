# Server-Client-Python-Calculator-using-TCP

Bring the Server Up:

In this section, first, you need a Unix-like command line environment.
Give the command below to run the server:

#java -jar PythonProject.jar [Your Python Program]

For example, if the PythonProject.jar and your Python program example.py are in the same directory, you should type:

#java -jar PythonProject.jar example.py

Then the server will run and listen on port 8888. If there is no message coming to 8888 in 10 secs, the server will exit and display a message “Socket Time Out”. Before running the server, please make sure that the port 8888 is free. If you make changes to your program, please run the server again and get a new flag.

Server Behavior:

When you connect to the server via TCP socket, the server will send you a welcome message. Hello there!\n
Once you receive the welcome message, you need to send your information with “HELLO” header to the server.

HELLO [name]\n

You should replace the name block with your husky account. For example, if your husky email is abc.def@husky.neu.edu, you need to put abc.def into the name block in the following format:

HELLO abc.def\n

After saying hi to the server, it will send a set of mathematical questions like in following format:

MATH [integer] [operator] [integer]\n

For example, you will receive a question like “MATH 58 + 12”, then you should calculate it and send the answer back to the server in the following format:

ANSWER [answer]\n

For example, the answer to the question above should be “ANSWER 70”. When you answer all questions, the server will reply a flag that is unique for each student in the following format:

DONE flag\n

Once the program receives the flag, it should close the socket connection. Please make sure that you give the right name. Marks would be deducted if the name doesn’t match your husky user name.
