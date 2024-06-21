#!/usr/bin/env sh

commit_sha='2dbcaa1'
version='1.4.0'
tarball_name="libpcap-1.4.0-20130826git${commit_sha}.tar.gz"
upstream_url='https://github.com/the-tcpdump-group/libpcap.git'

rm -rf libpcap

git clone -q $upstream_url 2>&1 >/dev/null
rc=$?
if [ $rc -ne 0 ]; then
    echo 'error: can not clone upstream git'
    exit $rc
fi

cd libpcap

git reset --hard 2dbcaa1 2>&1 >/dev/null
rc=$?
if [ $rc -ne 0 ]; then
    echo 'error: can not reset HEAD to commit $commit_sha, invalid repository'
    exit $rc
echo
fi

echo $version > VERSION

./configure >/dev/null 2>&1
rc=$?
if [ $rc -ne 0 ]; then
    echo 'error: configure script failed, probably there are missing build dependencies'
    exit $rc
fi

make releasetar
mv libpcap-1.4.0.tar.gz $tarball_name

cd ..
cp libpcap/$tarball_name $tarball_name
rm -rf libpcap

exit 0

