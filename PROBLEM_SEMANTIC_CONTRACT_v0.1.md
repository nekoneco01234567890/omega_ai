# ΩAI PROBLEM SEMANTIC CONTRACT v0.1

STATUS: FORMALLY_ADOPTED
TYPE: SEMANTIC_ONLY

## DEFINITION

Problem = Goalに関係する未解決事項

## MINIMAL SEMANTIC COMPONENTS

A Problem consists of:

1. Goal
2. Relevant Matter
3. Unresolvedness

つまり、

Goal
  ↓
Relevant Matter
  ↓
Unresolvedness
  ↓
Problem


## SEMANTIC MEANING

Problemは、
現在のGoalに関係し、
まだ解消・確定・説明・判断等が成立していない事項を表す。

ただし、具体的な解消方法や行動をProblemの意味そのものには含めない。


## REQUIRED

- Goal
- Goal relevance
- Unresolved matter


## NOT REQUIRED

- Question
- Action
- Resolution method
- Problem status
- Problem ID
- Problem class
- Persistent storage
- Database relation
- Inference algorithm
- Planner integration


## BOUNDARIES

Goal != Problem

Problem != Achievement Condition

Problem != Result

Problem != WorldModel Knowledge

Problem != Reasoner Decision

Problem != Action

Problem != Question


## RELATION TO GAR

GAR defines:

Goal
  ↓
Achievement Condition
  ↓
Semantic Result
  ↓
Achievement Evaluation

Problem is not identical to any of these.

Problem may exist before achievement evaluation,
during achievement evaluation,
or independently of a concrete action.


## RELATION TO WORLDMODEL

WorldModel represents:

- observation
- results
- history_count
- stable
- conflict
- unknown

Problem is not equivalent to:

- UNKNOWN
- CONFLICT
- STABLE
- Result

Evidence state and Problem semantics remain distinct.


## RELATION TO REASONER

Reasoner:

Knowledge -> Decision

Problem does not replace Reasoner Decision.

Problem describes a Goal-relevant unresolved matter.

Reasoner describes a decision state derived from Knowledge.


## IMPLEMENTATION BOUNDARY

This document defines WHAT a Problem means.

It does NOT require:

- Problem class
- Problem object
- Problem storage
- Problem ID
- Problem status enum
- Problem inference engine
- Planner
- Runtime integration
- WorldModel schema change
- Reasoner change


## VALIDATION BASIS

The contract was tested against:

- abstract Goal
- changing Goal
- multiple Goals
- multiple unresolved matters
- achievement evaluation uncertainty
- uncertainty about Problem existence
- relational Problems
- constraint-related Problems
- Problems without explicit Questions
- Problems without selected Actions

No tested counterexample falsified the minimal contract.


## PROVENANCE

This semantic contract is derived from ΩAI's internal semantic audits and consistency checks against:

- OMEGA PURPOSE v0.1
- GAR Semantic Contract v0.1
- Goal semantics
- WorldModel v1
- Reasoner v2

No authoritative external definition was established.

Therefore this is an ΩAI internal semantic contract.


## FORMAL STATUS

PROBLEM_SEMANTIC_CONTRACT: FORMALLY_ADOPTED

PROBLEM_SEMANTIC_STATUS: ADOPTED

PROBLEM_IMPLEMENTATION_REQUIRED: NO

WORLD_MODEL_CHANGE_REQUIRED: NO

REASONER_CHANGE_REQUIRED: NO

PLANNER_REQUIRED: NO

PRODUCTION_CHANGE: NONE


## IMPORTANT LIMIT

Formal adoption of this semantic contract does NOT establish that ΩAI currently possesses the capability to automatically identify Problems.

Problem identification remains a separate capability question.

That capability must be independently justified from Purpose,
current architecture, evidence, and capability-gap analysis.
