# Puppet Manifest for creating a file in /tmp
# Author: Paul Kirugu

# Create and ensure the /tmp/school file exists
file { '/tmp/school':
  ensure  => file,
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}

