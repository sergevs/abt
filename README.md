# Advanced Build Tool - abt

Advanced Build Tool is a shell scripts that simplify packages builds from a version control system or a local directory.

# Overview

Abt is developed to build a distribution packages directly from a version control system. 
The latest version is integrated with docker so only functional docker is required to start build packages. 

# Features

* Supported packaging systems: rpm, deb
* Version control systems integration: git, svn
* Build a project from arbitrary branch or tag
* Build flow customization for a particular project

Modular functions design allows easy implementation of other packaging systems or additional features.

# Description

The default build work flow provides the following stages:
* checkout a project and optional required modules from a version control system
* prepare build environment: install required packages which specified in rpm spec or deb control file 
* perform package(s) build
* publish packages to a repository. directory **repos** in home of the user is configured by default

# Getting started

While ready to use abt packages are provided at [release page](https://github.com/sergevs/abt/releases/latest) and can be
installed on a host or VM, the recommended way is to use prepared docker images.

1. Install and configure docker with non-root access for the user which will build packages. Please refer to appropriate for your OS documentation.
Verify installation:
   ```shell
   docker run --rm -it hello-world
   ```
2. Download abt.docker script and put it to appropriate location. As an instance:
   ```shell
   mkdir ~/bin
   curl -o ~/bin/abt.docker https://raw.githubusercontent.com/sergevs/abt/master/Docker/abt.docker
   chmod +x ~/bin/abt.docker
   ```
3. In the order to build rpm packages it's required to define **%packager** macro, like that ( replace "Your name" an "your email" appropriately ):
   ```shell
   echo "%packager Your name <your email>" >> ~/.rpmmacros
   ```
4. Ready to build packages. Verify to build abt itself:
   ```shell
   ~/bin/abt.docker sergevs42/centos7.x86_64-abt -v 3.1.2 sergevs/abt
   find ~/DockerBuild/repos 
   ```
# Customization 

It's possible to customize build behavior via various ways.

1. **DADD_OPTS** environment variable allow to supply additional options to container build environment. As an instance you can provide additional repositories.
   ```shell
   export DADD_OPTS='-v<path to yum.repo>:/etc/yum.repos.d/additional.repo'
   ```
2. [~/.abtrc](abtrc) allows to customize various aspects of abt
3. Customize [abt.docker](Docker/abt.docker) script according to your needs

# Options
  
See also:
```shell
abt.docker

Usage: Docker/abt.docker <docker image> -v <version> [OPTIONS] <vcs module path>

Supported images are:
NAME                                DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
sergevs42/centos6.x86_64-abt        abt ( https://github.com/sergevs/abt ) ima...   0                    [OK]
sergevs42/centos7.x86_64-abt        abt ( https://github.com/sergevs/abt ) ima...   0                    [OK]
sergevs42/debian8.amd64-abt         abt ( https://github.com/sergevs/abt ) ima...   0                    [OK]
sergevs42/debian9.amd64-abt         abt ( https://github.com/sergevs/abt ) ima...   0                    [OK]
sergevs42/debian7.amd64-abt         abt ( https://github.com/sergevs/abt ) ima...   0                    [OK]
```

And help for a particular image:
```shell
abt.docker sergevs42/debian8.amd64-abt -h

### Docker home is /home/builder/. ###

### user init ###

INFO: setting up container hostname to debian8.amd64-abt
Usage: abt -v <version> [OPTIONS] <vcs module path>

Options:
           [-a <release> ]
           [-b <trunk|branch|tag> ] 
           [-c <abt filename> ] 
           [-d <debug level> ]
           [-e <change log entry> ]
           [-h ]
           [-l <enable logging> ]
           [-n <vcs revision> ]
           [-o <build from spec file> ]
           [-m 0|1|<mock config> ]  0 - don't use mock, 1 - use mock, <mock config> - config file without arch and cfg extension
           [-p <rpmbuild  options> ]
           [-P rpm|deb ] package type to build
           [-r <repository> ]
           [-s <skip stages> ] 
           [-t <config type> ]
           [-u <vcs base URL> ]
           [-v <version>]
           [-A "module alias"]
           [-D "rpm macros"]
           [-C <full path to additional configuration file> (overrides /etc/abt/abtrc and ~/.abtrc)
           [-S <save build environment>]
           [-V [svn|git] version control system]

Default stages are:
Stage   1 => vcsPrepare
Stage   2 => pkgInitEnv
Stage  45 => debInstallDeps
Stage  50 => debBuild
Stage  70 => debRepoCopy
Stage  90 => cleanUp
```
# Known projects ready to build

* [sergevs/abt](https://github.com/sergevs/abt)
* [sergevs/net-snmp-subagent-shell](https://github.com/sergevs/net-snmp-subagent-shell)
* [newsgate/Server](https://github.com/newsgate/Server), repository customization is required
* [yandex/ClickHouse](https://github.com/yandex/ClickHouse), build verified for **sergevs42/debian9.amd64-abt** image, **v1.1.54289-stable** version(tag)
