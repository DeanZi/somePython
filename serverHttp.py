


# Orly Paknahad 315444646
# Dean Zion 203488556



import socket, threading
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# our computers id
server_ip = '127.0.0.1' #you might want to change it into yours
# our port to bint to the socket
server_port = 12346
server.bind((server_ip, server_port))
server.listen(5)
while True:
 client_socket, client_address = server.accept() # accepting the client
 print 'Connection from: ', client_address #print information about client that is connected
 data = client_socket.recv(1024) #recieving data from client
 print 'Received: ', data #prints for information
 string = bytes.decode(data)  # decode the data into string
 reqMethod = string.split(' ')[0]
 if reqMethod == 'GET' :
    fileRequested = string.split(' ')
    fileRequested = fileRequested[1]  # get the requested file name

 # Check for redundent URL arguments, if are remove them
    fileRequested = fileRequested.split('?')[0]


    if (fileRequested == '/'):  # if no file is requested by client
        fileRequested = 'index.html'
    elif(fileRequested == '/redirect'):#if result file is requested by client
        fileRequested = 'result.html'




    try:
         #trying to read the file into temp file before sending to client
         file = open(fileRequested, 'rb')
         responseContent = file.read()  # read file content
         file.close()
         # response header in case file was read properly
         responseHeaders  = 'HTTP/1.1 200 OK\r\n\r\n'
         #if failed reading the file
    except Exception as e:  #response code 404 headers
         print ("not found - response code 404\r\n\r\n", e)
         responseHeaders  = 'HTTP/1.1 404 Not Found\r\n\r\n'
         responseContent = b"<html><body><p>HTTP/1.1 404 not found</p><p>Orly and Dean</p></body></html>"
    serverResponse = responseHeaders.encode()  # encode headers
    serverResponse += responseContent  # send to client the header + encoded file content
    client_socket.send(serverResponse)
     #closing the client after one data unit transport
    client_socket.close()