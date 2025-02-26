# Puppet manifest to fix WordPress 500 error

exec { 'fix-wordpress':
  command => 'chown -R www-data:www-data /var/www/html && chmod -R 755 /var/www/html',
  path    => ['/bin', '/usr/bin'],
}
