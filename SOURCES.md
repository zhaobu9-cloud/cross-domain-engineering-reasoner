# 核查来源与类似 Skill

历史来源 S4至S8 保留1.0.0的2026-09-28核查记录，本轮未重新核查这些仓库，不代表它们的当前状态。S1至S3与新增S9至S11于2026-09-29重新/新增查阅。

1.0.0原记录的检索范围包括当前可见已安装 Skill 目录、公开 Skill 仓库、Agent Skills 格式规范，以及 OpenAI 和 Anthropic 的官方说明。它不是完整市场清单，也不能证明不存在其他等价方案。

本包面向通用工程任务编写，没有捆绑或执行下列第三方 Skill 的代码。来源用来比较能力边界与核查文件格式，不证明本包具有经过实测的效果。

## 官方格式与安装

### S1 · Agent Skills Specification

地址：`https://agentskills.io/specification`

用于核查：以 `SKILL.md` 为入口；YAML 元数据；name/description；支持文件和按需读取。通用格式并不保证所有宿主对扩展字段有相同行为。

### S2 · OpenAI · Build skills

入口：`https://developers.openai.com/codex/skills/`

核查时重定向：`https://learn.chatgpt.com/docs/build-skills`

用于核查：Codex 本地用户级 `$HOME/.agents/skills` 与项目级 `.agents/skills`；`$` 与 `/skills` 的显式调用；`agents/openai.yaml`；按需加载和指令优先的设计。产品版本与组织配置可能影响可用性，未在用户环境实测。

### S3 · Anthropic · Extend Claude with skills

地址：`https://code.claude.com/docs/en/skills`

用于核查：Claude Code 用户级 `~/.claude/skills`、项目级 `.claude/skills` 与 `/skill-name` 调用。本地、账户与云端范围应区分。

### S4 · Anthropic · skill-creator

地址：`https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md`

已查看原文：`https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator/SKILL.md`

相近之处：把工作流程写成 Skill，并使用用例、反馈和对照评估改进。它解决“怎样制作与评估 Skill”，不是制造领域的跨域分析流程。本包保留了评测用例与真实执行状态，不宣称已完成未运行的模型评测。

## 接近本需求的公开 Skill

### S5 · K-Dense · scientific-brainstorming

地址：`https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-brainstorming/SKILL.md`

已查看原文：`https://raw.githubusercontent.com/K-Dense-AI/scientific-agent-skills/main/skills/scientific-brainstorming/SKILL.md`

相近之处：科学选题、明确假设、结构化讨论、反方审查、证据核查和决策记录。偏向研究方向的产生与整理，不能将 brainstorm 结果直接作为假设验证。

### S6 · K-Dense · scientific-critical-thinking

地址：`https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-critical-thinking/SKILL.md`

已查看原文：`https://raw.githubusercontent.com/K-Dense-AI/scientific-agent-skills/main/skills/scientific-critical-thinking/SKILL.md`

相近之处：评估科学主张、实验设计、偏差、混杂和证据质量。制造任务需要另行定义物理边界、设备可执行性与工程验收，不能直接套用所有领域的证据框架。

### S7 · K-Dense · hypothesis-generation

地址：`https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/hypothesis-generation/SKILL.md`

已查看原文：`https://raw.githubusercontent.com/K-Dense-AI/scientific-agent-skills/main/skills/hypothesis-generation/SKILL.md`

相近之处：将观察转成候选假设、竞争解释、区分性预测、量测和试验计划。与本需求重叠明显；本包另外明确要求外部领域结构映射、工程约束和明确指定的任务边界。

### S8 · obra/superpowers · brainstorming

地址：`https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md`

已查看原文：`https://raw.githubusercontent.com/obra/superpowers/main/skills/brainstorming/SKILL.md`

相近之处：在实现之前理解意图、需求与设计。更偏软件开发前的方案澄清，不应仅凭它判断物理机理与制造可行性。

## 结论边界

有类似组件，所以无需声称这是全新方法。此次定制的价值是把跨领域启发、工程可行性、最小试验和任务边界合为一条可重复流程。未发现可直接替代全部定制要求的单一现成入口，不等于全球不存在。

具体工程方法的文献需要在每次实际任务中核查，本文件不是雷达、调度、清粉、材料或缺陷机理的技术证据库。

## 1.1.0 新增官方依据

### S9 · GitHub · Searching for repositories

地址：`https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories`

2026-09-29查阅。仅用于核查 README、topic、language、license、archived、pushed 等仓库搜索限定符，以及仓库发现和文件/代码检索的区别。具体工程任务的查询策略与分支逻辑是本包按用户要求制定，不是 GitHub 官方推荐的工程判断准则。

### S10 · GitHub · Licensing a repository

地址：`https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository`

2026-09-29查阅。用于区分公开可见和具有开放许可的代码，要求查看许可而非仅看仓库公开状态。本包不代替针对具体分发与集成的许可专业审查。

### S11 · GitHub · REST API endpoints for licenses

地址：`https://docs.github.com/en/rest/licenses/licenses`

2026-09-29查阅。用于提醒自动许可证识别可能不覆盖依赖与其他许可声明，需阅读原始许可材料。未在本次升级中查询任何具体工程仓库的许可证 API。

## 本版检索的边界

本次任务是修改 Skill，而不是对清粉、铺粉或排版做实际开源调研。因此没有把这些工程领域的项目写成已核实清单；示例只展示分支行为，正式使用时需重新执行两阶段检索。
