# Executes a command

exec { 'pkill':
  provider => 'shell',
  command  => 'pkill killmenow',
}
