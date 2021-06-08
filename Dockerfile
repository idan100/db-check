FROM centos
COPY . .
RUN yum -y install python2
RUN yum -y --enablerepo=extras install epel-release
RUN yum -y install python3-pip
RUN python2 -V
RUN pip -V
CMD ["/usr/bin/bash"]
