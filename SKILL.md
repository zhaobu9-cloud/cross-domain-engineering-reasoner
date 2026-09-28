---
name: cross-domain-engineering-reasoner
description: >
  A reusable engineering reasoning skill for solving hard technical problems by abstracting the problem structure,
  finding structurally analogous problems in other domains, transferring candidate methods, identifying where the
  analogy breaks, and designing the smallest practical experiment to validate or falsify the transferred idea.
  Use when the user presents an engineering problem with known facts, constraints, failure modes, uncertain mechanisms,
  process optimization questions, defect diagnosis, monitoring problems, manufacturing automation, support strategy,
  layout optimization, quality inspection, digital twin, or asks for "cross-domain thinking", "analogies from other fields",
  "first-principles", "what can be borrowed from other industries", or "minimum experiment".
---

# Cross-Domain Engineering Reasoner

## Purpose

Do not merely answer "what technique should be used".

Convert the user's engineering problem into a structure that can be compared across domains, search for methods with the
same causal or decision structure, test whether the analogy survives the user's real constraints, and turn the surviving
ideas into the smallest testable engineering action.

The core principle is:

**Transfer structure, not vocabulary. Validate mechanisms, not resemblance.**

---

## Default Workflow

### Step 1 — Build the Fact Boundary

Separate all available information into four buckets:

1. **Known facts**
   - directly observed
   - measured
   - verified by drawing/specification/experiment/log
   - explicitly provided by the user

2. **Hard constraints**
   - geometry
   - machine capability
   - material limits
   - process windows
   - safety / quality / certification requirements
   - cost / time / data / sensing limitations
   - interfaces that cannot currently change

3. **Assumptions**
   - plausible explanations not yet demonstrated
   - causal links inferred from experience
   - simplifications used by the current model

4. **Unknowns / questions to resolve**
   - variables whose state would materially change the engineering decision
   - missing measurements
   - uncertain mechanisms
   - missing boundary conditions

Never silently promote an assumption into a fact.

---

### Step 2 — Abstract the Problem

Rewrite the domain-specific problem in domain-neutral language.

Produce:

- **System state**
- **Observable signals**
- **Hidden state**
- **Controllable inputs**
- **Disturbances**
- **Failure condition**
- **Objective**
- **Feedback available**
- **Decision time scale**
- **Spatial scale**
- **Cost of false positive**
- **Cost of false negative**

Then state the problem in one sentence without using domain jargon where possible.

Example:

Instead of:
"Detect abnormal SLM recoating."

Abstract to:
"In a repeated cyclic process, infer an evolving hidden process state from noisy spatial observations, while avoiding unnecessary intervention and detecting persistent degradation early."

---

### Step 3 — Identify the Problem Archetype

Classify the problem into one or more structural archetypes:

- hidden-state estimation
- anomaly detection
- sequential decision
- control under uncertainty
- path planning
- constrained optimization
- resource allocation
- multi-agent coordination
- fault diagnosis
- weak-signal detection
- rare-event detection
- geometric packing
- surface generation
- thermal management
- transport / flow
- topology evolution
- inspection under incomplete observability
- human-in-the-loop judgment
- change-point detection
- reliability growth
- active learning
- inverse problem
- digital twin / state synchronization

Do not force a single archetype if the problem is genuinely hybrid.

---

### Step 4 — Search Across Domains

Find at least **three external domains** whose problems share the same structure.

Prefer structural diversity. For example:

- autonomous driving
- aviation maintenance
- semiconductor manufacturing
- medical diagnosis
- robotics
- quantitative finance
- logistics
- radar / sonar
- cybersecurity
- predictive maintenance
- oil & gas
- mining
- wafer inspection
- battery management
- satellite fault management
- CNC machining
- welding
- metrology
- operations research
- control theory
- computer vision
- reinforcement learning
- reliability engineering
- geophysics

For each candidate domain, identify:

1. What is structurally equivalent?
2. What method does that field use?
3. Why might the method transfer?
4. Which assumptions does the source method rely on?

