# ΩAI ACTION SELECTION SEMANTIC CONTRACT v0.1

STATUS: FORMALLY_ADOPTED / SEMANTIC_ONLY

## DEFINITION

Action Selection
= 目的に関係する次の観測または行動を定めること

## MINIMUM SEMANTICS

Action Selectionは、目的に関係する対象について、
次に扱う観測または行動を定める意味を持つ。

複数の対象を許容する。

唯一のActionを選ぶことを要求しない。

## DOES NOT REQUIRE

- UNIQUE_ACTION
- SINGLE_TARGET
- OPTIMIZATION
- RANKING
- SELECTION_CRITERION
- CANDIDATE_GENERATION
- PLANNER
- EXECUTION
- RUNTIME_COMPONENT

## BOUNDARIES

Action Selection != Goal

Action Selection != Problem

Action Selection != Representation

Action Selection != Achievement Evaluation

Action Selection != WorldModel Knowledge

Action Selection != Reasoner Decision

Action Selection != Execution

## RELATION TO PURPOSE

Purpose contains:

「目的達成に必要な次の観測・行動を選ぶ」

Existing formal semantic contracts did not explicitly represent
the meaning of determining the next observation or action.

This contract fills that semantic gap without defining
an implementation strategy.

## UNDEFINED BY THIS CONTRACT

- how candidates are generated
- how multiple candidates are compared
- how one candidate is selected
- what happens when no target exists
- uncertainty handling
- execution procedure

These remain open requirements.

## IMPLEMENTATION BOUNDARY

Formal semantic adoption does not require implementation.

The following remain UNCONFIRMED:

- independent runtime component
- Planner
- candidate-generation capability
- selection algorithm
- selection criterion

## STATUS

ACTION_SELECTION_SEMANTIC_CONTRACT: ADOPTED

SEMANTIC_GAP: CLOSED

IMPLEMENTATION_REQUIRED: NO

PRODUCTION_CHANGE: NONE

PLANNER_REQUIRED: UNCONFIRMED

CANDIDATE_GENERATOR_REQUIRED: UNCONFIRMED
