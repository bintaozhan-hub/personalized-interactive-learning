# 课程内容提取指南 · Extraction Guide

本文档详细说明如何从不同平台提取课程内容，包括具体命令、常见故障处理和替代方案。

---

## 支持的平台

### YouTube（🟢 高可靠性）

**原理**：YouTube 视频通常带有字幕（CC），手动字幕质量最高，自动生成字幕次之。用 `yt-dlp` 直接下载字幕文件，无需下载视频本身。

**安装 yt-dlp（如未安装）：**
```bash
pip install yt-dlp
# 或
scoop install yt-dlp
```

**步骤：**

```bash
# 1. 查看可用字幕
yt-dlp --list-subs "https://www.youtube.com/watch?v=VIDEO_ID"

# 输出示例：
# zh-Hans  — 简体中文（手动字幕）
# en       — English (auto-generated)
# zh-Hans-auto — 简体中文（自动生成）

# 2. 下载字幕
# 优先选择手动字幕（不带 -auto 后缀的）
yt-dlp --write-subs --sub-langs "zh-Hans,en,zh" --skip-download --convert-subs srt -o "%(title)s" "https://www.youtube.com/watch?v=VIDEO_ID"

# 3. 如果没有手动字幕，用自动生成字幕
yt-dlp --write-auto-subs --sub-langs "zh-Hans,en,zh" --skip-download --convert-subs srt -o "%(title)s" "https://www.youtube.com/watch?v=VIDEO_ID"
```

**字幕文件清理**（.srt → 纯文本）：
```bash
# 去掉时间戳和序号，只保留文字
sed -E '/^[0-9]+$|^[0-9]{2}:[0-9]{2}:[0-9]{2}[,.][0-9]{3} -->|^$/d' input.srt | awk '!seen[$0]++' > output.txt
```

**播放列表处理**：
```bash
# 如果用户给的是播放列表链接，一次性下载所有视频字幕
yt-dlp --write-subs --sub-langs "zh-Hans,en,zh" --skip-download --convert-subs srt -o "%(playlist_index)s-%(title)s" "PLAYLIST_URL"
```

**无字幕时的处理**：
> "这个视频似乎没有字幕。你可以试试：
> 1. 用「飞书妙记」或「通义听悟」上传视频生成逐字稿
> 2. 或者简单告诉我每节课讲了什么，我帮你整理成学习计划"


### 网页课程 / 博客 / 文档（🟢 高可靠性）

直接用 `WebFetch` 工具抓取，无需额外命令。

**如果页面是分页的（多个 URL）：**
逐个抓取，按页码或标题命名存入 `raw/`。

**如果页面有反爬/需要登录：**
不要尝试绕过，直接告知用户：
> "这个页面需要登录才能查看内容。你可以把内容复制粘贴给我，或者截图发给我。"


### 本地文件（🟢 高可靠性）

用户拖拽或粘贴本地文件时，用 `Read` 直接读取。

**支持的格式：**
- `.md` — 直接读取
- `.txt` — 直接读取
- `.srt` / `.vtt` — 字幕文件，按 YouTube 字幕的清理方式处理
- `.pdf` — 用 `Read` 的 PDF 模式读取（指定页码）
- `.docx` — 提示用户另存为 .txt 或直接粘贴内容

**PDF 大文件处理：**
分页读取，每 10-20 页一个文件存入 `raw/`。


### Bilibili（🟡 中等可靠性）

Bilibili 的视频字幕覆盖率因视频而异。官方课程和大会员视频通常有字幕，普通用户上传的视频可能没有。

