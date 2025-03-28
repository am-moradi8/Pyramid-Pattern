{
  "log": {
    "level": "warn",
    "output": "box.log",
    "timestamp": true
  },
  "dns": {
    "servers": [
      {
        "tag": "dns-remote",
        "address": "udp://1.1.1.1",
        "address_resolver": "dns-direct"
      },
      {
        "tag": "dns-trick-direct",
        "address": "https://sky.rethinkdns.com/",
        "detour": "direct-fragment"
      },
      {
        "tag": "dns-direct",
        "address": "1.1.1.1",
        "address_resolver": "dns-local",
        "detour": "direct"
      },
      {
        "tag": "dns-local",
        "address": "local",
        "detour": "direct"
      },
      {
        "tag": "dns-block",
        "address": "rcode://success"
      }
    ],
    "rules": [
      {
        "domain": [
          "mw6.festivalfoods.ir",
          "www.speedtest.net"
        ],
        "server": "dns-direct"
      },
      {
        "domain": "cp.cloudflare.com",
        "server": "dns-remote",
        "rewrite_ttl": 3000
      }
    ],
    "final": "dns-remote",
    "static_ips": {
      "sky.rethinkdns.com": [
        "104.21.69.44",
        "172.67.204.84",
        "2606:4700:3031::ac43:cc54",
        "2606:4700:3032::6815:452c",
        "104.17.147.22",
        "104.17.148.22",
        "104.21.83.62",
        "172.67.214.246",
        "2606:4700:3030::6815:533e",
        "2606:4700:3030::ac43:d6f6"
      ]
    },
    "independent_cache": true
  },
  "inbounds": [
    {
      "type": "tun",
      "tag": "tun-in",
      "mtu": 9000,
      "inet4_address": "172.19.0.1/28",
      "auto_route": true,
      "strict_route": true,
      "endpoint_independent_nat": true,
      "stack": "mixed",
      "sniff": true,
      "sniff_override_destination": true
    },
    {
      "type": "mixed",
      "tag": "mixed-in",
      "listen": "127.0.0.1",
      "listen_port": 2334,
      "sniff": true,
      "sniff_override_destination": true
    },
    {
      "type": "direct",
      "tag": "dns-in",
      "listen": "127.0.0.1",
      "listen_port": 6450
    }
  ],
  "outbounds": [
    {
      "type": "selector",
      "tag": "select",
      "outbounds": [
        "auto",
        "@v2ray313 کانالمون 🥰 § 0",
        "@v2ray313 کانالمون 👄 § 1",
        "@v2ray313 کانالمون 🥹 § 2",
        "@v2ray313 کانالمون 🔥 § 3",
        "@v2ray313 کانالمون ☺️ § 4",
        "@v2ray313 کانالمون 😬 § 5"
      ],
      "default": "auto"
    },
    {
      "type": "urltest",
      "tag": "auto",
      "outbounds": [
        "@v2ray313 کانالمون 🥰 § 0",
        "@v2ray313 کانالمون 👄 § 1",
        "@v2ray313 کانالمون 🥹 § 2",
        "@v2ray313 کانالمون 🔥 § 3",
        "@v2ray313 کانالمون ☺️ § 4",
        "@v2ray313 کانالمون 😬 § 5"
      ],
      "url": "http://connectivitycheck.gstatic.com/generate_204",
      "interval": "10m0s",
      "idle_timeout": "1h40m0s"
    },
    {
      "type": "vmess",
      "tag": "@v2ray313 کانالمون 🥰 § 0",
      "server": "186.190.215.93",
      "server_port": 22324,
      "uuid": "04621bae-ab36-11ec-b909-0242ac120002",
      "security": "auto",
      "authenticated_length": true
    },
    {
      "type": "vless",
      "tag": "@v2ray313 کانالمون 👄 § 1",
      "server": "188.114.97.155",
      "server_port": 80,
      "uuid": "7c9e3c1d-a360-4429-9189-e45a98de7fde",
      "transport": {
        "type": "ws",
        "path": "/Telegram@v2rayngv16/",
        "headers": {
          "Host": "showmo.wfft.ir"
        },
        "max_early_data": 2560,
        "early_data_header_name": "Sec-WebSocket-Protocol"
      },
      "packet_encoding": ""
    },
    {
      "type": "vless",
      "tag": "@v2ray313 کانالمون 🥹 § 2",
      "server": "mw6.festivalfoods.ir",
      "server_port": 443,
      "uuid": "91e0b515-f19c-4491-b849-0f562fc19f23",
      "tls": {
        "enabled": true,
        "server_name": "mw6.festivalfoods.ir",
        "utls": {
          "enabled": true,
          "fingerprint": "chrome"
        },
        "reality": {
          "enabled": true,
          "public_key": "GB7zayJb4ApVwXxUijmcNqONDamLIyeUL1OwqfX4ulQ",
          "short_id": "9a77"
        }
      },
      "packet_encoding": ""
    },
    {
      "type": "vless",
      "tag": "@v2ray313 کانالمون 🔥 § 3",
      "server": "www.speedtest.net",
      "server_port": 443,
      "uuid": "5e1306ff-3ffa-4166-89ab-1a06ff42eca6",
      "tls": {
        "enabled": true,
        "server_name": "www.speedtest.net.www.google.com.bing.com.visa.com.tls.htr.ddns-ip.net",
        "utls": {
          "enabled": true,
          "fingerprint": "chrome"
        }
      },
      "transport": {
        "type": "ws",
        "path": "/Telegram-XV2ry2",
        "headers": {
          "Host": "www.speedtest.net.www.google.com.bing.com.visa.com.tls.htr.ddns-ip.net"
        },
        "max_early_data": 512,
        "early_data_header_name": "Sec-WebSocket-Protocol"
      },
      "packet_encoding": ""
    },
    {
      "type": "vless",
      "tag": "@v2ray313 کانالمون ☺️ § 4",
      "server": "188.114.97.3",
      "server_port": 80,
      "uuid": "c5293efa-28f8-4a0f-8f34-541078970cee",
      "transport": {
        "type": "ws",
        "path": "/SIGrNRCU4ongDlz4",
        "headers": {
          "Host": "gozargah.validbv7996.ir"
        },
        "max_early_data": 2560,
        "early_data_header_name": "Sec-WebSocket-Protocol"
      },
      "packet_encoding": ""
    },
    {
      "type": "vless",
      "tag": "@v2ray313 کانالمون 😬 § 5",
      "server": "84.32.9.19",
      "server_port": 8880,
      "uuid": "df0680ca-e43c-498d-ed86-8e196eedd012",
      "transport": {
        "type": "grpc",
        "idle_timeout": "15s",
        "ping_timeout": "15s"
      },
      "packet_encoding": ""
    },
    {
      "type": "dns",
      "tag": "dns-out"
    },
    {
      "type": "direct",
      "tag": "direct"
    },
    {
      "type": "direct",
      "tag": "direct-fragment",
      "tls_fragment": {
        "enabled": true,
        "size": "1-500",
        "sleep": "0-500"
      }
    },
    {
      "type": "direct",
      "tag": "bypass"
    },
    {
      "type": "block",
      "tag": "block"
    }
  ],
  "route": {
    "rules": [
      {
        "rule_set": [
          "geoip-ir",
          "geosite-ir"
        ],
        "outbound": "direct"
      },
      {
        "inbound": "dns-in",
        "outbound": "dns-out"
      },
      {
        "port": 53,
        "outbound": "dns-out"
      },
      {
        "clash_mode": "Direct",
        "outbound": "direct"
      },
      {
        "clash_mode": "Global",
        "outbound": "select"
      }
    ],
    "rule_set": [
      {
        "type": "remote",
        "tag": "geoip-ir",
        "format": "binary",
        "url": "https://raw.githubusercontent.com/hiddify/hiddify-geo/rule-set/country/geoip-ir.srs",
        "update_interval": "120h0m0s"
      },
      {
        "type": "remote",
        "tag": "geosite-ir",
        "format": "binary",
        "url": "https://raw.githubusercontent.com/hiddify/hiddify-geo/rule-set/country/geosite-ir.srs",
        "update_interval": "120h0m0s"
      }
    ],
    "final": "select",
    "auto_detect_interface": true,
    "override_android_vpn": true
  },
  "experimental": {
    "cache_file": {
      "enabled": true,
      "path": "clash.db"
    },
    "clash_api": {
      "external_controller": "127.0.0.1:6756",
      "secret": "LxUVl1K04V1po-XU"
    }
  }
}
