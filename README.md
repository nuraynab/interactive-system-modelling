# interactive-system-modelling
## Project Installation
1. Download the code from repository https://github.com/nuraynab/interactive-system-modelling.git 
2. Install PyQt5   
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
3. Download and install XAMPP   
link: https://www.apachefriends.org/ru/download.html   
4. Install MySQLdb  
```
pip3 install mysqlclient
```
source #3: https://pypi.org/project/mysqlclient/ 
## How to run the project
5. Launch XAMPP (Ubuntu)  
```
sudo /opt/lampp/lampp start
```
6. Open http://localhost/phpmyadmin   
7. Import the InterSys.sql file from the project’s database directory
8. Run the system 
```
python3 main.py
```
