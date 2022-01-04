# Kills a process named 'killmenow' using puppet

exec { 'killit':
  command  => 'pkill killmenow',
  provider => 'shell',
  }