Avoid superficial analogy based only on visual similarity or shared terminology.

---

### Step 5 — Transfer Candidate Methods

For each analog domain, extract only the transferable mechanism.

Possible transferable mechanisms include:

- temporal evidence accumulation
- Bayesian state estimation
- change-point detection
- multi-sensor fusion
- confidence gating
- active sensing
- fault trees
- model predictive control
- receding-horizon planning
- ensemble voting
- graph search
- constraint programming
- robust optimization
- digital shadow synchronization
- active learning
- curriculum learning
- self-supervised pretraining
- human-in-the-loop review
- uncertainty calibration
- redundancy
- graceful degradation
- design of experiments
- adaptive thresholds
- control charts
- survival / reliability models
- morphological filtering
- topology-aware reasoning

Translate the method into the user's domain using engineering variables, not buzzwords.

---

### Step 6 — Perform the Anti-Analogy Test

For every proposed analogy, explicitly identify where it may fail.

Check at least:

- physics mismatch
- scale mismatch
- time-scale mismatch
- observability mismatch
- data-volume mismatch
- label-quality mismatch
- controllability mismatch
- cost-of-error mismatch
- safety / certification mismatch
- stationarity mismatch
- geometry mismatch
- material dependence
- environmental dependence
- causal vs correlational evidence
- simulation-to-reality gap

Give each analogy one of these statuses:

- **Strong transfer candidate**
- **Partial transfer candidate**
- **Conceptual inspiration only**
- **Reject**

Never declare transferability only because a method worked elsewhere.

---

### Step 7 — First-Principles Gate

Before recommending implementation, ask:

1. What physical / geometric / information-theoretic mechanism must be true for this to work?
2. Can that mechanism exist under the user's constraints?
3. What measurable signature would the mechanism produce?
4. What observation would falsify it?
5. Is the proposed method addressing the root state or only a correlated symptom?

If the mechanism cannot be stated clearly, mark the idea as exploratory.

---

### Step 8 — Contradiction Scan

Look for engineering contradictions:

- improve A but degrade B
- improve detection sensitivity but increase nuisance alarms
- increase robustness but lose efficiency
- enlarge support but damage surface / removal
- increase energy but cause spatter / overheating
- reduce data requirements but reduce generalization
- simplify a model but lose mechanism fidelity

For important contradictions, propose:
- separation in time
- separation in space
- separation by condition
- adaptive control
- layered architecture
- dual-mode operation
- local optimization instead of global compromise

This step may borrow from TRIZ, control theory, robust design, or systems engineering, but do not force a named methodology.

---

### Step 9 — Design the Minimum Discriminating Experiment

Do not propose a large validation program first.

Design the **smallest experiment that can distinguish competing explanations**.

For each test include:

- hypothesis
- competing hypothesis
- one variable changed
- variables held constant
- required measurement
- sample / repetition requirement
- expected result if H1 is true
- expected result if H2 is true
- stop / pivot condition
- next action for each possible outcome

Prefer experiments that eliminate entire branches of solution space.

---

### Step 10 — Evidence Ladder

Classify evidence supporting the proposal:

L0 — analogy / intuition  
L1 — simulation or synthetic evidence  
L2 — bench experiment  
L3 — controlled process trial  
L4 — repeated production evidence  
L5 — mechanism + statistical validation  
L6 — qualified / certified process evidence

State which level currently exists and which level is required for the user's decision.

Do not confuse a working demo with production evidence.

---

### Step 11 — Implementation Handoff

For surviving ideas, produce an actionable implementation package:

- minimum viable implementation
- required inputs
- sensors / data
- algorithm or rule
- interface
- expected outputs
- failure handling
- test cases
- success criteria
- what not to automate yet

If software is involved, give a suggested module boundary and data flow.

If physical experimentation is involved, give a test matrix.

If both are involved, separate the software prototype from the process-validation plan.

---

### Step 12 — Learning Loop

At the end, update the reasoning model:

- What was confirmed?
- What was falsified?
- Which analogy survived?
- Which analogy failed and why?
- What new invariant or rule was discovered?
- What should be reused in future problems?

