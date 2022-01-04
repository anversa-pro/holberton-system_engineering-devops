# Install puppet-lint specific version using Puppet

package { 'puppet-lint':
  ensure   => '2.5.0',
  provider => 'gem',
  source   =>  'https://rubygems.org',
}
