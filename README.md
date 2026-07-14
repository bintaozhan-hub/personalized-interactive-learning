# 🎓 定制化交互式学习系统

一套基于 Claude Code（兼容 Codex）的交互式学习 skill 套件。**让 AI 不再每次从零开始认识你**——5 个 skill 覆盖完整学习闭环：了解你 → 研究领域 → 学习课程 → 深度阅读 → 个性化咨询。

---

## 💡 为什么需要这套系统？

普通 AI 对话有两个致命问题：**千人一面**（不管你是什么背景，它给所有人的答案都一样）和**学用脱节**（学完就忘，知识和生活没有关联）。

这套系统解决了这两个问题：

### 🎯 定制化：学什么、怎么学，都围绕你展开

传统方式 AI 教你"定位理论"就是照本宣科。这套系统会先通过 `life-interviewer` 了解你是谁——你的职业、思维模式、当下困惑——然后**每个学习 skill 都会读取你的档案来定制内容**：

| 场景 | 没有定制化 | 有定制化 |
|------|-----------|---------|
| 学行业研究 | "新能源产业链分上中下游" | "你在产品经理的视角看，中游电池制造是当前最值得关注的环节，因为这决定了你产品的成本结构" |
| 学一门课 | 通用案例：某大公司的营销方案 | 结合你的背景提问："你在 XX 行业做增长，课程里这套方法论用到你的产品上，第一步你会做什么？" |
| 读一本书 | "这本书的观点是……你有什么想法？" | "你之前提到自己在创业，作者说的'定位就是放弃'——你目前的产品线有没有不敢放弃的部分？" |

### 🔧 学以致用：知识不在 wiki 里吃灰

学完的知识不是存起来就完了。`knowledge-consultation` 会**主动检索你所有学过的东西**（书、研究、课程），结合你当前的实际情况，给出可以直接执行的建议：

> **你的问题**："/consult 我想转行做AI产品经理，但不知道怎么切入"
>
> **AI 的回应**：不是给你一篇"如何转行"的通用文章，而是——
> - 从 `user_wiki` 读到：你有 3 年 B 端产品经验，实用主义思维，目前时间紧迫
> - 从 `research_wiki` 读到：你研究过 AI 产业链，知道大模型和应用层的分界
> - 从 `book-reading` 读到：你在《定位》笔记里写过"从细分市场切入"
> - **综合建议**："别从头学算法。你的优势是懂 B 端场景，结合你对应用层的了解，先找 3 个 AI SaaS 产品深度拆解，用你已有的产品 sense 去判断价值，而不是跟工程师卷技术。"

**核心思路**：先让 AI 懂你（`user_wiki`）→ 学习时围绕你的真实场景（定制化教学）→ 学完能立刻用到生活和工作中（`knowledge-consultation`）。**学习不是为了囤积知识，是为了解决你的真实问题。**

---

## 📦 安装

### 前置条件

- 已安装 [Claude Code](https://docs.anthropic.com/en/docs/claude-code)（或 Codex）
- 已安装 [Node.js](https://nodejs.org/) ≥ 18

在终端输入 `claude` 能正常启动，就可以继续了。

---

### 方式一：一键安装（推荐）

```bash
npx skills add bintaozhan-hub/personalized-interactive-learning
```

这个命令会自动把 5 个 skill 安装到 Claude Code 的 skills 目录。装完重启 Claude Code 就能用。

---

### 方式二：手动克隆

如果你的网络环境不方便使用 `npx`，也可以直接 git clone：

```bash
# 进入 Claude Code 的 skills 目录
cd ~/.claude/skills/

# 克隆本项目
git clone https://github.com/bintaozhan-hub/personalized-interactive-learning.git personalized-interactive-learning

# 重启 Claude Code 即可生效
```

---

### 验证安装

打开 Claude Code，输入：

```
/help
```

在 skill 列表中看到 `life-interviewer`、`industry-research`、`course-learning`、`book-reading`、`knowledge-consultation` 就说明安装成功了。

---

### 开始使用

推荐从 **life-interviewer** 开始，直接说：

> "我想聊聊我的经历"

AI 会带你从童年开始回溯人生经历，聊完后自动沉淀到个人档案。之后的学习 skill 都会读取这份档案来定制化内容——比如用你熟悉的行业举例、针对你的思维模式调整教学方式。

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
