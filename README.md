# 🛡️ Honeypot-python
 Honeypot in Python to detect SSH attacks and log intrusion attempts.

## 🚀  Features
✅ Listens on a specific port
✅ Logs connection attempts
✅ Simulates a real server to deceive attackers
✅ Real-time notifications  

⚠️ Warning: Only use this software in controlled environments.

## 🛠️ Installation
bash
Copy
git clone https://github.com/tor-p2/Honeypot-Python.git  
cd Honeypot-Python  
pip install -r requirements.txt  
python honeypot.py

## Usage

python honeypot.py --port 2222

## Stop the process

Ctrl + C

#Killing the process 
bash
Copy
#Windows
netstat -ano | findstr :2222 
taskkill /PID #processID /F

## Logs
Connection attempts are saved in a log file named honeypot_log.txt, located in the same folder where the script is executed.
