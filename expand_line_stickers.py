import requests,json,pathlib
root=pathlib.Path(__file__).parent
catalog=root/"emojis"/"index.json"
data=json.loads(catalog.read_text(encoding="utf-8"))
session=requests.Session()
packages=[30890]
for pkg in packages:
 meta_url=f"https://stickershop.line-scdn.net/stickershop/v1/product/{pkg}/iphone/productInfo.meta"
 r=session.get(meta_url,timeout=20);r.raise_for_status();meta=r.json()
 for sticker in meta.get("stickers",[]):
  sid=sticker["id"]
  url=f"https://stickershop.line-scdn.net/stickershop/v1/sticker/{sid}/iPhone/sticker_key@2x.png"
  try:
   response=session.get(url,timeout=12,stream=True)
   signature=next(response.iter_content(8),b"")
   valid=response.status_code==200 and response.headers.get("content-type","").startswith("image/png") and signature.startswith(bytes.fromhex("89504e470d0a1a0a"))
   response.close()
  except requests.RequestException:valid=False
  if valid:
   entry={"id":f"maltese-{pkg}-{sid}","collection":"线条小狗","package_id":pkg,"sticker_id":sid,"image_url":url,"source":f"https://store.line.me/stickershop/product/{pkg}/zh-Hant","creator":"Moonlab_studio","content_type":"image/png","http_verified":True,"user_visual_confirmed":sid==691386753,"chat_inline_verified":False,"tags":["待人工标注"],"license":"Original creator retains copyright; URL reference only"}
   items=data.setdefault("images",[])
   match=next((x for x in items if x.get("id")==entry["id"]),None)
   if match:
    match["http_verified"]=True
   else:items.append(entry)
  print(sid,"PASS" if valid else "FAIL",flush=True)
catalog.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("TOTAL_VERIFIED",sum(x.get("http_verified",False) for x in data["images"]),flush=True)
