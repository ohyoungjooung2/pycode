kt@oyj:/mnt/c/Users/SDH/ec2-run$ cat start-vas-instances.yaml
---
- name: provision aws ec2 instances for vas cluster -바스 클러스터용 ec2 프로비저닝
  hosts: local
  connection: local
  gather_facts: False
  vars:

  tasks:
     - name: start specific number of multiple instances
       amazon.aws.ec2_instance:
         #instance_type: t3.small
         instance_type: c6i.4xlarge
         launch_template:
           name: "create-ec2-rocky8-golden-image"
           version: 13
             #vpc_subnet_id: subnet-070005fc17a34f947
         vpc_subnet_id: subnet-0232d78b686e2d657
         volumes:
           - device_name: /dev/sda1
             ebs:
               volume_size: 300
               delete_on_termination: true
               volume_type: gp3
         region: ap-northeast-2
         profile: test
         network:
           assign_public_ip: false
           security_groups: ["sg-037be9a58e9800cc5","sg-02c26a473394a64eb"]
           private_ip_address: "{{ item.ip }}"

         state: present
         tags:
           tst: tst
           Name: "{{ item.hname }}"
       with_items:
         - { hname: master1, ip: 10.71.164.150 }
         - { hname: master2, ip: 10.71.164.151 }
         - { hname: master3, ip: 10.71.164.152 }
         - { hname: worker1, ip: 10.71.164.153 }
         - { hname: worker2, ip: 10.71.164.154 }
         - { hname: worker3, ip: 10.71.164.155 }
         - { hname: worker4, ip: 10.71.164.156 }
         - { hname: worker5, ip: 10.71.164.157 }
         - { hname: worker6, ip: 10.71.164.158 }
         - { hname: worker7, ip: 10.71.164.159 }
         - { hname: db1, ip: 10.71.164.160 }
         - { hname: db2, ip: 10.71.164.161 }
