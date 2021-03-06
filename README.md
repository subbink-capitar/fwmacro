# fwmacro


## Description

fwmacro is a library for generating iptables/ip6tables rules and to generate input files for iptables-restore and ip6tables-restore.

The library comes with two scripts: fwmpp and fwmc

The fwmpp command processes the simplified rules to a set of ip[6]tables rules and fwmc compiles a set of ip[6]tables rules to a ip[6]tables-restore file.


## Usage

Typical setup/usage will be:

 * Create files with default chain sets in /etc/fwmacro/chains[4|6]/
 * Create a file with simplified rules in /etc/fwmacro/fw.rules
 * Compile these with: fwmpp /etc/fwmacro/fw.rules
 * Build restore files with: fwmc
 * Install iptables rules with: iptables-restore /etc/fwmacro/ipv4.rules
 * Install ip6tables rules with: ip6tables-restore /etc/fwmacro/ipv6.rules


## Installation

On Debian / Ubuntu you might want to use the .deb from the files section (also installs manuals).
 * wget https://github.com/keesbos/fwmacro/raw/master/files/python-fwmacro_0.9.4_all.deb

With easy_install:
 * easy_install fwmacro
 * easy_install https://github.com/keesbos/fwmacro/archive/master.zip
