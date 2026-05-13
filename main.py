import pandas as pd
from src.eda_agent.agents.eda_agent import EDAAgent


def main():
    # Example: use a small DataFrame for local test
    df = pd.DataFrame(
        {
            "a": [1, 2, None, 4],
            "b": [5, None, 7, 8],
        }
    )
    agent = EDAAgent()
    output = agent.run(["summary_statistics", "missing_value_analysis"], df)
    print(output)


if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
