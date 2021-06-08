FROM centos
COPY . .
RUN yum -y install python2
RUN yum -y --enablerepo=extras install epel-release
RUN yum -y install python3-pip
CMD ["/usr/bin/bash"]
