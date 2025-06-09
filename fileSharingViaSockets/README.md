# 📁 Simple File Transfer using Python Sockets

This project provides a simple GUI-assisted file transfer system using Python's built-in `socket` module and `tkinter` for file dialogs. It includes:

- `sender.py`: A script to select and send a file to another device.
- `client.py`: A receiver script that listens for incoming files and allows you to choose where to save them.
## 🔧 Features

- 📂 GUI-based file and folder selection using `tkinter`
- 📡 TCP socket connection for reliable file transfer
- 🖥️ Cross-platform compatible with Python 3
- 🔐 Simple and lightweight, no third-party dependencies## 🚀 Getting Started

### ✅ Requirements

- Python 3.x
- No external libraries required (uses `tkinter`, `socket`, `os`)

---
## 📦 File Structure
```plaintext
.
├── sender.py     # Sends file to a specified IP and port
├── client.py     # Receives the file and saves to chosen folder

```

## 📤 How to Send a File
1. Run client.py on the receiving machine:
```bash
python client.py
```
- Enter the port number to listen on (e.g., 5001).
- Choose the folder where the file will be saved.
2. Run sender.py on the sending machine:
```bash
python sender.py
```
- Enter the IP address of the receiving machine.
- Enter the same port number used on the client.
- Choose the file to send.
3. The file will be transferred and saved to the selected folder on the receiver's end.

## 🌐 Network Setup 
- Ensure both sender and receiver are on the same local network (or port-forwarded if remote).
- Use your local IP (e.g., 192.168.x.x) on the sender side when prompted.

## 📌 Example
Receiver:
```bash
Enter the port number to listen on: 5001
```
Sender:
```bash
Enter the receiver IP address: 192.168.1.5
Enter the receiver port number: 5001
```
## ❗ Notes
- The connection is one-time and closes after the file transfer.
- It currently supports transferring one file at a time.
- File name collisions are not handled — new files will overwrite if they have the same name.


## 🙏 Acknowledgements

- Python socket module documentation
- tkinter GUI for interactive file selection


## 📄 License
This project is intended for educational and experimental use. Please contact the author for reuse or distribution permissions.
