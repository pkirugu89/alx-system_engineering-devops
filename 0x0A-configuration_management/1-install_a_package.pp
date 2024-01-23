# Puppet Manifest for installing Flask using pip3
# Author: Paul Kirugu

# Install Flask version 2.1.0 using pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
# Ensure pip3 is installed before attempting to install Flask

# Ensure python3-pip is installed
package { 'python3-pip':
  ensure => installed,
}

