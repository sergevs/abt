FROM sergevs42/centos7.x86_64-base
MAINTAINER Serge at abrikus@gmail.com

RUN yum -y install https://github.com/sergevs/abt/releases/download/3.0.0/abt-3.0.0-ssv1.el7.noarch.rpm && \
    yum -y install iproute hostname nfs-utils rpcbind && \
    yum clean all && \
    echo "%wheel  ALL=(ALL)       NOPASSWD: ALL" >> /etc/sudoers

COPY .rpmmacros /root/
COPY abtrc /etc/abt/
COPY user.init /usr/bin/

ENTRYPOINT ["/usr/bin/user.init"]
