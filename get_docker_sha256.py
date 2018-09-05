# coding=utf-8
# from __future__ import print_function
# def read_file(filename):
#     with open(filename) as f:
#         return [i.strip() for i in f]
#
#
# fl = open("missing.txt", 'w+')
# setAll = set(open("all2.txt", "r").readlines())
# print("all2.txt total line:",len(setAll))
# setNew = set(open("new2.txt", "r").readlines())
# print("new2.txt total line:",len(setNew))
#
# setTemp = setNew.difference(setAll)
# for user in list(setTemp):
#     fl.write(''.join(user))
#
# fl.close()

# from functools import reduce
#
# def fn(x,y):
#     return x * y
#
# def prod(list):
#     return reduce(fn,list)
#
# L1 = [1, 2, 3, 4]
# L2 = list(map(prod, L1))
# print(L2)
# total = 0
# for x in open("money.txt", "r").readlines():
#     total = total + int(x)
# print total
# from urllib import quote
# import requests
# requests.packages.urllib3.disable_warnings()
# import sys,re
# reload(sys)
# sys.setdefaultencoding('utf-8')
#
# URL1 = "http://kms.sys.wanmei.net/pages/viewpage.action"
# URL2 = ".html?pageId=38437967"
#
# for x in range(0,256,1):
#     #print chr(x)
#     html = requests.get(URL1 + quote(chr(x)) + URL2, verify=False)
#     print x,quote(chr(x)),html.status_code,html.__sizeof__()

# !/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import json
import traceback

repo_ip = '192.168.0.241'
repo_port = 5000

def getImagesNames(repo_ip, repo_port):
    docker_images = []
    try:
        url = "http://" + repo_ip + ":" + str(repo_port) + "/v2/_catalog"
        res = requests.get(url).content.strip()
        res_dic = json.loads(res)
        images_type = res_dic['repositories']
        for i in images_type:
            url2 = "http://" + repo_ip + ":" + str(repo_port) + "/v2/" + str(i) + "/tags/list"
            res2 = requests.get(url2).content.strip()
            res_dic2 = json.loads(res2)
            name = res_dic2['name']
            tags = res_dic2['tags']
            for tag in tags:
                docker_name = str(repo_ip) + ":" + str(repo_port) + "/" + name + ":" + tag
                docker_images.append(docker_name)
                url3 = "http://" + repo_ip + ":" + str(repo_port) + "/v2/" + str(i) + "/manifests/" + tag
                headers = {
                    'Accept':'application/vnd.docker.distribution.manifest.v2+json'
                }
                res3 = requests.get(url3, headers=headers).headers
                #res_dic3 = json.loads(res3)
                sha256 = res3['Docker-Content-Digest']
                print docker_name,sha256
    except:
        traceback.print_exc()
    return docker_images

a = getImagesNames(repo_ip, repo_port)
# print a

