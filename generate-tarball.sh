#! /bin/sh

rm -fr resources
git clone git://github.com/psi-plus/resources.git
rev=$(cd resources && git log -1 --pretty=%h sound)
pkgrev=$(date +%Y%m%d)git${rev}
psiver=0.16-${pkgrev}
tar -C resources/ -czf psi-plus-sounds-${psiver}.tar.gz sound

