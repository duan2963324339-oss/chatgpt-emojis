import json,pathlib
p=pathlib.Path(__file__).parent/"emojis"/"index.json"
data=json.loads(p.read_text(encoding="utf-8"))
data["version"]=3
data["description"]="Sticker source catalog with individually HTTP-verified remote image URLs; copyright remains with creators."
url="https://stickershop.line-scdn.net/stickershop/v1/sticker/691386753/iPhone/sticker_key@2x.png"
entry={"id":"maltese-30890-691386753","collection":"线条小狗","package_id":30890,"sticker_id":691386753,"image_url":url,"source":"https://store.line.me/stickershop/product/30890/zh-Hant","creator":"Moonlab_studio","content_type":"image/png","http_verified":True,"user_visual_confirmed":True,"chat_inline_verified":False,"tags":["可爱","日常"],"license":"Copyright retained by original creator; link only, not rehosted"}
images=data.setdefault("images",[])
if not any(x.get("id")==entry["id"] for x in images):images.append(entry)
p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("registered",entry["id"],"total",len(images))
