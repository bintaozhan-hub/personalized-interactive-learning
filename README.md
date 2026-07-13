# 🎓 定制化交互式学习系统

一套基于 Claude Code（兼容 Codex）的交互式学习 skill 套件。**让 AI 不再每次从零开始认识你**——5 个 skill 覆盖完整学习闭环：了解你 → 研究领域 → 学习课程 → 深度阅读 → 个性化咨询。

---

## 💡 为什么需要这套系统？

Claude Code 默认每次对话都是"初次见面"。你聊完一段，关了窗口，下次再打开——AI 又失忆了。

这套系统解决了这个问题：

| 没有这套系统 | 有了这套系统 |
|-------------|-------------|
| "我最近想学 Rust" → AI 不知道你是做什么的 | AI 读了你的档案："你是产品经理，之前用过 Python，建议从你熟悉的场景切入" |
| "帮我研究一下新能源" → 每次从头搜索 | AI 存下研究成果，下次直接调用，还能关联你读过的书 |
| "这本书怎么理解？" → AI 逐段翻译给你看 | AI 像朋友一样跟你聊："哎这段我也没太懂，你怎么理解？" |
| 聊完就没了 | 所有知识沉淀到 wiki，随时检索、持续积累 |

**核心思路**：用 `user_wiki` 让 AI 记住你是谁，用 `book_wiki` / `research_wiki` / `course_wiki` 让 AI 记住你学过什么，用 `knowledge-consultation` 把这一切串起来变成可执行的建议。

---

## 📦 安装

```bash
npx skills add bintaozhan-hub/personalized-interactive-learning
```

或手动克隆：

```bash
git clone https://github.com/bintaozhan-hub/personalized-interactive-learning.git .claude/skills/personalized-interactive-learning
```

---

## 🧩 五个 Skill

### 1. 🎤 life-interviewer — 人生采访师

通过 5 阶段时间线回溯（童年 → 学生 → 大学 → 工作 → 当下），完整了解你的人生经历，沉淀为 7 维度结构化个人档案。

> `📋 7维度档案` `⏳ 5阶段回溯` `🔗 双向链接`

**触发**："我想聊聊我的经历"、"帮我梳理一下我的人生"

---

### 2. 🔬 industry-research — 行业研究

系统性研究任何不熟悉的行业、概念或领域。AI 自行搜集资料并标注可信度，通过 MISSION 驱动教学循环帮你建立结构化认知。

> `📊 T1-T4 可信度分级` `🟢🟡🔴 三层理解评估` `📖 读 user_wiki 定制化提问`

**触发**："帮我研究一下 XX 行业"、"XX 是什么？帮我科普一下"

---

### 3. 📖 course-learning — 课程学习

基于固定学习资料（YouTube/Bilibili/网页/文件），自动提取内容 → 制定 CURRICULUM 学习地图 → 逐节教学评估。保留讲师原话，AI 做你的助教而非替代者。

> `🎬 自动提取 YouTube/Bilibili 字幕` `🗺️ CURRICULUM 学习地图` `🟢🟡🔴 逐节评估`

**触发**："帮我学这门课"、"这是课程链接，帮我提取内容"

---

### 4. 📚 book-reading — 深度阅读

辅助深度阅读一本书。提取目录 → 明确阅读目的 → 生成 3-5 部分阅读蓝图 → 逐部分苏格拉底诘问对话。AI 是你的**阅读伙伴**，不是考官。

> `💬 苏格拉底诘问四阶段` `🎭 双重角色（教练→伙伴）` `📄 内置 PDF 提取`

**触发**："帮我读这本书"、"/read"、粘贴书籍目录

---

### 5. 🧠 knowledge-consultation — 知识咨询

结合你的个人档案和**所有已学知识**（书 + 研究 + 课程），为具体问题提供个性化、可执行的建议。转化知识而非摘录知识。

> `🔍 四库检索` `🎯 转化而非摘录` `🧩 匹配用户思维风格`

**触发**："/consult 我想做XX但不知道从哪里开始"

---

## 🗺️ 使用流程

```
第 1 步：life-interviewer      →  让 AI 了解你是谁
          │
第 2 步：industry-research     →  研究你感兴趣的领域
         course-learning       →  系统学完一门课
         book-reading          →  深度读透一本书
         （三者可并行，按需触发）
          │
第 3 步：knowledge-consultation →  AI 综合检索所有知识，给出个性化建议
```

---

## 🏗️ Skill 之间的关系

```
life-interviewer  →  user_wiki  ←  基础层（了解用户）
                                  ↓
industry-research  ─┐
course-learning    ─┤→  各自 wiki  ←  学习层（积累知识）
book-reading       ─┘
                                  ↓
knowledge-consultation            ←  应用层（综合检索，给出建议）
```

---

## 📁 目录结构

```
├── CLAUDE.md                     # 系统总纲（AI 读取）
├── AGENTS.md                     # 同上（Codex 兼容）
├── README.md                     # 你正在读的这个文件
├── .gitignore
├── skills/                       # 5 个 skill 定义
│   ├── life-interviewer/
│   ├── industry-research/
│   ├── course-learning/
│   ├── book-reading/
│   └── knowledge-consultation/
├── wiki/                         # 知识产出（AI 自动维护）
│   ├── user_wiki/                # 你的个人档案（7 维度）
│   ├── book_wiki/                # 书籍阅读记录
│   ├── research_wiki/            # 行业/概念研究成果
│   └── course_wiki/              # 课程学习记录
└── raw/                          # 原材料（你放入的文件）
    ├── user_raw/                 # 个人原始素材（简历、日记等）
    └── book_raw/                 # 书籍 PDF
```

---

## ⚠️ 注意事项

- **所有数据存在本地**，不上传任何云端
- 使用前建议先完成 `life-interviewer`，让 AI 充分了解你
- 每个 skill 可以独立使用，但组合使用效果最好
- wiki 目录由 AI 自动维护，无需手动编辑

---

## 👤 关于作者

- **抖音**：阿韬NEX
- **Codex 学习 / 知识库搭建 / 合作**：ytai89757
