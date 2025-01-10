# This Puppet manifest kills a process named 'killmenow' using the pkill command.
exec { 'kill_process_killmenow':
  command   => 'pkill killmenow',
  path      => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
  onlyif    => 'pgrep killmenow',
  logoutput => true,
}
