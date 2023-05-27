import socket
import os
import tkinter as tk
from tkinter import filedialog

def receive_file(host, port):
    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            # Bind the socket to a specific host and port
            s.bind((host, port))

            # Listen for incoming connections
            s.listen(1)

            print('Waiting for a connection...')

            # Accept the incoming connection
            conn, addr = s.accept()
            print('Connected!')

            # Receive the file name first
            file_name = conn.recv(1024).decode()

            # Open a file dialog to choose the save location
            root = tk.Tk()
            root.withdraw()
            save_path = filedialog.askdirectory()

            # Construct the file path to save the received file
            file_path = os.path.join(save_path, file_name)

            # Receive the file data
            with open(file_path, 'wb') as file:
                data = conn.recv(1024)
                while data:
                    file.write(data)
                    data = conn.recv(1024)

            print('File received and saved successfully.')
        except Exception as e:
            print(f'An error occurred while receiving the file: {str(e)}')

# Example usage
host = ''  # Bind to all available interfaces
port = int(input('Enter the port number to listen on: '))

receive_file(host, port)
