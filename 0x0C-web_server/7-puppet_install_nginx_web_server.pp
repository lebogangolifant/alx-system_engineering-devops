# Install Nginx web server with Puppet

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
file_line { '/etc/nginx/sites-enabled/default':
  ensure  => 'link',
  target  => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'rewrite ^/redirect_me https://www.github.com/lebogangolifant permanent;',
}
