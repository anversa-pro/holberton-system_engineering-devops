#!/usr/bin/env bash
# Set up a client SSH configuration file so it can connect to a server 
# without a password with puppet

exec { 'connect':
    command  => 'echo "IdentityFile ~/.ssh/school\nPasswordAuthentication no" >> /etc/ssh/ssh_config',
    path     => '/bin/',
    provider => 'shell'
}
