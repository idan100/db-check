FROM centos
COPY . .
RUN yum -y install python2
RUN yum --enablerepo=extras install epel-release
RUN yum -y install python-pip
RUN pip install -r requirements.txt
CMD ["/bin/bash"]
