# interactive-system-modelling
## Project Installation
1. Install Python (version 3.6) using the following command line or check the official website https://www.python.org/ and use an installer
```
sudo apt-get update
sudo apt-get install python3.6
```
2. Download the code from repository https://github.com/nuraynab/interactive-system-modelling.git 
3. Install PyQt5, pip should be installed (Ubuntu)
```
sudo apt update
sudo apt install python3-pip
```
```
pip3 install PyQt5
```   
  &ensp;source #1: https://pypi.org/project/PyQt5/   
  &ensp;There is also an option to install PyQt5 with python3 (Ubuntu)  
```
pip3 install --user pyqt5  
sudo apt-get install python3-pyqt5
```
  &ensp;source #2: https://gist.github.com/ujjwal96/1dcd57542bdaf3c9d1b0dd526ccd44ff   
  
  on MAC OS
```
python3 -m pip install PyQt5
```
4. Download and install XAMPP   
link: https://www.apachefriends.org/ru/download.html   
5. Install MySQLdb (on Mac OS install the pip first https://pip.pypa.io/en/stable/installing/)
```
pip3 install mysqlclient
```
source #3: https://pypi.org/project/mysqlclient/ 
## How to run the project
6. Launch XAMPP (Ubuntu)  
```
sudo /opt/lampp/lampp start
```
7. Open http://localhost/phpmyadmin   
8. Import the InterSys.sql file from the project’s database directory
9. Run the system 
```
python3 main.py
```
