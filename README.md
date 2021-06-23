# interactive-system-modelling
## Project Installation
- Download the code from repository https://github.com/nuraynab/interactive-system-modelling.git 
- Install PyQt5   
```
pip3 install PyQt5
```   
  source #1: https://pypi.org/project/PyQt5/   
  There is also an option to install PyQt5 with python3 (Ubuntu)  
```
pip3 install --user pyqt5  
sudo apt-get install python3-pyqt5
```
  source #2: https://gist.github.com/ujjwal96/1dcd57542bdaf3c9d1b0dd526ccd44ff   
- Download and install XAMPP   
link: https://www.apachefriends.org/ru/download.html   
- Install MySQLdb  
```
pip3 install mysqlclient
```
source #3: https://pypi.org/project/mysqlclient/ 
## How to run the project
- Launch XAMPP (Ubuntu)  
```
sudo /opt/lampp/lampp start
```
- Open http://localhost/phpmyadmin   
- Import the InterSys.sql file from the project’s database directory
- Run the system 
```
python3 main.py
```
