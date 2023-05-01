#!/usr/bin/env python3
import os

# Set password expiration to 3 months
os.system('chage --maxage 90')

# Upgrade password hashing algorithm to SHA-512
os.system('authconfig --passalgo=sha512 --update')

# Enforce strong passwords (8char at least) and 1 retrial policy
os.system('authconfig --passminlen=8 --passmaxrepeat=1 --update')

# Enable password log
os.system('echo "password" >> /etc/audit/audit.rules')

# Setup a Login Banner
with open('/etc/motd', 'w') as banner:
    banner.write('############################\n This belongs to 1976996\n. All activities are being monitored\n.By Alejandro Cavazos Valdes and unauthorized$

# Set default file permissions to 700 for the user and 755 for other users
os.system('umask 0077')

# Enable Firewall and block all Inbound and allow all outbound traffic
os.system('firewall-cmd --zone=public --add-interface=eth0 --permanent')
os.system('firewall-cmd --zone=public --set-default-zone=public --permanent')
os.system('firewall-cmd --zone=public --add-masquerade --permanent')
os.system('firewall-cmd --zone=public --add-rich-rule=\'rule family="ipv4" source address="10.0.0.0/8" reject\' --permanent')
os.system('firewall-cmd --zone=public --add-rich-rule=\'rule family="ipv4" source address="172.16.0.0/12" reject\' --permanent')
os.system('firewall-cmd --zone=public --add-rich-rule=\'rule family="ipv4" source address="192.168.0.0/16" reject\' --permanent')
os.system('firewall-cmd --zone=public --add-rich-rule=\'rule family="ipv4" source address="224.0.0.0/4" reject\' --permanent')
os.system('firewall-cmd --reload')

# Disable SElinux
os.system('setenforce 0')
os.system('sed -i \'s/SELINUX=enforcing/SELINUX=disabled/g\' /etc/selinux/config')

# Install and configure antivirus
os.system('yum install clamav clamav-update -y')
os.system('freshclam')
os.system('systemctl enable clamav-freshclam')
os.system('systemctl start clamav-freshclam')
os.system('systemctl enable clamav-daemon')
os.system('systemctl start clamav-daemon')

# Block root account from login via SSH directly
os.system('sed -i \'s/PermitRootLogin yes/PermitRootLogin no/g\' /etc/ssh/sshd_config')

# Ensure directive “strict mode” is enabled and set SSH LogLevel to INFO
os.system('echo "LogLevel INFO" >> /etc/ssh/sshd_config')
os.system('echo "StrictModes yes" >> /etc/ssh/sshd_config')

# Enable TCP SYN Cookie Protection, IP Spoofing Protection, and Ignoring ICMP Requests
os.system('echo "net.ipv4.tcp_syncookies = 1" >> /etc/sysctl.conf')
os.system('echo "net.ipv4.conf.all.rp_filter = 1" >> /etc/sysctl.conf')
os.system('echo "net.ipv4.icmp_echo_ignore_all = 1" >> /etc/sysctl.conf')
os.system('sysctl -p')
