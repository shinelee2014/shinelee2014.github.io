# ShineLee 极简个人入口

线上：https://shinelee2014.github.io/index.html

## 页面

- index.html：主页；直接进入博客、工具箱与 GitHub。
- tools.html：24 个公开 Pages 项目、本地搜索、原有密钥解锁入口。
- overview.html：保留旧地址，使用相同静态入口布局。

纯 HTML/CSS，首页不依赖 JavaScript。工具页仅使用 tools.js，不加载视频、远程字体、图标库或 GitHub API。hyalite.js 保留在仓库历史与当前文件中，但不再被页面引用。

## 更新目录

修改 data/projects.json，然后运行：

```sh
python scripts/build.py
```

目录有意作为静态快照随页面发布，新增项目需更新此文件。访问地址延续原工具页规则，不以 fork 仓库中的 upstream homepage 替换个人部署地址。

## 本地预览

```sh
python -m http.server 4190 --bind 127.0.0.1
```

打开 http://127.0.0.1:4190 。解锁逻辑需要 HTTPS 或 localhost 的 Web Crypto。客户端解锁并非服务端安全边界，不能用于存储秘密；这里只保留原有操作方式。

## 发布与回退

main 分支根目录由 GitHub Pages 发布。修改后提交 main，等待 Pages 构建通过。需恢复旧版时可从 Git 历史还原相关文件，不涉及其他项目与 Vercel 博客。

## 验证摘要

桌面与手机布局、原访问密钥、错误密钥、记忆状态、搜索无结果、24 项目录均检查通过。浏览器请求检查确认不请求外部资源，关闭 JavaScript 后首页仍可使用。
