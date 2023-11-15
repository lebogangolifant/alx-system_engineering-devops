# Puppet manifest to fix the number of max open files per process for Nginx

# Use exec resource to run sed command and replace the value in the nginx defaults file
exec { 'fix--for-nginx':
  command => "/bin/sed -i /etc/default/nginx -e 's/15/4096/'",
}

# Use exec resource to restart the Nginx service
exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart',
  # Ensure that the 'fix--for-nginx' exec is completed before restarting Nginx
  require => Exec['fix--for-nginx'],
}
