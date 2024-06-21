#!/bin/bash
baseos=http://archive.kernel.org/centos-vault/centos/6/os/Source/SPackages
updates=http://archive.kernel.org/centos-vault/centos/6/updates/Source/SPackages

curl -L \
  -X PATCH \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $githuapikey" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/andykimpe/myrpmspec/releases/assets/40450 \
  -d '{"name":"get-package.sh","label":"binary"}'


curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $githuapikey" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/andykimpe/myrpmspec/releases




decompte() {
    i=$1
    echo "please wait or press key for continue"
    for _ in `seq $i`; do
        if ! read -rs -n1 -t1 ; then echo -e "\033[31m\r "$i" \c\033[0m"; else break; fi
        i=$(expr $i - 1)
    done
    echo -e "\033[32m\033[0m"
}
rm -f *.rpm
check1=$(wget -S --spider $updates/$1 2>&1 | grep -q 'HTTP/1.1 200 OK' && echo SUCCESS || echo FAIL)
check2=$(wget -S --spider $baseos/$1 2>&1 | grep -q 'HTTP/1.1 200 OK' && echo SUCCESS || echo FAIL)
if [ $check1 == "SUCCESS" ]; then
    wget $updates/$1
elif [ $check2 == "SUCCESS" ]; then
    wget $baseos/$1
else
    echo not found file
    echo 0
fi
packagename=$(rpm -qp --queryformat '%{NAME}' *.rpm)
mkdir -p $packagename
cd $packagename
rm -rf *
rpm2cpio ../*.rpm | cpio -idmv
echo "folder $packagename"
#decompte 600
rm -rf *.tar.*
rm -rf *.tgz.*
rm -rf *.zip.*
rm -rf *.7z.*
rm -rf *.rar.*
rm -rf *.rpm.*
cd ..
rm -f *.rpm
git add --all *
git commit -a -m "add original $packagename package el6"
git push origin el6






















