import socket
import os
import tkinter as tk
from tkinter import filedialog

def send_file(host, port):
    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            # Connect to the receiver
            s.connect((host, port))

            # Open a file dialog to choose the file
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.askopenfilename()

            # Get the file name from the file path
            file_name = os.path.basename(file_path)

            # Send the file name first
            s.sendall(file_name.encode())

            # Send the file data
            with open(file_path, 'rb') as file:
                data = file.read(1024)
                while data:
                    s.sendall(data)
                    data = file.read(1024)

            print('File sent successfully.')
        except Exception as e:
            print(f'An error occurred while sending the file: {str(e)}')

# Example usage
host = input('Enter the receiver IP address: ')
port = int(input('Enter the receiver port number: '))

send_file(host, port)
