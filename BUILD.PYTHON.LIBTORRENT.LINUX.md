## dependencies
apt update
apt install build-essential checkinstall
apt get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

## Python 3.7.2
cd /usr/local/src
wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz
tar xzf Python-3.7.2.tgz
cd Python-3.7.2
./configure --enable-optimizations
make install

## BOOST 1.69.0
cd /usr/local/src
wget https://dl.bintray.com/boostorg/release/1.69.0/source/boost_1_69_0.tar.bz2
tar jxf boost_1_69_0.tar.bz2
cd boost_1_69_0
./bootstrap.sh --prefix=/usr/local/
ln -s /usr/local/include/python3.7m /usr/local/include/python3.7
./b2 -j4 --with-python release install

## LIBTORRENT
cd /usr/local/src
wget https://github.com/joriscarrier/libtorrent/archive/libtorrent_1_1_12_python_jamfile.zip
unzip libtorrent_1_1_12_python_jamfile.zip
cd libtorrent-libtorrent_1_1_12_python_jamfile/bindings/python
/usr/local/src/boost_1_69_0/b2 -j4 address-model=64 libtorrent-link=static boost-link=static -sBOOST_ROOT=/usr/local/src/boost_1_69_0 release


