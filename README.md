# 工程跨域求解 · engineering-bridge

版本：1.1.0  
更新日期：2026-09-29；本版重新核查格式/安装与 GitHub 检索/许可官方说明，历史类似 Skill 清单保留原核查日期。

这是面向通用工程问题的公开 Agent Skill：

**问题与约束 → 本领域开源检索 → 有则优先参考与复用；本轮未找到则跨域 → 对应领域开源检索 → 模块适配与反类比 → 最小验证 → 经授权的实现/记录。**

本仓库最初以 `cross-domain-engineering-reasoner` 发布 v0.1.0；本次接入完整的 `engineering-bridge` v1.1.0 包。仓库地址保持不变，技能调用名更新为 `$engineering-bridge`。公开版以通用场景替代个人背景文件，并去除示例中的私有项目名称。包内更新记录沿用 engineering-bridge 自身的版本历史，新增规则、模板与回归题见 [CHANGELOG.md](CHANGELOG.md)。

它并非训练后的专用模型，也不带自动设备控制。核心是 Markdown 指令，按需读取参考资料；唯一 Python 脚本只用于本地包结构检查，不调用模型、不联网、不改工艺参数。

## 从哪里开始

先看 `SKILL.md`，这是主入口。安装时保留整个 `engineering-bridge` 文件夹，不要只复制主文件；否则按需引用的资料会缺失。

### Codex CLI / IDE 本地安装

按照本次核查的 OpenAI 文档，用户级目录是 `$HOME/.agents/skills`，项目级目录是 `.agents/skills`。[S2]

Windows 原生环境示例：

```text
C:\Users\你的用户名\.agents\skills\engineering-bridge\SKILL.md
```

解压下载的 zip，把 `engineering-bridge` 文件夹整体复制到 `.agents\skills` 下。目录不存在就创建；不要多套一层版本号文件夹。已有同名文件夹时先备份到 skills 目录之外，避免重复发现或覆盖个人修改。

在 Codex CLI 或 IDE 中输入 `/skills` 检查是否列出，再调用：[S2]

```text
$engineering-bridge
分析我的铺粉检测问题，沿用已知事实和约束。
先查本领域类似开源项目，给最相关的3个参考。
本领域未找到时再跨域，随后检索对应领域的开源实现。
说明可复用模块、差异、源码与许可核查状态，以及最小验证。
```

未显示时检查实际运行环境与保存目录是否一致，并刷新可用技能列表。在 WSL 中运行的代理需要检查该 WSL 用户的 HOME，不能假定会读 Windows 用户目录。[安装环境提示]

### Claude Code 本地安装

用户级目录为 `~/.claude/skills/engineering-bridge/`，项目级为 `.claude/skills/engineering-bridge/`。复制同一个完整文件夹，用 `/engineering-bridge` 调用。[S3]

这不是对所有 Claude 产品、云端会话或移动端安装方式的承诺。本地文件不会仅因下载就自动进入其他客户端。

### 在当前聊天或其他支持文件的客户端使用

把主文件及需要的参考文件作为任务资料交给代理，要求按该流程处理，可以复用指令内容，但这不等于已经原生安装、永久记忆或获得自动触发能力。原生 Skill 安装由具体宿主与权限决定。[S1][S2][S3]

这些步骤针对本地 CLI / IDE 的手动安装。GitHub 文件更新不会自动更新其他电脑上的技能副本；ChatGPT 中已安装的技能由宿主单独管理。本包的原始验证边界见 `evals/validation-report.md`。

## 怎样触发

可以明确调用名称，也可以用“从跨领域看”“重新定义这个工程问题”“不要局限于本领域”“审查这个方法为什么可能失效”等请求。自动触发依赖宿主和模型，不能保证每次都触发；明确调用最容易核对。[S2][S3]

默认先执行本领域检索，不先让你填一堆表。找到实质相关项目时优先给参考，不强行生成三个外部领域；未找到才跨域，并继续寻找对应的代码实现。只说“跨域思考”不表示跳过前置关卡；明确要求跳过或只审查已选路线则遵从。你可自然指定“只做半页快筛”“审查这一个方案”“给出最小试验”或“已经授权实现，输出工程交接”。普通翻译、润色和明确的直接修复任务不应被它劫持。

## 1.1.0 的分支规则

