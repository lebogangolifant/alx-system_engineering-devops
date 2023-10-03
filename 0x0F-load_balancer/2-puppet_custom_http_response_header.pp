# Automate the task of creating a custom HTTP header response, but with Puppet.

# Define a custom HTTP response header
class custom_http_response_header {

  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure => running,
    enable => true,
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-available/custom-header':
    ensure  => file,
    content => "
      server {
        listen 80 default_server;
        server_name _;

        location / {
          add_header X-Served-By $hostname;
        }
      }
    ",
    require => Package['nginx'],
  }

  # Create a symbolic link to enable the site
  file { '/etc/nginx/sites-enabled/custom-header':
    ensure => link,
    target => '/etc/nginx/sites-available/custom-header',
    require => File['/etc/nginx/sites-available/custom-header'],
    notify => Service['nginx'],
  }
}
