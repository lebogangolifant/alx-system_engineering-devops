# Puppet manifest to change max open files limits for specific user

# Set a new hard limit for the max open files specifically for holberton user
exec { 'set-holberton-max-open-files-hard-limit':
  command => "/bin/sed -i '/^\\s*holberton\\s*hard\\s*nofile\\s/s/.*/holberton hard nofile 5000/' /etc/security/limits.conf",
}

# Set a new soft limit for the max open files specifically for holberton user
exec { 'set-holberton-max-open-files-soft-limit':
  command => "/bin/sed -i '/^\\s*holberton\\s*soft\\s*nofile\\s/s/.*/holberton soft nofile 4000/' /etc/security/limits.conf",
}

