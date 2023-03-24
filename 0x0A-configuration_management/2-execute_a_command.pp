#A Manifest that kills a process called me now

exec { 'killmenow':
  command => 'pkill killmenow',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'pgrep killmenow',
}
