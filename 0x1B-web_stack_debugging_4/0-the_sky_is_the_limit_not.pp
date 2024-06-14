# This Puppet manifest is used to configure Nginx to handle more concurrent connections.
exec { 'fix-nginx':
  command => '/bin/sed -i "s/worker_connections 768/worker_connections 4096/" /etc/nginx/nginx.conf && /bin/sed -i "s/worker_processes 1/worker_processes auto/" /etc/nginx/nginx.conf && systemctl reload nginx',
  path    => ['/bin', '/usr/bin'],
}
