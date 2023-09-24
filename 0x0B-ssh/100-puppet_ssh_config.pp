# Configure the SSH server to authenticates only through SSH keys
include stdlib

file { '/etc/ssh/ssh_config':
  ensure => file,
}

file_line { 'Configure IdentityFile':
  path  => '/etc/ssh/ssh_config',
  line  => '    IdentityFile ~/.ssh/school',
  match => '^(\s+IdentityFile.*)$',
}

file_line { 'Disable PasswordAuthentication':
  path  => '/etc/ssh/ssh_config',
  line  => '    PasswordAuthentication no',
  match => '^(\s+PasswordAuthentication.*)$',
}

