## Visual Studio Community Edition

- Go to https://www.visualstudio.com/
- Download and run "Download Visual Studio Community Edition" (or another one based on licensing terms)
- Choose "Desktop development with C++", then "Install"

## chocolatey

We'll need this to install yasm (i don't why i cannot install yasm without this)
- Start Menu → All programs → Visual studio 2017 → Visual studio tools → VC → x64 Native tools command prompt
- `@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"`

## python

- Start Menu → All programs → Visual studio 2017 → Visual studio tools → VC → x64 Native tools command prompt
- choco install python


## git

We'll need this to cloning repositories (openssl, libtorrent, isa-l)
choco install git

## nasm

We'll need this to install Openssl

- Go to https://www.nasm.us/
- download nasm installer for windows 64bits
- right click on nasm-<version>-installer-x64.exe -> run as administrator

## perl

We'll need this to install Openssl

- Go to https://www.activestate.com/activeperl/downloads
- Download and run "Download ActivePerl for Windows (64-bit)"
- Choose a typical install


## Openssl

- Start Menu → All programs → Visual studio 2017 → Visual studio tools → VC → x64 Native tools command prompt
- cd /
- git clone https://github.com/openssl/openssl.git
- cd openssl
- git checkout tags/OpenSSL_1_1_0j
- set PATH=%PATH%;"c:\Program Files\NASM"
- `perl Configure VC-WIN64A`
- `nmake`
- `nmake install`


## 7-zip

We'll need this to extract `.7z` or `.tar.gz` archives.

- Go to http://www.7-zip.org/
- Download and run the installer

## Boost 1.69.0

- Go to http://www.boost.org/users/history/version_1_69_0.html
- Download and save `boost_1_69_0.7z`
- Right-click, 7-Zip → Extract To c:\boost_1_69_0
- Start Menu → All programs → Visual studio 2017 → Visual studio tools → VC → x64 Native tools command prompt
- `cd c:\boost_1_69_0`
- `bootstrap.bat`


## libtorrent 1.1.12

- Start Menu → All programs → Visual studio 2017 → Visual studio tools → VC → x86 Native tools command prompt
- cd /
- git clone https://github.com/joricarrier/libtorrent.git
- cd libtorrent
- git checkout libtorrent_1_1_12_python_jamfile
- `c:\boost_1_69_0\b2 -j4 address-model=64 libtorrent-link=static boost-link=static link=static runtime-link=static --hash crypto=openssl openssl-include="c:\Program Files\OpenSSL\include" openssl-lib="c:\Program Files\OpenSSL\lib" -sBOOST_ROOT=c:\boost_1_69_0 release`

