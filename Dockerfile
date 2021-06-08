FROM centos
COPY . .
RUN yum -y install python3
RUN yum -y --enablerepo=extras install epel-release
RUN yum -y install python3-pip
ENTRYPOINT /bin/bash
