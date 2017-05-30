##########################################################################
#### Start: Initial setup

## Follow instructions from Amazon on [launching a Linux Instance](
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.html), 
which is their term for a virtual server.

## Follow instructions for [connecting to your Linux Instance](
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstances.html).


## If you are connecting to the Instance using Linux (either as the OS on 
your computer or through Git Bash on Windows), put the key-pair file in ~/.ssh/.



## Log in to the Instance's default account (ubuntu) through a Git Bash 
terminal or Putty (follow AWS website instructions).
## e.g.
  Laptop:$ ssh -i ~/.ssh/my_keypair_file.pem ubuntu@ec2-XX-XX-XXX-X.us-east-2.compute.amazonaws.com
  Laptop:$ ssh -p 2200 -i ~/.ssh/my_keypair_file.pem ubuntu@ec2-XX-XX-XXX-X.us-east-2.compute.amazonaws.com



## Create new account and set privileges (one time):
# *** http://www.brianlinkletter.com/how-to-set-up-a-new-userid-on-your-amazon-aws-server-instance/

  ubuntu@AWS:$ sudo adduser newuser

  ubuntu@AWS:$ sudo cat /etc/sudoers
  ubuntu@AWS:$ sudo visudo             # have to use visudo to open sudoers

# Add these lines to sudoers:
  newuser ALL=(ALL:ALL) ALL

# Make the new users administrators:
  ubuntu@AWS:$ sudo adduser newuser sudo
  
# Now need to create an ~/.ssh/authorized_keys file for each new user. 
# Switch to newuser account locally and create ~/.ssh directory:
  ubuntu@AWS:$ sudo su newuser
  newuser@AWS:$ mkdir ~/.ssh
  
# Switch back to ubuntu to copy authorized_keys file (can also copy and 
# paste into a new authorized_keys file on the newuser account):
  newuser@AWS:$ sudo su ubuntu
  ubuntu@AWS:$ sudo cp ~/.ssh/authorized_keys /home/newuser/.ssh/authorized_keys

# Now log back in to newuser and set file permissions:
  ubuntu@AWS:$ sudo su newuser
  newuser@AWS:$ chmod 700 ~/.ssh
  subnird@AWS:$ sudo chmod 644 ~/.ssh/authorized_keys

# Now should be able to log in as newuser remotely using key pair:
  Laptop:$ ssh -i ~/.ssh/my_keypair_file.pem newuser@ec2-XX-XX-XXX-X.us-east-2.compute.amazonaws.com

# Note: Here, the same key pair is being used for ubuntu and newuser.
# When switching accounts back and forth, can also enter $ exit.


## Disable password authentication and enforce key-based authentication:
  ubuntu@AWS:$ sudo vim /etc/ssh/sshd_config
  
# Make sure this set is to no:
  PasswordAuthentication no

# Restart ssh:
  ubuntu@AWS:$ sudo service ssh restart



## Control which accounts are allowed to log in remotely.
## /etc/ssh/ssh_config is for outgoing ssh connections and 
## /etc/ssh/sshd_config is for incoming ssh connections?

  ubuntu@AWS:$ sudo vim /etc/ssh/sshd_config

# Add this to the end of /etc/ssh/sshd_config:
  AllowUsers ubuntu newuser

# Change PermitRootLogin to no to make sure root can't log in remotely:
  PermitRootLogin no

# Restart ssh after making changes:
  ubuntu@AWS:$ sudo service ssh restart

# Check that the root user is not able to log in remotely:
  ubuntu@AWS:$ exit
  Laptop:$ ssh -i ~/.ssh/my_keypair_file.pem root@ec2-XX-XX-XXX-X.us-east-2.compute.amazonaws.com
  Laptop:$ Permission denied (publickey).



## FIREWALLS.
## If using a cloud server, you need to make sure the server is allowing 
## the ssh connections you need to be able to connect and manage it.
## https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-14-04
  
  # Check the current status:
  ubuntu@AWS:$ sudo ufw status verbose

  # Can check /etc/services to see defaults:
  ubuntu@AWS:$ cat /etc/services
  
  # Set up some rules:
  ubuntu@AWS:$ sudo ufw default deny incoming
  ubuntu@AWS:$ sudo ufw default allow outgoing

  # Specify ports:
  ubuntu@AWS:$ sudo ufw allow ssh   # normally
  ubuntu@AWS:$ sudo ufw allow 2200/tcp    # use 2200 for SSH Remote Login
  ubuntu@AWS:$ sudo ufw allow http        # port 80 by default
  ubuntu@AWS:$ sudo ufw allow ntp         # port 123 by default
  

  # Now enable the FIREWALL:
  sudo ufw enable

  # Check the status:
  sudo ufw status
  sudo ufw status numbered

  # In the Amazon Web Services console, go to "Security Groups", click on 
  # the correct instance, select the "Inbound" tab and specify the 
  # desired ports.
  # https://stackoverflow.com/questions/13475303/running-ssh-on-amazon-ec2-instance-on-port-other-than-22
  
  # Now add port 2200 to /etc/ssh/sshd_config:
  ubuntu@AWS:$ sudo vim /etc/ssh/sshd_config
  
  # Add this line:
  Port 2200
  
  # Restart:
  ubuntu@AWS:$ sudo service ssh restart
  
  # **Now log in using port 2200. Make sure all accounts work!!
  ssh -p 2200 -i ~/.ssh/my_keypair_file.pem newuser@ec2-XX-XX-XXX-X.us-east-2.compute.amazonaws.com
  
  
  # Still need to disable port 22:

#### End: Initial setup
##########################################################################
