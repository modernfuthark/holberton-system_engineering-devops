# change user limits for holberton
exec { 'soft limit':
    command  => 'sudo sed -i "s/holberton\ssoft.*/holberton\tsoft\tnofile\t10000/" /etc/security/limits.conf',
    provider => shell,
}

exec { 'hard limit':
    command  => 'sudo sed -i "s/holberton\shard.*/holberton\thard\tnofile\t10000/" /etc/security/limits.conf',
    provider => shell,
}
