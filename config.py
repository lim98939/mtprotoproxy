PORT = 443

# name -> secret (32 hex chars)
USERS = {
    "tg":  "271954e5da21e3652e332d6dbeb5f6fc",
    # "tg2": "0123456789abcdef0123456789abcdef",
}

MODES = {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": False,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
TLS_DOMAIN = "www.cloudflare-cn.com"

# Tag for advertising, obtainable from @MTProxybot
# https://t.me/telephcn
# AD_TAG = "f0b5afdf45d164c5794d7bf1f019425b"
# https://t.me/tgzh_vip
AD_TAG = "9cd18205e07716f93152af6d44366e13"

#若服务器内存为2g以上加入一下配置
TO_CLT_BUFSIZE = 262144
TO_TG_BUFSIZE = 262144