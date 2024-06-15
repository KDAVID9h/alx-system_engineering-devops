# This Puppet manifest is used to increase the file descriptor limits for the user 'holberton'.
exec { 'change-os-configuration-for-holberton-user':
  command => 'echo "holberton soft nofile 65535\nholberton hard nofile 65535" >> /etc/security/limits.conf && echo "session required pam_limits.so" >> /etc/pam.d/common-session',
  path    => ['/bin', '/usr/bin'],
}