| 本领域结果 | 默认动作 |
|---|---|
| 有同任务或关键子问题开源实现 | 给前3个、最多5个参考；不足按实际数量。解释模块、缺口与一个最小验证。 |
| 本轮有覆盖的检索仍未找到 | 说明范围和近似项目排除理由；跨域映射后再检索具体开源实现。 |
| 工具失败、未能核实代码/许可 | 标为检索不充分；不能写没有项目，也不据此自动跨域。 |
| 用户要求跳过/离线/只审指定路线 | 标注例外；不虚构已搜索，条件化完成授权范围。 |

本领域部分覆盖也应先给参考，不要求一站式解决全部任务。通用框架、数据集、论文和许可待核实的公开代码单独列，不冒充已确认的同领域开源实现。

每个项目至少给：规范链接、真实匹配点、已查代码模块、适配差异、许可范围、维护与复现状态、核查日期及来源。Star 不是排序依据。

跨域后的每条路线保留“工程子问题 → 来源结构 → 方法 → 仓库 → 所查模块 → 适配 → 最小试验”链条；找不到代码就写尚需自研，不编造项目。

完整检索依赖宿主提供的获准搜索/仓库阅读工具，本包不内置爬虫、凭据或网络权限，不会自动安装或运行被检索到的代码。

## 与原提示词相比增加了什么

| 扩展 | 要防止的问题 |
|---|---|
| 本领域开源检索关卡 | 为跨域而跨域，忽略已有成果 |
| 跨域后的实现检索 | 只借概念，找不到具体代码与适配入口 |
| 仓库核查、状态与相关性排序 | 将公开、开源、可运行、工程可用混为一谈 |
| 真实目标与功能重构 | 把错误目标自动化 |
| 约束来源与修改权限 | 把硬约束当作可以随意优化的偏好 |
| 问题结构与具体关系映射 | 只有行业名，没有可借用的方法 |
| 量纲、尺度、观测与执行门槛 | 原领域有效，迁移后基础条件消失 |
| 竞争解释与反例 | 只替自己找证据 |
| 基线、对照、三类试验结果 | Demo 成功就宣布工程问题解决 |
| 实现交接与安全边界 | 报告写得完整，输入接口、测试和责任不清楚 |
| 案例与回归测试 | 讨论过就当作学会了，改版后旧规则悄悄失效 |

## 文件导航

- `SKILL.md`：工作契约、触发边界、主流程与交付检查。
- `references/`：新增 `open-source-discovery.md`，保留方法迁移、证据/试验规则、通用工程场景。
- `assets/`：新增项目参考卡、检索日志；同步更新报告、交接和案例模板，保留试验卡。
- `examples/`：铺粉检测完整结构示例，以及支撑、清粉、排版的目标重构。
- `evals/`：原16题与新增检索分支题、对照评估办法、本次本地检查结果。行为题未经过独立模型执行。
- `agents/openai.yaml`：可选的名称、说明和默认调用语句。[S2]
- `scripts/validate_package.py`：不联网的包结构检查，不验证工程推理是否正确。
- `SOURCES.md`：本次核查的现成 Skill 与官方格式/安装资料。

## 本次完成与没有完成

已更新主流程、参考资料、模板、示例、默认调用与回归用例，并执行本地文件/结构检查。实际检查范围和结果以本版记录为准，不沿用旧版的执行结论。详细结果见 `evals/validation-report.md`。

未进行 Codex/Claude 的真实宿主加载测试，未进行有/无 Skill 的独立模型对照评测，也未运行任何制造试验。不能据此宣称已经提高准确率、保证自动触发或验证跨领域方案有效。

## 如何让它逐渐变成你的方法库

把新任务的真实结果按 `assets/case-record.md` 保存到你指定的项目位置。成功和失败都保留；没有授权不写入，没有试验不升级为已验证。再次使用时提供或让有权限的工具读取这些记录。

调整稳定方法时更新本 Skill 的版本并重跑用例。不要把某批材料、某台设备的单次参数直接写成所有项目通用规则。

来源编号见 `SOURCES.md`。

## English overview

Engineering Bridge is the v1.1.0 successor to this repository's original Cross-Domain Engineering Reasoner skill. The repository URL stays unchanged; invoke the updated skill as `$engineering-bridge`.

Start by checking relevant open-source implementations in the problem's own domain. When a verified implementation covers the task or a critical subproblem, assess reuse first. If a sufficiently scoped search finds none, map the problem to structurally similar domains and look for concrete implementations there. Failed or incomplete searches remain inconclusive.

Every proposed reuse or transfer retains facts, assumptions, hard constraints, counterexamples and a minimum discriminating experiment. Code availability, local test results and physical engineering validation are separate evidence levels. Install the complete folder so referenced guides, templates and examples remain available.

## License / 许可

MIT. See [LICENSE](LICENSE).
