# This Puppet manifest installs Flask 2.1.0 and Werkzeug 2.1.1 using pip.
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
}

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip',
  require  => Package['flask'], # Ensure Werkzeug is installed after Flask
}
