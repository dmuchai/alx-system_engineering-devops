# Fixes a faulty WordPress site by correcting the .phpp to .php in wp-settings.php
exec { 'fix-wordpress':
  command => 'sed -i s/class-wp-locale.phpp/class-wp-locale.php/ /var/www/html/wp-settings.php',
  path    => '/usr/bin:/usr/sbin:/bin'
}
