#Manifest setup client SSH config file ...without a password
file { '/etc/ssh/ssh_config':
  ensure  => file,
  mode    => '0600',
  content => "\
Host ubuntu
    HostName ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no\n",
}
