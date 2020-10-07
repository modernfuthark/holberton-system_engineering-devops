# changes the open file limit for nginx
exec { 'Increases the ULIMIT from 15 to 4096':
    command  => 'sudo sed -i "s/15/4096/g" /etc/default/nginx; sudo service nginx restart',
    provider => 'shell',
}
