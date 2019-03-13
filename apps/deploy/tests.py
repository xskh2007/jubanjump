from django.test import TestCase

# Create your tests here.

from jenkinsapi.jenkins import Jenkins as Jenkins2
import jenkins

# pro_name="dsd"

def mycl_deploy():
    # giturl = "git@gitlab.lark.wiki:nbgold/"
    # template_xml = "/root/jumpserver-master/tmp/jenkins_job.xml"
    # view_name = env
    # server = jenkins.Jenkins('http://192.168.2.169:8080/jenkins/', username='admin', password='zzjr#2015')

    server2 = Jenkins2('http://jks_online.51juban.com', username='admin', password='juban@2018')


    # job_list = ["bank", "mldp", "pms", "cms", "pay", "member", "weapon", "trade", "wealth", "statistics", "bops",
    #             "napp", "site", "crm", "channel", "tiger", "rams", "activity", "api", "eagle", "squirrel", "wap",
    #             "dragon", "tengu"]
    #
    #
    # for i in job_list:
    #
    #     ### 批量发布job by python-jenkins
    #     # parameters = {"model":i,"branch":"origin/master"}
    #     # deploy=server.build_job(view_name+i,parameters=parameters)
    #
    #     ### 批量发布job by jenkinsapi
    #     parameters = {"model": i, "branch": "origin/master"}
    #     deploy = server2.build_job(view_name + i, params=parameters)

    joblist=server2.get_jobs()
    for i in joblist:
        print(i)

mycl_deploy()