# 7-puppet_install_nginx_web_server.pp
#
# This manifest installs Nginx, ensures it is configured to serve a custom page
# with the string 'Hello World!' at the root, and sets up a 301 redirect for /redirect_me.

# Install the Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx is running and enabled
service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => Package['nginx'],
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
    listen 80;

    # Serve 'Hello World!' at the root
    location / {
        return 200 'Hello World!';
    }

    # Redirect /redirect_me to the root with a 301 redirect
    location /redirect_me {
        return 301 http://$host/;
    }
}
  ",
  notify  => Service['nginx'],
}

# Ensure Nginx is reloaded to apply the new configuration
exec { 'reload_nginx':
  command     => 'systemctl reload nginx',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}
