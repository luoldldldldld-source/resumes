# 罗顿 · 个人求职网站

轻量静态网站，原生 HTML、CSS、JavaScript，无数据库、无后端、无付费服务、无外部字体和追踪脚本。中文为主，内容按独立 section 组织，便于后续增加英文版。

## 本地打开

直接打开 `index.html` 可浏览页面。视频、下载与复制邮箱建议在本地服务器中检查：

```sh
python tools/serve.py --port 8765
```

打开 http://127.0.0.1:8765 。终端中按 Ctrl+C 停止。Windows 如使用 Python Launcher，可将 `python` 换成 `py`。预览服务仅监听本机地址，支持视频拖动进度。

## 文件说明

| 文件 | 用途 |
| --- | --- |
| `index.html` | 所有网页文案、栏目、联系方式与作品卡片 |
| `styles.css` | 颜色、字号、间距、响应式布局 |
| `script.js` | 菜单、视频弹窗、邮箱复制和导航高亮 |
| `assets/luodun-resume.pdf` | 可下载的公开版简历 |
| `assets/paper-acceptance.jpg` | 论文录用通知及作者署名依据 |
| `assets/videos/eviews-1.mp4` 至 `eviews-3.mp4` | 原创教程网页播放版 |
| `assets/poster-1.jpg` 至 `poster-3.jpg` | 从对应视频提取的预览画面 |
| `tools/build_resume.py` | 重新生成简历PDF的可编辑源文件 |
| `tools/serve.py` | 本地预览工具，不是线上后端 |
| `.nojekyll` | 让 GitHub Pages 直接提供静态文件 |

## 日后修改内容

1. **文字与经历**：在 `index.html` 搜索对应中文标题，再修改其下文字。保留元素的 `id`，导航依靠这些标识跳转。
2. **邮箱**：同时修改 `index.html` 中可见邮箱及 `mailto:` 地址、`script.js` 中复制内容，以及 `tools/build_resume.py` 中的邮箱。
3. **颜色与排版**：修改 `styles.css` 开头的 `:root` 变量。手机布局位于文件末尾的媒体查询。
4. **视频**：替换 `assets/videos/` 中同名 MP4，同时替换对应封面，并更新页面时长。建议保留 MP4 / H.264 / AAC 格式。页面不自动播放，打开弹窗后仍需点击播放器播放按钮；关闭弹窗即停止加载与播放。
5. **补充研究报告或Excel案例**：将确认可公开的文件放入 `assets/`，把对应“材料待补充”卡片改为实际说明及真实下载链接。未提供材料时保留占位，不编写分析结果。
6. **更新PDF**：修改 `tools/build_resume.py` 中内容，再执行下方命令。网页与PDF为独立文件，改经历或数值时应同步更新。

```sh
python -m pip install reportlab
python tools/build_resume.py
```

PDF脚本默认使用Windows微软雅黑中文字体。其他系统需设置 `RESUME_FONT` 与 `RESUME_FONT_BOLD` 指向可用的中文TrueType字体。脚本只用于本地制作PDF，访客不需要安装任何东西。

7. **增加英文版**：创建 `en/index.html`，将 `lang` 设为 `en` 并翻译文案；共享样式和脚本使用 `../styles.css`、`../script.js`。将英文页的PDF、封面和视频路径改为 `../assets/...`，并调整脚本的视频资源前缀。确认英文页面可用后再添加语言切换链接。当前没有未实现的语言切换按钮。

## GitHub Pages部署步骤（尚未执行）

本项目尚未创建GitHub仓库，也没有公开部署。以下操作会公开网站；执行前应确认所有网页、PDF和视频都适合公开。

1. 登录你的GitHub账号，创建仓库，例如 `portfolio`。免费方案可使用公开仓库。
2. 把本目录的内容放到仓库根目录：`index.html` 应位于根目录，不要把整个文件夹再嵌套一层。不要上传原始简历、工作目录或原始视频。
3. 视频超过浏览器上传大小限制，建议使用GitHub Desktop或Git命令提交整个目录。不要把MP4交给Git LFS后直接期望GitHub Pages播放。
4. 在仓库 `Settings → Pages → Build and deployment` 中，将 Source 设为 `Deploy from a branch`，选择 `main` 分支、`/(root)`，保存。
5. 等待部署完成，打开Pages设置中给出的地址。普通仓库的地址通常为 `https://你的用户名.github.io/portfolio/`。本项目使用相对路径，支持仓库子目录地址。
6. 在线复查所有栏目、手机菜单、三段视频、邮箱和PDF下载。后续更新文件并提交到 `main`，Pages会重新发布。

若已经安装Git，也可在本目录运行以下命令。请先把占位地址替换成你确认的仓库地址；`git push` 会上传所选文件。

```sh
git init
git add index.html styles.css script.js assets tools README.md .nojekyll .gitignore
git commit -m "Add personal portfolio website"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/portfolio.git
git push -u origin main
```

部署依据：[GitHub Pages官方入门文档](https://docs.github.com/en/pages/quickstart)。GitHub普通仓库阻止大于100 MiB的单文件，浏览器上传上限为25 MiB；本项目所有视频均小于100 MiB。参见[大文件限制](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)。

## 内容与隐私约定

- 事实来源：用户提供的Markdown简历、稿件录用通知及后续确认；赛事全称为“中国国际大学生创新大赛”，论文状态为“录用待刊”，视频原创身份由本人确认。
- 根据本人补充，教育经历加入“弗罗斯特堡州立大学｜理学本科”；就读时间与湖南工商大学一致，为2023.09—2027.06，未推断具体专业、学位授予情况或联合培养形式。
- 公开联系渠道仅为本人确认的邮箱。不包含生日、手机号、家庭地址或原始简历文件。
- 付款笔数与业务项数保留具体值；金额和成本使用“70余万元”“5千余元”“60余万元”“50余万元”。重量按概数展示。
- 教学经历只呈现简历已有说明及本人提供的3段教程，不编造教学人数、评分或成果。
- 论文已录用待刊，录用通知拟安排于《山西农经》2026年第22期发表。作者顺序为王柯理、袁佳豪、罗顿、朱逸骁、陈栋，罗顿为第三作者。网页提供录用通知查看入口；论文公开链接、项目证书及公开链接待补充。
- 研究原文、回归结果表、脱敏Excel样例尚未提供，相关卡片明确提示缺少资料。
- 教程采用通用编号，未推断完整章节名称；字幕和文字讲义待补充。第二段由原始2560×1440转为1920×1080网页播放版；第一段保留原音视频编码，第三段遮盖抽样检查中发现的文档编号区域并重新编码。三个原文件均未修改，所有播放版均优化加载位置。
- 视频已做抽样画面检查，未逐帧审阅或完整转写音轨。发布前建议本人完整回看，确认录屏中没有其他不必要的个人信息，且课程材料适合公开展示。
- 未添加远程分析、表单收集或外部资源请求。访客点击邮箱后会使用自己的邮件应用。

## 维护检查

每次修改后查看桌面与手机宽度，点击所有导航、打开每段视频、关闭弹窗、试用邮箱复制，并下载最新PDF。确认简历文字同步、占位提示准确，再考虑发布。
