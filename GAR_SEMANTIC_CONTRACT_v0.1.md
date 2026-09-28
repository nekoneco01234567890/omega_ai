# ΩAI GAR Semantic Contract v0.1

STATUS: FORMALLY_ADOPTED / SEMANTIC_ONLY
PRODUCTION_CHANGE: NONE

## 1. PURPOSE

GARは、ΩAIにおける
Goal / Achievement Condition / Semantic Result
の最小意味論を定義する。

これはPlanner、Policy、Action、Learner、WorldModel全体を
定義する契約ではない。

## 2. GOAL

Goalは、

「望ましい状態・方向」

を表す。

Goalは以下を内包しない。

- 具体的Action
- Action Selection Policy
- Achievement Condition
- Execution Status
- Semantic Result

現在の実装では `AIState.goal: str` を維持する。

## 3. ACHIEVEMENT CONDITION

Achievement Conditionは、

「Goalを満たしたと判断する観測可能な条件」

を表す。

最低条件:

- Goalと関係付けられる
- 観測可能である
- Semantic Resultと比較可能である

時間条件、閾値条件、関係条件は、
現時点では必須要件として採用しない。

## 4. SEMANTIC RESULT

Semantic Resultは、

「ActionまたはObservation後に観測された意味的結果」

を表す。

Semantic ResultはExecution Statusとは異なる。

現在のΩAIでは `Experience.actual_result`
が既存のResult保持経路として存在する。

## 5. ACHIEVEMENT EVALUATION

Achievement Evaluationは、

Semantic ResultとAchievement Conditionを比較し、

Goalが満たされたかを評価する関係

とする。

## 6. UNKNOWN BOUNDARY

UNKNOWNはFAILUREを意味しない。

Semantic ResultがUNKNOWNの場合、

「Achievementが成立したことを確認できない」

とする。

## 7. FORBIDDEN SEMANTIC COLLAPSES

以下を同一視しない。

Goal == Achievement Condition
Result == Achievement
Execution Status == Result
Execution Status == Achievement
UNKNOWN == FAILURE

## 8. ARCHITECTURAL BOUNDARY

GARは以下を定義しない。

- Problem Definition
- Representation Definition
- WorldModel
- Hypothesis Generation
- Hypothesis Search
- Action Selection
- Planner
- Policy
- Learning Algorithm
- Causal Reasoning

これらは別途、必要性が証拠によって確認された場合に検証する。

## 9. IMPLEMENTATION BOUNDARY

本契約の採用によって、

- AIStateの変更
- Goal schema変更
- Achievement Condition class追加
- Result class追加
- Planner追加
- Reasoner変更

を自動的には行わない。

意味論の固定と実装要求を分離する。

## 10. MINIMAL CONTRACT

Goal
    ↓
Achievement Condition
    ↓
Semantic Result
    ↓
Achievement Evaluation

この関係をGARの最小意味論とする。

## 11. STATUS

GAR semantic core:
STABLE

Missing mandatory bridge concept:
NOT_IDENTIFIED

Formal semantic adoption:
ADOPTED

Production implementation:
NOT_REQUIRED

Production change:
NONE
