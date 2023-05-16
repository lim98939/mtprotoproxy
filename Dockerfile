FROM ubuntu:22.10

RUN sed -i 's#http://archive.ubuntu.com/#http://mirrors.tuna.tsinghua.edu.cn/#' /etc/apt/sources.list
RUN apt-get update --fix-missing  && apt-get install --no-install-recommends -y python3 python3-uvloop python3-pycryptodome python3-socks libcap2-bin ca-certificates && rm -rf /var/lib/apt/lists/*
RUN setcap cap_net_bind_service=+ep /usr/bin/python3.10

RUN useradd tgproxy -u 10000

USER tgproxy

WORKDIR /home/tgproxy/

COPY --chown=tgproxy mtprotoproxy.py config.py /home/tgproxy/

CMD ["python3", "mtprotoproxy.py"]
