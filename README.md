Exercise 1 (ex1)
================

## Description

This repo contains scripts for downloading MODIS active fire data and creating daily hotspot layers for each country.

## Installation

These installation instructions are subject to change.  Right now, since there are non-debian package dependencies, you can really extract the scripts to whatever directory you want.  The instructions below are suggested as they mirror Linux best practices for external packages.  Please be careful when installing gdal-bin and python-gdal packages as they may require different version of some packages than other programs, such as the OpenGeo Suite.  It is recommended to test this and other GDAL scripts within a vagrant environment first.

As root (`sudo su -`), for basic install execute the following:

```
apt-get update
apt-get install -y curl vim git
#==#
cd /opt
git clone https://github.com/pjdufour/ex1.git ex1.git
cp ex1.git/profile/ex1.sh /etc/profile.d/
```

You'll also want to install [NGINX](http://nginx.org/) to provide a server to publish the exported files:

```
apt-get install nginx
```

## Usage

```Shell
ex1-init-countries.sh 
ex1-modis-fires-collect.sh
ex1-modis-fires-export.py --output OUTPUT 
```

## Examples

```Shell
ex1-init-countries.sh
ex1-modis-fires-collect.sh
ex1-modis-fires-export.py --output '/var/www/hotspots'
```

## Contributing

We are not accepting pull requests for this repository.

## LICENSE

Copyright (c) 2015, Patrick Dufour
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of ex1 nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