```bash
# 尝试用 yt-dlp 提取（Bilibili 也在 yt-dlp 的支持列表中）
yt-dlp --list-subs "https://www.bilibili.com/video/BV_VIDEO_ID"
yt-dlp --write-subs --sub-langs "zh-Hans,zh" --skip-download --convert-subs srt -o "%(title)s" "https://www.bilibili.com/video/BV_VIDEO_ID"

# Bilibili 的 AI 生成字幕通常质量不错，可以尝试
yt-dlp --write-auto-subs --sub-langs "zh-Hans" --skip-download --convert-subs srt -o "%(title)s" "https://www.bilibili.com/video/BV_VIDEO_ID"
```

**无字幕时：**
> "这个 Bilibili 视频没有字幕。建议用「飞书妙记」——直接把视频拖进去就能生成逐字稿，准确率很高。生成后把文本发给我。"


## 不支持的平台

### 付费课程平台

以下平台有付费墙和/或反爬机制，**不可自动提取**：

- 得到 App
- 极客时间
- 知识星球
- 小鹅通
- 三节课
- Coursera / Udemy 付费课程

**对用户的引导话术：**
> "我没办法自动提取这门课的内容（有付费墙保护）。你有以下几种方式：
>
> 1. **手机录音 + 飞书妙记**：把课程播放时段用手机录音，上传到飞书妙记转成文字，然后把文本发给我。这是最快的方式。
> 2. **截图字幕**：如果课程本身有字幕，截图发给我，我能从图片中提取文字。
> 3. **自己记笔记**：你听课的时候记下每节的核心要点，发给我，我帮你扩展成课程文件。
>
> 你哪种方式最方便？"

### 纯音频课程 / 播客

没有内嵌字幕，需要 ASR 语音识别。当前环境不内置 ASR 工具。

**对用户的引导话术：**
> "纯音频我需要你用转写工具先转成文字：
>
> - **飞书妙记**（免费，准确率高）— 上传音频/视频文件即可
> - **通义听悟**（免费，阿里出品）— 同样上传即转
> - **剪映**（免费，适合短视频）— 自动生成字幕
>
> 转完之后把文本发给我就行。"


## 提取后的内容组织

### 存入 raw/ 目录

```
wiki/course_wiki/{课程名}/raw/
├── 01-{章节标题}.md
├── 02-{章节标题}.md
├── ...
└── README.md（可选：记录提取信息）
```

### README.md 模板

```markdown
# {课程名} — 原始内容

## 提取信息
- 来源：{链接}
- 提取时间：YYYY-MM-DD HH:MM
- 提取方式：{YouTube字幕 / WebFetch / 用户提供 / ...}
- 字幕类型：{手动字幕 / 自动生成 / ...}
- 总章节数：{N}

## 内容质量说明
- {如有自动生成字幕，标注：基于AI自动生成字幕，可能存在少量识别错误}
- {如有缺失章节，在此说明}

## 章节列表
1. {章节名} — {文件名}
2. {章节名} — {文件名}
...
```

---

## 常见故障处理

### yt-dlp 报错 "Video unavailable"

1. 确认链接是否正确 — 检查是否复制了完整的 URL
2. 确认视频是否被删除或设为私密 — 请用户确认
3. 确认网络是否能访问 YouTube — 如果用户在国内且没开代理，可能需要代理

### 字幕下载了但是乱码

.srt 文件的编码可能是 UTF-16 或其他编码：
```bash
# 检测编码
file -i subtitle.srt
# 转成 UTF-8
iconv -f UTF-16 -t UTF-8 subtitle.srt > subtitle_utf8.srt
```

### 自动生成字幕质量太差

有些视频的自动字幕错误率高到不可用。此时：
> "这个视频的 AI 字幕质量不太好，错误比较多。建议你听的时候对照着看，如果有看不懂的地方随时问我。或者你用飞书妙记重新识别一遍，通常质量会好很多。"

### 课程内容量太大

一门 50 讲的课程，提取完后 raw/ 可能有几十万字的原始内容。**不需要一次全部精炼完**——按照 CURRICULUM.md 的节奏，每次只读本节对应的 raw 文件即可。raw/ 相当于备课参考资料库。
