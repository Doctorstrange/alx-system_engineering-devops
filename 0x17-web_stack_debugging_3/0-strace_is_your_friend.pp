# change line in a server

$path_file = '/var/www/html/wp-settings.php'

#replace occurrence of "phpp" with "php"

exec { 'replace_in_place':
  command => "sed -i 's/phpp/php/g' ${path_file}",
  path    => ['/bin','/usr/bin']
}
