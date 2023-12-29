docker network create scada-network --subnet=192.168.1.0/24
docker run --name openplc_host --rm -d -p 8080:8080 -p 502:502 --privileged openplc
docker network connect scada-network openplc_host --ip 192.168.1.2
docker run --name scadabr_host --rm -d -p 9090:9090 --privileged scadabr
docker network connect --ip 192.168.1.3 scada-network scadabr_host
xhost +local:docker
docker run --name factory_host -ti --rm -d -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --privileged factory
docker network connect --ip 192.168.1.4 scada-network factory_host

