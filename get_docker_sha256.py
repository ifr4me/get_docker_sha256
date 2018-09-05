# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author ifr4me

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

