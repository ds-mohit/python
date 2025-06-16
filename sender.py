import socket

try:
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # AF_INET is used for IPv4 addresses 
    #and SOCK_DGRAM is for UDP protocol
    print("Socket successfully created.")

    ip_add="192.168.169.180"
    port=48888
    target_add=(ip_add, port)
    message=input("Enter the message to send:😊 ")
    encode_msg=message.encode('ascii')
    s.sendto(encode_msg, target_add)
    print("message sent successfully.")
    s.close()  # Close the socket connection
except Exception as e:
    print(f"An error occurred: {e}")



