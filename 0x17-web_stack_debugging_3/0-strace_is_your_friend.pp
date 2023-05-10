# A puppet script to replae replaces "phpp" with "php"

$php_path = '/var/www/html/wp-settings.php'

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${php_path}",
  path    => ['/bin','/usr/bin']
}
