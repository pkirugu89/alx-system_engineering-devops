# Puppet Manifest for Killing killmenow process
# Author: Paul Kirugu

# Define exec resource to kill a process using pkill
exec { 'pkill killmenow':
  path        => '/usr/bin',
  command     => 'pkill killmenow',
  provider    => shell,
  returns     => [0, 1]
}

