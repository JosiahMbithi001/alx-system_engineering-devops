# A puppet Manuscript replacing A Line in A File or Server

$edit_file = '/var/www/html/wp-settings.php'

Replaces "phpp" with "php"

exec { 'line_replace':
	command => "sed -i 's/phpp/php/g'", $(edit_file)",
	path => ['/bin','/usr/bin']
}
