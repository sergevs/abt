FROM centos:7
MAINTAINER Serge at abrikus@gmail.com

RUN yum -y --setopt=tsflags=nodocs install https://github.com/sergevs/abt/releases/download/3.0.1/abt-3.0.1-ssv1.el7.noarch.rpm && \
    yum -y --setopt=tsflags=nodocs install http://mirror.yandex.ru/epel/7Server/x86_64/e/epel-release-7-8.noarch.rpm && \
    yum -y --setopt=tsflags=nodocs install iproute hostname nfs-utils rpcbind && \
    yum clean all && \
    echo "%wheel  ALL=(ALL)       NOPASSWD: ALL" >> /etc/sudoers

RUN sed -i -e 's/el7.centos/el7/' /etc/rpm/macros.dist
COPY .rpmmacros /root/
COPY abtrc /etc/abt/
COPY user.init /usr/bin/

ENTRYPOINT ["/usr/bin/user.init"]
