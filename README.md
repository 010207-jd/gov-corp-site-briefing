# 政企现场讲解稿生成器 · gov-corp-site-briefing

把零散材料（纪要、周报、报表、新闻稿、领导批示、PPT、口头要点）整理成**可直接上台念**的政企现场讲解稿。

输出不止一篇稿子，而是一套现场交付物：**主稿 + 提词卡 + 问答预案 + 待补清单**。

适用于 Codex（`~/.codex/skills/`）以及任何支持 Agent Skills / SKILL.md 规范的客户端。

## 解决什么问题

材料散在十几个文件里，写稿的人两小时内要交、领导还要审——最后写出来的往往是"工作总结朗读版"：没有动线、没有时长、通篇形容词、一个数字都不敢说，现场一被追问就崩。

本技能把这件事拆成六步固定流程：

**材料台账 → 场景判定 → 动线结构 → 逐节成稿 → 质检打分 → 交付打包**

并强制三个约束：

1. 每个数字必须在事实台账里有出处，否则只能写 `【待补】`
2. 不越权表态、不做结果承诺
3. 时长按 200 字/分钟倒推，超时即返工

## 覆盖场景

政务调研接待 · 企业展厅参观 · 项目开工竣工投产 · 成果验收评审 · 党建阵地 · 数字政府 / 指挥中心 · 产业园招商推介 · 生产一线走访

场景可叠加，常见组合「政务调研接待 + 指挥中心」「客户参观 + 生产一线」。

## 安装

### 方式一：Codex 用户级（推荐）

```bash
git clone https://github.com/010207-jd/gov-corp-site-briefing.git
cp -r gov-corp-site-briefing ~/.codex/skills/
```

### 方式二：Codex 项目级

```bash
mkdir -p .codex/skills
cp -r gov-corp-site-briefing .codex/skills/
```

### 方式三：在 Codex 里直接装

```text
$skill-installer install https://github.com/010207-jd/gov-corp-site-briefing
```

### 其他客户端

- Claude Code：`~/.claude/skills/`
- 任何支持 Agent Skills 的客户端：放到其 skills 目录下的同名文件夹即可

## 用法

装好后直接说话即可触发：

```text
用这批材料写一个 25 分钟的政务调研讲解稿，来访是市发改委一行 8 人，
走展厅、指挥中心、车间三个点位。（然后粘贴或附加材料）
```

也可显式调用：`使用 gov-corp-site-briefing 帮我把这些材料整理成讲解稿`

## 目录结构

```text
gov-corp-site-briefing/
├── SKILL.md                          # 主入口：六步流程、三条硬底线、交付契约
├── README.md
├── LICENSE
├── references/
│   ├── 01-material-intake.md         # 材料类型映射、事实台账、冲突裁决
│   ├── 02-scenario-playbooks.md      # 八类场景的动线与话术套路
│   ├── 03-style-and-tone.md          # 口语化改写、称谓、禁忌替换表
│   ├── 04-timing-and-delivery.md     # 语速换算、节奏配比、突发应对
│   ├── 05-qa-prep.md                 # 提问六分类与三段式应答
│   └── 06-quality-checklist.md       # 100 分质检表
├── assets/
│   ├── briefing-template.md          # 主稿模板
│   ├── cue-card-template.md          # 提词卡模板
│   └── fact-ledger-template.md       # 事实台账模板
├── scripts/
│   └── script_stats.py               # 字数与时长核算
└── examples/
    └── example-smart-city.md         # 完整示例（虚拟案例）
```

## 字数核算

```bash
python3 scripts/script_stats.py examples/example-smart-city.md
python3 scripts/script_stats.py 讲解稿.md --wpm 190   # 嘈杂环境放慢
```

输出每节字数与实际预估时长，直接对照节头标注检查是否超时。

## 设计原则

1. **渐进式加载**：主文件只放流程与约束，具体话术在 `references/`，用到才读，不占上下文。
2. **事实优先于文采**：台账机制让每个数字可追溯，宁可留 `【待补】` 也不编。
3. **时长是硬指标**：每节标注字数与时长，用脚本核算。
4. **交付的是现场方案**，不是一篇好看的文字。

## 自定义

- 想固定本单位口径：在 `references/03-style-and-tone.md` 末尾追加一节「本单位专用表述」，列常用提法与禁用语。
- 想增加场景：在 `references/02-scenario-playbooks.md` 按同样格式追加，同时在 `SKILL.md` 第 2 步的场景清单里补一行。
- 想改语速基准：改 `scripts/script_stats.py` 的 `--wpm` 默认值（当前 200）。

## 免责

本技能生成的是讲解稿初稿，所有事实、数据、口径须由使用者核定后方可用于正式场合。示例中的机构、数据均为虚构。

## License

MIT
