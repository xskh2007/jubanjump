# -*- coding: utf-8 -*-
#
from jenkinsapi.jenkins import Jenkins as Jenkins2
import jenkins
import time
from celery import shared_task





@shared_task
def deployjenkins1():
    print("deploying.....")

@shared_task
def mongoexecute(uid):
    print(uid+"1111111111111")

@shared_task
def deployjenkins(env):
    server = jenkins.Jenkins(jks_url, username, password)
    server2 = Jenkins2(jks_url, username, password)
    jobnames=[]
    joblists=server2.get_jobs()
    for i in joblists:
        if i[0].find(env)>=0:
            jobnames.append(i[0])
    for i in jobnames:
        print (i)
        server2.build_job(i,params={"host":"all"})
        # job_lastBuild_number = server.get_job_info(i)['lastBuild']['number']
        # print(server.get_build_info(i, job_lastBuild_number)['building'])
        while True:
            job_lastBuild_number=server.get_job_info(i)['lastBuild']['number']
            building=server.get_build_info(i, job_lastBuild_number)['building']
            if building is True:
                print(i,"is building")
                time.sleep(10)
            if building is False:
                result=server.get_build_info(i, job_lastBuild_number)['result']
                if result=="SUCCESS":
                    print("build ",i,result)
                    break
                else:
                    # result=="FAILURE"
                    print(result)
                    exit(1000)
                print (i,result)
    print (jobnames)



# mycl_deploy()



