# Fixes the file extension from .phpp to .php
exec { 'Fixes misspelling on line 137':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
