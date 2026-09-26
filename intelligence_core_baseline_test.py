from intelligence_core import IntelligenceCore


class AlwaysH1:
    def predict(self, hypotheses, history):
        return "X"


class AlwaysH2:
    def predict(self, hypotheses, history):
        return "Y"


class LatestResult:
    def predict(self, hypotheses, history):
        if not history:
            return "X"
        return history[-1]


class Majority:
    def predict(self, hypotheses, history):
        if not history:
            return "X"

        x = history.count("X")
        y = history.count("Y")

        return "X" if x >= y else "Y"


def core_predict(core, observation, hypotheses, result):
    return core.cycle(
        observation={"signal": observation},
        hypotheses=hypotheses,
        actual_result=result,
    )["prediction"]


def run_sequence(name, results):

    hypotheses = [
        {"id": "H1", "prediction": "X"},
        {"id": "H2", "prediction": "Y"},
    ]

    models = {
        "ALWAYS_X": AlwaysH1(),
        "ALWAYS_Y": AlwaysH2(),
        "LATEST": LatestResult(),
        "MAJORITY": Majority(),
        "CORE": IntelligenceCore(),
    }

    histories = {name: [] for name in models}
    correct = {name: 0 for name in models}

    print()
    print("===", name, "===")
    print("RESULTS:", results)

    for actual in results:

        for model_name, model in models.items():

            history = histories[model_name]

            if model_name == "CORE":
                prediction = core_predict(
                    model,
                    "A",
                    hypotheses,
                    actual,
                )
            else:
                prediction = model.predict(
                    hypotheses,
                    history,
                )

            if prediction == actual:
                correct[model_name] += 1

            history.append(actual)

    print("CORRECT:", correct)

    for model_name in models:
        print(
            model_name,
            "ACCURACY:",
            correct[model_name] / len(results)
        )


def main():

    print("=== INTELLIGENCE CORE BASELINE TEST ===")

    run_sequence(
        "STABLE",
        ["X", "X", "X", "X", "X", "X"],
    )

    run_sequence(
        "SWITCH",
        ["X", "X", "X", "Y", "Y", "Y"],
    )

    run_sequence(
        "ALTERNATING",
        ["X", "Y", "X", "Y", "X", "Y"],
    )

    run_sequence(
        "MAJORITY_X",
        ["X", "X", "Y", "X", "X", "Y"],
    )

    run_sequence(
        "MAJORITY_Y",
        ["Y", "Y", "X", "Y", "Y", "X"],
    )

    run_sequence(
        "UNKNOWN_PATTERN",
        ["X", "Y", "Y", "X", "Y", "X", "X", "Y"],
    )

    print()
    print("=== BASELINE TEST COMPLETE ===")
    print("NO DESIGN CHANGE")


if __name__ == "__main__":
    main()
