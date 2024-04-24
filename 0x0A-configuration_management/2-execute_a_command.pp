exec { 'kill_process':
  command     => 'pkill killmenow',
  path        => ['/usr/bin', '/bin'],  # Specify the path if necessary
  refreshonly => true,  # Only execute the command when notified
}
