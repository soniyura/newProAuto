import requests

url = "https://play.google.com/log?format=json&hasfast=true&authuser=0"

payload = "[[1,null,null,null,null,null,null,null,null,null,[null,null,null,null,\"ru-UA\",null,null,null,[[[\"Not A(Brand\",\"99\"],[\"Google Chrome\",\"121\"],[\"Chromium\",\"121\"]],0,\"macOS\",\"12.7.3\",\"x86\",\"\",\"121.0.6167.184\"],[1,0,0,0,0]]],407,[[\"1708341177919\",null,null,null,null,null,null,\"[538,1708341177919000,\\\"!WVqlWgLNAAY9UbWqHVFChe9rQ9B-d-Q7ADQBEArZ1GiKJvG-edaotgiJiWSyDjnDsDVN5fvbiRtmg8bHXxbdy_2nfNSt_dhybZwmhTC2AgAAAWpSAAAABGgBB5kE9vzHnEGXljGiBxJ04NVibRLq5K2d4Ofa9dKllvhpcJ7xvC5tUlGnhz3IuxP-u-PqtsTDMVHOIhnaD_eXV9kplyQ0NGOnpQL8PFHs42tvmGz7cCm3eQ59EG6bXvldxeEzq8FplLTdFRbQXxj2saQhK5jQwhQ6rLW6xbtErMqo96TiEz5bHS-sRTRlO29XSkyaE7_tfStzGlKMI_gCVDj0M3ssoju1ijjCT-IWteSW_lgIcLs8tWNXCfgd6tRvA5tU1a88lBqRhGfzc3zOlNixTdMw6zXgI3NeVXa9atP1PPffagy6RyXS2JcNA7tRY_aK-sojJ_GcVYR9T8u8v0h4QRMVFCAML3wZl_2gPn9XfJ1NyWbGVq-bRkzqtLX-wKHnSLT8o4qMeHhoE7CGwKUyselxqYZl2e0poY3O74RQBRipkau5TWHFgz8H5IHqJdsnd0mQi9vG_EUXlAW6mwwJOMmwzENtdmXQZ_G3dqAU4ohqvFzkrP_9epmQ5ifTJF9cUDUoGkjzDGwEqaQnYlBCjuDV1m8fS37XcOfBaWKVRp9Y6Z2BUWCyJFsh5m5B-HYgqzBE_i6GFeAZFv8egxwoZiLPM7QqGqjX22bG6LTvLKuLFQ21EUgID1aKdt1MceDTwofeIfIol5xwi6uK7VoJcxzLDNsVtq5DIk3FEEDu5qhBRxRmNfUNKdol1o8uwGXEWYxIFWeVNY3P_rrdUdax9Syu-iEP0HdWQ3Z8OspE2T6hib_mTxDFVFeaIDkHCnF9KRYwUcHshBVZtXk-m5pTjl4TIWe_vH7HaD8mnCex81orH_MpGQ-eEJZWQW8Q3nGfDpXZhPTgI7hopWaLbS1byI5ioTCAf5FCBXb_xUXwofLHCpQUa6AkP_OOo3YuKW9I9Un9bBOIsY6GwFt9ccTJ0s_f9hX6w4sQCkgkv_ZeTs_qxwFlb6cUmDJD0kXyZUhbLmUENHCb5r_bWbYYzAEThpWUPoMKC7ODtq9-95BHEGEQYfxqOZUyEX0ErE_euO5xd5xrAbwDAb0D2vWXC2Io53MW-uh9cdtjBxMCGflu5jAYCTxbsBZyHtgjbEcjUe6uKDd9_M0zyoJu55TJPiMarCLG9qiaKJ_Y2bUqqBcDFNHp7H_suTvKfAc4c6zbpfOKIeVWWAB4D4rGBsu4oa6vg5LwAKNEbcxEOH-dul2uFXUVUMIKhdql6AL3kWgzA-B--JMib7RCHxN5SEXybBx9BwugV1UYJkiiUZpaX8W8vCaL2CifqyVnRJMRO4hKk3AKq5Je9lbifCROt8iREqz1_-Z8Dg25-xF7SLZfOgOSLHmUvL2zyEDhf-ri-WSFGQq5VhO6l0ab2EKPoeDoTtyS9ypxkfAler6Hj3Kjc9Gm8K6fzRTa3aThJxIfUw06-w2-KwPjKci9Yxx15kOk_hOhfYBPdjYhaNlt0p-uy7jnU42rZ6orhSqvHk6YaHtLBc60SnOZC4eAmffNdKjqGplTkchlNKcPTdnQQkZvmf3CjGZt6SN9Y5xL3kIZZRN03M3ZKfzdNwipSS6lc0lE3jAGLiG4AT2fj70XRoASaudGqDPnoljLvjoamdRUM9uZiNK9C_yfM1vcJ5CBd2mr7nqavKMqsvRyohttdDupRCS43cZBcOVh0-tRDLbkuAzEzWK9u4lJZXCAkhVlxyGg9r_S4LTTs-DM5H8\\\",1009677010,0]\",null,null,null,null,null,null,-7200,null,null,null,null,null,1]],\"1708341177921\"]"
headers = {
  'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
  'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
  'X-Goog-AuthUser': '0',
  'sec-ch-ua-mobile': '?0',
  'Authorization': 'SAPISIDHASH 35274ea0e44ba6ca7bea93408198122621697afe',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
  'sec-ch-ua-platform': '"macOS"',
  'Accept': '*/*'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)


print(response.text)
