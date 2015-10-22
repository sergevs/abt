FROM sergevs42/debian7.amd64-base
MAINTAINER Serge at abrikus@gmail.com

RUN apt-get update && \
    apt-get install --no-install-recommends ca-certificates sudo equivs gawk nfs-common openssh-client -y && \
    wget https://github.com/sergevs/abt/releases/download/3.0.1-rc/abt_3.0.1_all.deb && \
    dpkg -i abt_3.0.0_all.deb ; \
    apt-get install --no-install-recommends -fy && \
    rm -f abt_3.0.0_all.deb && \
    apt-get remove mawk awk -y && \
    apt-get clean && \
    echo "%sudo  ALL=(ALL)       NOPASSWD: ALL" >> /etc/sudoers

COPY abtrc /etc/abt/
COPY user.init /usr/bin/

ENTRYPOINT ["/usr/bin/user.init"]
