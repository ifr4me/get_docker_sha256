# get_docker_sha256
大部分从网上摘抄的，增加了对镜像sha256的获取。
利用 curl -I -X DELETE <protocol>://<registry_host>/v2/<repo_name>/manifests/<digest_hash>就可以删除私有docker registry 镜像了
eg: curl -I -X DELETE http://192.168.0.221:5000/v2/wordpress/manifests/sha256:b3a15ef1a1fffb8066d0f0f6d259dc7f646367c0432e3a90062b6064f874f57c
