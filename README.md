# 定制化交互式学习系统

一套基于 Claude Code（兼容 Codex）的交互式学习 skill 套件。5 个 skill 覆盖完整学习闭环：了解自己 → 研究领域 → 学习课程 → 深度阅读 → 综合咨询。

---

## 安装

```bash
npx skills add <your-github-username>/<repo-name>
```

或直接克隆到 `.claude/skills/` 目录：

```bash
git clone https://github.com/<your-username>/<repo-name>.git .claude/skills/customized-learning
```

---

## 五个 Skill

### 1. life-interviewer — 人生采访师

通过 5 阶段时间线回溯，完整了解你的人生经历，沉淀为 7 维度个人档案。后续所有 skill 都会读取这份档案来定制化内容。

**触发**："我想聊聊我的经历"、"帮我梳理一下我的人生"

### 2. industry-research — 行业研究

系统性研究任何不熟悉的行业、概念或领域。AI 自行搜集资料（T1-T4 可信度分级），通过教学循环帮你建立结构化认知。

**触发**："帮我研究一下 XX 行业"、"XX 是什么？"

### 3. course-learning — 课程学习

基于固定学习资料（课程链接、逐字稿、视频字幕等），自动提取内容、制定学习地图、逐节教学。支持 YouTube、Bilibili、网页。

**触发**："帮我学这门课"、"这是课程链接"

### 4. book-reading — 深度阅读

辅助深度阅读一本书。提取目录 → 明确目的 → 生成阅读蓝图 → 苏格拉底诘问对话。内置 PDF 提取工具。

**触发**："/read"、"帮我读这本书"、粘贴书籍目录

### 5. knowledge-consultation — 知识咨询

结合你的个人档案和所有已学知识（书、研究、课程），为具体问题提供个性化建议。

**触发**："/consult 我想做XX但不知道从哪里开始"

---

## 使用流程

```
第 1 步：life-interviewer     →  让 AI 了解你是谁
第 2 步：industry-research    →  研究你感兴趣的领域
         course-learning      →  系统学完一门课
         book-reading         →  深度读透一本书
         （三者可并行，按需触发）
第 3 步：knowledge-consultation → 基于所有已学知识，获得个性化建议
```

---

## 目录结构

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
├── wiki/                         # 知识产出（由 AI 自动维护）
│   ├── user_wiki/                # 你的个人档案
│   ├── book_wiki/                # 书籍阅读记录
│   ├── research_wiki/            # 研究成果
│   └── course_wiki/              # 课程学习记录
└── raw/                          # 原材料（你放入的文件）
    ├── user_raw/                 # 个人原始素材
    └── book_raw/                 # 书籍 PDF
```

---

## Skill 之间的关系

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

## 注意事项

- **所有数据存在本地**，不上传任何云端
- 使用前建议先完成 `life-interviewer`，让 AI 充分了解你
- 每个 skill 可以独立使用，但组合使用效果最好
- wiki 目录由 AI 自动维护，无需手动编辑

---

## 关于作者

- **抖音**：阿韬NEX
- **Codex 学习 / 知识库搭建 / 合作**：ytai89757
