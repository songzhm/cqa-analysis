# Windows

## 1. [Install 'bash shell' on Windows 10](https://msdn.microsoft.com/en-us/commandline/wsl/install_guide) 

## 2. Steps to Create a New Sudo User
1. Log in to remote server as the root user

    `ssh root@server_ip_address`
2. User the `adduser` command to add a new user to system.
    
    `adduser username`

3. Use the `usermod` command to add the user to the sudo gruop.

    `usermod -aG sudo username`

    By default, on Ubuntu, members of the sudo group have sodu privileges.

4. Test sudo access on new user account

    - Use the `su` command to switch to the new user account.

        `su - username`

## 3. Install Pip on Ubuntu 16.04

1. `sudo apt-get update && sudo apt-get -y upgrade`

2. `sudo apt-get install python-pip` 

3. `pip -V` #check pip version

4. `sudo pip install --upgrade pip` #update pip

## 4. Install virtualenv

1. `sudo pip install virtualenv`

## 5. In the new created user account, create project folder

1. `mkdir votingproject`

2. `cd votingproject`

## 6. create virtualenv 

1. `virtualenv venv`

## 7. [Install MongoDB on Ubuntu 16.04](https://www.howtoforge.com/tutorial/install-mongodb-on-ubuntu-16.04/)

## 8. clone github repository

1. `git clone -- https://github.com/songzhm/cqa-analysis.git`

2. `cd cqa-analysis`

## 9. [Install MariaDB on Ubuntu 16.04](https://www.linuxbabe.com/linux-server/install-apache-mariadb-and-php7-lamp-stack-on-ubuntu-16-04-lts)

## 10. INstall MySQL-python package:

    `sudo apt-get install python-mysql.connector`

