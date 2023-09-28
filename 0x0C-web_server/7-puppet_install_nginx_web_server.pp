# Install Nginx web server with Puppet
include stdlib

package { 'nginx':
  ensure => 'installed',
}

# Ensure Nginx is running and enabled
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

# Create the Hello World HTML page
file { '/var/www/html/index.html':
  content => 'Hello World!',
  require => Package['nginx'],
}

# Configure the Nginx default site to serve Hello World!
file { '/etc/nginx/sites-available/default':
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Enable the default Nginx site
file { '/etc/nginx/sites-enabled/default':
  ensure  => 'link',
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify  => Service['nginx'],
}

# Create a custom configuration for the 301 redirect
file { '/etc/nginx/sites-available/redirect_me':
  content => template('nginx/redirect_me.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Enable the custom configuration for the 301 redirect
file { '/etc/nginx/sites-enabled/redirect_me':
  ensure  => 'link',
  target  => '/etc/nginx/sites-available/redirect_me',
  require => File['/etc/nginx/sites-available/redirect_me'],
  notify  => Service['nginx'],
}
