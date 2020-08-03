# Creates a file in /tmp

file { '/tmp/holberton':
  group   => 'www-data',
  owner   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet',
}
