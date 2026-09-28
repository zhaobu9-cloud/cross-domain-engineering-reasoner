# Cross-Domain Engineering Reasoner

> Transfer structure, not vocabulary. Validate mechanisms, not resemblance.

A reusable engineering reasoning Skill for solving difficult technical problems through **problem abstraction, cross-domain analogy, anti-analogy, first-principles checks, and minimum discriminating experiments**.

它不是让 AI 随机脑暴，而是让 AI 像工程师一样先划清事实边界，再把问题抽象为跨行业可比较的结构，寻找可迁移的方法，同时主动攻击自己的类比，最后用最小试验让证据裁决。

## Why this exists

AI can search and implement quickly, but the quality of the result still depends heavily on how the problem is framed. Many engineering breakthroughs come from recognizing that a difficult problem in one field has already appeared, in another form, somewhere else.

This Skill turns that idea into a repeatable workflow.

## Core workflow

`Facts → Constraints → Assumptions → Unknowns → Problem Abstraction → Structural Archetype → Cross-Domain Search → Method Transfer → Anti-Analogy → First-Principles Gate → Contradiction Scan → Minimum Experiment → Evidence Ladder → Implementation → Learning Loop`

## What makes it different

- **Fact Boundary**: separates observations from assumptions.
- **Problem Archetype**: identifies the structural problem before searching for solutions.
- **Cross-Domain Analogy**: searches for structurally similar problems outside the current field.
- **Anti-Analogy**: explicitly asks where each analogy breaks.
- **First-Principles Gate**: requires a plausible physical, geometric, or information mechanism.
- **Contradiction Scan**: looks for trade-offs and conflicting engineering requirements.
- **Minimum Discriminating Experiment**: designs the smallest test that can separate competing hypotheses.
- **Evidence Ladder**: distinguishes intuition, simulation, bench tests, controlled trials, production evidence, and qualification.
- **Learning Loop**: turns one-off troubleshooting into reusable engineering knowledge.

## Typical use cases

- LPBF / SLM process anomalies
- recoating and powder-bed inspection
- defect monitoring
- support strategy
- layout optimization
- depowdering planning
- process-parameter optimization
- digital twins
- AI + manufacturing
- quality closed loops
- fault diagnosis
- automation feasibility
- any engineering problem where methods from other domains may transfer

## Quick invocation

```text
这是我的工程问题、已知事实和硬约束。

请执行 Cross-Domain Engineering Reasoner：
1. 把已知事实、硬约束、假设、未知项分开；
2. 把问题抽象成领域无关的结构；
3. 找出至少三个其他领域中结构相似的问题；
4. 说明每个领域可以迁移的方法和底层机制；
5. 主动寻找类比失效点；
6. 用第一性原理检查方法是否可能成立；
7. 找出关键工程矛盾；
8. 为最有希望的方案设计最小判别试验；
9. 区分“能做 Demo、工程可用、生产可用、完成验证”；
10. 最后给出下一步信息价值最高的动作。

不要用跨领域术语堆砌答案。类比不是证据，试验结果才是。
```

## Files

- `SKILL.md` — complete Skill instructions
- `README.md` — project overview and usage
- `LICENSE` — MIT License

## Design principle

A cross-domain analogy is only a hypothesis generator.

The final decision should come from mechanisms, measurements, experiments, and engineering constraints.

## License

MIT
