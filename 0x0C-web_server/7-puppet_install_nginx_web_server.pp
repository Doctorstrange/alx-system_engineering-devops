# Nginx package
package { 'nginx':
  ensure => installed,
}

#Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Create Hello World! page
file { '/var/www/html/index.html':
  content => "<html><body>Hello World!</body></html>",
  mode    => '0644',
  require => Package['nginx'],
}

# Create 404 page
file { '/var/www/html/404.html':
  content => "<html><body>Error 404: Ceci n'est pas une page</body></html>",
  mode    => '0644',
  require => Package['nginx'],
}

# Configure Nginx server
file { '/etc/nginx/sites-available/default':
  content => "
server {
  listen 80;
  server_name _;

  location /redirect_me {
    return 301 https://example.com/new_page;
  }

  location / {
    root /var/www/html;
    index index.html;
    error_page 404 /404.html;
    location = /404.html {
      internal;
    }
  }
}",
  mode    => '0644',
  require => Package['nginx'],
  notify  => Service['nginx'],
}
