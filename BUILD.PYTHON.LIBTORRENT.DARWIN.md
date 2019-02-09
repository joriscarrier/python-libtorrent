## Command Line Tools

`xcode-select --install`

## Homebrew

`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

## OpenSLL

`brew install openssl`

## Python 3

`brew install python3`

## BOOST 1.69.0
`mkdir /usr/local/src`
`cd /usr/local/src`
`wget https://dl.bintray.com/boostorg/release/1.69.0/source/boost_1_69_0.tar.bz2`
`tar jxf boost_1_69_0.tar.bz2`
`cd boost_1_69_0`
`./bootstrap.sh --prefix=/usr/local`

## LIBTORRENT 1.1.12
`cd /usr/local/src`
`wget https://github.com/joriscarrier/libtorrent/archive/libtorrent_1_1_12_python_jamfile.zip`
`unzip libtorrent_1_1_12_python_jamfile.zip`
`cd libtorrent-libtorrent_1_1_12_python_jamfile/binding/python`
`/usr/local/src/boost_1_69_0/b2 -j4 address-model=64 libtorrent-link=static boost-link=static -sBOOST_ROOT=/usr/local/src/boost_1_69_0 release`
