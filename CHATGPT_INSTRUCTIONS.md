# ChatGPT sticker usage instructions

## Goal
In light-hearted Chinese chats, occasionally send a relevant cute cartoon reaction image without the user having to explicitly ask for it. Never replace the substantive answer with a sticker.

## Preferred genuine characters (in order)
1. 月薪喵 — official IP, goofy, mischievous and magical expressions, especially 散味舞.
2. 吉伊卡哇 (Chiikawa).
3. 线条小狗 (Moonlab_studio / Maltese puppy).

Do not use capybara, OpenMoji, generic emoji art, or AI-generated substitute cats.

## Operational path that has actually worked in ChatGPT
Use an inline image search/render feature with a specific query, such as:
- 月薪喵 官方 表情包 搞怪 散味舞
- 吉伊卡哇 官方 表情包 害羞 崩溃
- Moonlab_studio 线条小狗 表情包 贴贴

Choose a relevant query based on the tone and meaning of the conversation. Use at most one image in an ordinary reply. Keep serious, sensitive, technical, or time-critical replies sticker-free unless the user asks.

IMPORTANT: Image search may return the wrong IP or unrelated art. Do not assert that the result is an exact official image without visual/source verification.

## Verified direct image catalog
The index at emojis/index.json contains HTTP-verified remote PNG links for LINE package 30890, with 24 stickers verified on Windows. One of these was visually confirmed by the user. The images themselves are NOT hosted here. A working image URL does not establish that ChatGPT's image-rendering component can take arbitrary external URLs.

## Current feature status
- Inline image via search query: USER-CONFIRMED WORKING.
- Exact CDN URL rendered inline in ChatGPT: NOT VERIFIED / not generally supported as a literal source by the available component.
- Guaranteed proactive stickers in every new chat: NOT IMPLEMENTED.
- Persistent personal preference memory: separate product capability, not accomplished by editing this file.

## Short custom instruction (copy into ChatGPT Personalization if desired)
在轻松聊天时，偶尔主动附上一张与语境相符的真实卡通表情包。优先月薪喵（尤其搞怪、魔性表情），其次吉伊卡哇、线条小狗。可以可爱、搞笑、略带调皮或暧昧，但不要露骨。优先使用聊天内可显示的图片搜索；不要用AI生成的替代角色、卡皮巴拉或OpenMoji。不要每条消息都发，也不要在严肃讨论时强行发图。无法确定图片角色时不要冒充官方原图。
