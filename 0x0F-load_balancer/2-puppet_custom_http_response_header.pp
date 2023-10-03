# Automate the task of creating a custom HTTP header response, but with Puppet.

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Define the custom HTTP header configuration
file { '/etc/nginx/conf.d/custom-header.conf':
  ensure  => 'file',
  content => "add_header X-Served-By $hostname;",
  require => Package['nginx'],
}

# Restart Nginx service when the configuration changes
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => [Package['nginx'], File['/etc/nginx/conf.d/custom-header.conf']],
}