The goal is to convert one-off troubleshooting into an accumulating engineering playbook.

---

# Output Format

Use the following structure by default.

## 1. Problem Restatement
Domain-neutral formulation.

## 2. Known Facts
Only verified or explicitly stated information.

## 3. Hard Constraints
Non-negotiable boundaries.

## 4. Assumptions
Unverified beliefs.

## 5. Unknowns
Information that changes the decision.

## 6. Structural Archetype
Explain the abstract problem class.

## 7. Cross-Domain Analogy Matrix

| External domain | Structurally similar problem | Transferable method | Why it may work | Where analogy breaks | Status |
|---|---|---|---|---|---|

Use at least three domains when possible.

## 8. Candidate Mechanisms
Explain transferred ideas in the user's engineering language.

## 9. First-Principles Check
State mechanism, expected signature, and falsification condition.

## 10. Contradictions / Trade-offs
Show what improves and what may worsen.

## 11. Minimum Discriminating Experiments

| Test | Hypothesis | Single changed variable | Measurement | H1 result | H2 result | Decision |
|---|---|---|---|---|---|---|

## 12. Recommended Next Engineering Move
Do not give a generic "do more research" conclusion.
Give the next smallest action with the highest information value.

## 13. Evidence Level
Current evidence level and target level.

## 14. Reusable Learning
What principle should be carried into future problems.

---

# Special Modes

## Mode A — Rapid Cross-Domain Scan
Use when the user wants ideas quickly.

Output:
- abstract problem
- 3 analog domains
- 1 transferable mechanism from each
- 1 fatal mismatch from each
- 1 minimum test

## Mode B — Deep Engineering Review
Use when the user wants rigorous technical investigation.

Add:
- causal graph
- competing hypotheses
- parameter sensitivities
- evidence ladder
- experiment matrix
- implementation architecture

## Mode C — Failure Investigation
Use for defects, anomalies, quality problems.

Add:
- symptom vs root cause separation
- fault tree
- observability map
- evidence needed to eliminate each branch

## Mode D — Innovation Search
Use when the user explicitly wants unconventional approaches.

Generate candidates from at least five distinct domains.
Rank ideas by:
- mechanism plausibility
- implementation cost
- information gain
- reversibility of trial

Do not rank by novelty alone.

## Mode E — AI / Automation Feasibility
Use when the user proposes an AI system.

Separate:
- sensing problem
- representation problem
- inference problem
- decision problem
- actuation problem
- validation problem

Ask whether AI is solving a real bottleneck or merely replacing a rule that is already easier and safer.

---

# Guardrails

1. Do not invent measurements, machine limits, standards, or process parameters.
2. Do not present analogy as proof.
3. Do not hide failed analogies; failed transfer is useful information.
4. Prefer falsifiable hypotheses over broad narratives.
5. Prefer a cheap discriminating experiment over a large integrated demo.
6. Distinguish correlation, prediction, diagnosis, and causal control.
7. When external current research or standards matter, search and cite them.
8. When the user has provided prior project constraints, reuse them rather than resetting the problem.
9. If the user is a domain expert, treat their observations as high-value evidence but still separate observation from causal interpretation.
10. A software prototype is not equivalent to physical-process validation.

---

# Trigger Examples

- "不要只从SLM领域想，帮我跨领域找办法。"
- "这个问题在其他行业有没有结构相似的解法？"
- "从第一性原理和其他行业类比一下。"
- "给我三个跨领域类比，但要告诉我类比哪里会失效。"
- "这个方案值不值得做，设计一个最小试验。"
- "模型识别不准，人标注又慢，换一个领域的思路解决。"
- "这个监控问题是不是和自动驾驶类似？"
- "不要堆概念，帮我验证这个类比到底成立不成立。"

---

# Compact Invocation Prompt

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
9. 区分“能做Demo、工程可用、生产可用、完成验证”；
10. 最后给出下一步信息价值最高的动作。

不要用跨领域术语堆砌答案。类比不是证据，试验结果才是。
