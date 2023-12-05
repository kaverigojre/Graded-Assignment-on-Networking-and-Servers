# Graded-Assignment-on-Networking-and-Servers

#Created custom local host domain Awsomeweb and also added the subdomains to it. 

1. Changed Nginx conf file as given below: 
 server {
         listen       80;
         server_name  awesomeweb;  
      

        location / {
           root   C:/Users/Kaver/Downloads/nginx/nginx-1.24.0/awesomeweb;
           index  index.html;
         }
        }
        server {
         listen       80;
         server_name  Subdomain1;
      

        location / {
           root   html/Subdomain1;
           index  index.html;
         }

        }

          server {
         listen       80;
         server_name  Subdomain2;
      

        location / {
           root   html/Subdomain2;
           index  index.html;
         }


      }
     


2. Changed the local hosts file in Windows: c:\Windows\System32\Drivers\etc\hosts.
![localhost](image.png)

 	127.0.0.1       awesomeweb 
        127.0.0.1       Subdomain1
        127.0.0.1       Subdomain2

3. Added website file at the location mentioned in the Nginx Conf file.
4. Started Nginx on widnwos Powershell using command: start nginx 
5. Now, Awsome web can be accessed at http://awesomeweb/, and subdomains can be access at  http://Subdomain1 and http:Subdomain2


#python program writtern to check the status of the domain running which gives output in tabuler formate as given below: 

PS C:\Users\Kaver> & C:/Users/Kaver/AppData/Local/Microsoft/WindowsApps/python3.11.exe c:/Users/Kaver/Downloads/nginx/Subdomain_check.py
Checking subdomains...
+------------+--------+
| Subdomain  | Status |
+------------+--------+
| awesomeweb |  200   |
| subdomain1 |  200   |
| subdomain2 |  200   |
+------------+--------+

=======================================================================================================================================================================
Task 2: 

Install Nginx inside the Ubuntu machine and host a website. 

Come back to your host machine (windows/Linux/mac) and scan the virtual machine using nmap. Create the documentation of the process and the output of the scan. Observe the ports which are open.

Documentation: 

1. Installing Nginx on Ubuntu:

Opened a terminal on the Ubuntu virtual machine.
Updated the package list: sudo apt update
Installed Nginx: sudo apt install nginx
Started Nginx and enabled it to start on boot: sudo systemctl start nginx and sudo systemctl enable nginx
Created a simple HTML file for the website: echo "<html><body><h1>Hello, this is your Nginx-hosted website!</h1></body></html>" | sudo tee /var/www/html/index.html
Accessed the website through a web browser using the virtual machine's IP address.


2. Nmap Scan:

Opened a terminal on the host machine.
Ran an Nmap scan on the Ubuntu virtual machine's IP address: nmap VMaddress
Reviewed the output of the scan to observe open ports.

Nmap Scan Output:

Starting Nmap 7.94 ( https://nmap.org ) at 2023-12-05 18:39 India Standard Time
Nmap scan report for 10.0.2.15
Host is up (0.027s latency).
All 1000 scanned ports on 10.0.2.15 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap done: 1 IP address (1 host up) scanned in 8.71 seconds
