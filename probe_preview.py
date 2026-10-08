import requests,json,pathlib,re,html
sources={"maltese":"https://store.line.me/stickershop/product/30890/zh-Hant","moonlab":"https://store.line.me/stickershop/product/32170448/zh-Hant","yuexinmiao":"https://www.sina.cn/media/5626763209"}
out=[]
for name,url in sources.items():
 try:
  r=requests.get(url,timeout=15,headers={"User-Agent":"Mozilla/5.0"})
  tags=re.findall(r"<meta\\s[^>]*>",r.text,re.I)
  tag=next((x for x in tags if "og:image" in x.lower()),"")
  m=re.search(r'content="([^"]+)"',tag)
  img=html.unescape(m.group(1)) if m else None
  ir=requests.get(img,timeout=15,stream=True) if img else None
  ct=ir.headers.get("content-type","") if ir else ""
  valid=bool(ir and ir.status_code==200 and ct.startswith("image/"))
  out.append({"name":name,"source":url,"page_status":r.status_code,"preview_url":img,"preview_status":ir.status_code if ir else None,"content_type":ct,"verified_image":valid,"note":"Page preview only, not necessarily an individual sticker."})
  print(name,r.status_code,valid,ct,img,flush=True)
 except Exception as e:out.append({"name":name,"source":url,"error":str(e)});print(name,"ERROR",str(e),flush=True)
pathlib.Path(__file__).with_name("preview_checks.json").write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding="utf-8")
