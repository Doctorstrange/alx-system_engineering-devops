#!/usr/bin/env bash
# puppet connect without password

file { '/etc/ssh/ssh_config':
  ensure => present,
}

file_line { 'passwd auth off':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no',
  match => '^#PasswordAuthentication',
}

file_line { 'Declare file identity':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^#IdentityFile',
}
