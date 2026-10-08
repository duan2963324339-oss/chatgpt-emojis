# 验证记录与真实能力边界
验证日期：2026-10-09（Asia/Shanghai）。

## 已完成：外部图库
- 原提交67bee9ff534cb3e30722afc26be3c13ee68f4fdf与GitHub main一致，推送确认。
- Pages已启用：main分支 / 根目录，HTTPS，首次部署状态built。
- 在线地址：https://duan2963324339-oss.github.io/chatgpt-emojis/
- 在kaiqi上运行真实Microsoft Edge（Chromium，Playwright无头模式）访问在线站点，HTTP 200。
- 逐张滚动使懒加载生效，24/24图片naturalWidth与naturalHeight均大于0。
- 逐一点击24个复制按钮，并读取真实浏览器剪贴板比对原URL：24/24通过。
- 不匹配搜索显示0/24，清空搜索恢复24张；无页面JavaScript错误。
- 桌面1200×900与手机390×844截图、逐图结果在本地work/。这些截图包含版权图像，不公开上传。
- 原图均使用外部LINE CDN，无原图重新托管。可访问不代表获得再分发权。

## ChatGPT内指定URL嵌入
网站img标签加载通过，只证明网站能力。官方图片输入文档说明上传、粘贴图片等方式，不承诺回答中的任意外部Markdown图片链接一定内嵌。
本轮未取得ChatGPT网页会话的浏览器操作权限/连接，也没有可调用的read_thread工具，因此无法独立复测上一轮聊天显示。
CHATGPT_INSTRUCTIONS.md所记“图片搜索已获用户确认”是既有项目记录，本轮不当作独立测试结论。
结论：指定CDN URL在ChatGPT回答内精确嵌入仍未验证；不能声称平台普遍不支持，也不能保证支持。图片搜索结果也不能保证命中指定URL或正确角色。

## 跨对话主动发表情
仓库/Pages不会监听ChatGPT会话，不会自动注入新对话。
自定义指令可影响各对话回复；记忆按相关性使用，不保留每项细节，也不保证每次检索。
因此偏好提示与“每个新对话主动选取指定真实图片并成功显示”是不同能力，后者未实现。
本轮没有修改账户记忆或个性化设置。编辑仓库指令文件不是写入账户记忆。

## 用户偏好与来源状态
优先月薪喵，其次吉伊卡哇，最后线条小狗。不用AI替代、OpenMoji、卡皮巴拉。
月薪喵：作者主页存在并说明系列表情；本轮未验证可直接使用的单图/动图URL。
吉伊卡哇：ナガノ的LINE包13716526来源已核查；本轮未收录其单图。
线条小狗：LINE包30890，24张外部链接已浏览器验证。
不能将仅有线条小狗的图库描述为已完成月薪喵主动聊天系统。

## 官方资料
- 自定义指令：https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions
- 记忆：https://help.openai.com/en/articles/8590148-memory-in-chatgpt
- 图片输入：https://help.openai.com/en/articles/8400551-chatgpt-image-inputs-faq
这些文档未提供指定外部URL输出渲染与跨对话自动发送的保证。
