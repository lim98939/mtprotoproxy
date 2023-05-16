# Async MTProto Proxy #

Fast and simple to setup MTProto proxy written in Python.

## Starting Up ##
 
1. `yum install git python3 -y ;python3 -m pip install --upgrade pip; pip install uvloop pycrypto pycryptodome cryptogrpaphy `   
2. `git clone -b stable https://github.com/lim98939/mtprotoproxy-v.git; cd mtprotoproxy`
3. *(optional, recommended)* edit *config.py*, set **PORT**, **USERS** and **AD_TAG**
4. `docker-compose` 安装   
`sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose `  
`sudo chmod +x /usr/local/bin/docker-compose`  
5. docker-compose version ：用于查看当前的版本  
docker-compose ps -a 查看当前启动服务  
docker-compose build 用于docker-compose文件中描述的build构建镜像  
docker-compose up 启动服务  
docekr-compose stop 停止服务  
docker-compose start 启动停止的服务  
docker-compose run 启动docker-compose.yml描述的一个service  
docker-compose restart 重启服务  
docker-compose logs 查看日志  
docker-compose down 下线服务  
docker-compose pull 拉取镜像  
docker-compose push 推送镜像到仓库  
更多命令参考 docker-compose help
4. `docker-compose up -d` (or just `python3 mtprotoproxy.py` if you don't like Docker)
5. *(optional, get a link to share the proxy)* `docker-compose logs`

![Demo](https://alexbers.com/mtprotoproxy/install_demo_v2.gif)

## Channel Advertising ##

To advertise a channel get a tag from **@MTProxybot** and put it to *config.py*.

## Performance ##

The proxy performance should be enough to comfortably serve about 4 000 simultaneous users on
the VDS instance with 1 CPU core and 1024MB RAM.

## More Instructions ##

- [Running without Docker](https://github.com/alexbers/mtprotoproxy/wiki/Running-Without-Docker)
- [Optimization and fine tuning](https://github.com/alexbers/mtprotoproxy/wiki/Optimization-and-Fine-Tuning)

## Advanced Usage ##

The proxy can be launched:
- with a custom config: `python3 mtprotoproxy.py [configfile]`
- several times, clients will be automaticaly balanced between instances
- with uvloop module to get an extra speed boost
- with runtime statistics exported to [Prometheus](https://prometheus.io/)
