FROM centos:6
MAINTAINER Serge at abrikus@gmail.com

RUN yum -y --setopt=tsflags=nodoc install https://github.com/sergevs/abt/releases/download/3.0.1/abt-3.0.1-ssv1.el6.noarch.rpm && \
    yum -y --setopt=tsflags=nodoc install http://mirror.yandex.ru/epel/6Server/x86_64/epel-release-6-8.noarch.rpm && \
    yum -y --setopt=tsflags=nodoc install iproute hostname nfs-utils rpcbind openssh-clients && \
    yum clean all && \
    echo "%wheel  ALL=(ALL)       NOPASSWD: ALL" >> /etc/sudoers

COPY .rpmmacros /root/
COPY abtrc /etc/abt/
COPY user.init /usr/bin/

ENTRYPOINT ["/usr/bin/user.init"]
