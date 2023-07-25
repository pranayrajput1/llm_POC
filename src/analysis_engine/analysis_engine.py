import pandas as pd
from src.utils.helpers.input_helpers import get_user_query
from src.utils.helpers.select_function import extract_operation, select_function_based_on_keyword, column_name, get_log

logging = get_log()
df = pd.DataFrame(columns=["Question", "Answer"])


class AnalysisEngine:

    @staticmethod
    def analysis_pipeline():
        """
        calling all the function for the pipeline and returning output
        @return function
        """
        user_query = get_user_query()
        operation = extract_operation(user_query)
        extracted_column_name = column_name(user_query)
        if extracted_column_name is not None:
            platform1 = extracted_column_name[0]
            platform2 = extracted_column_name[1] if len(extracted_column_name) > 1 else None

            function = select_function_based_on_keyword(user_query,operation, platform1, platform2)
            return function
        else:
            return "No matching column names found in the input query."


if __name__ == "__main__":
    analysis_instance = AnalysisEngine()
    while True:
        question, answer = analysis_instance.analysis_pipeline()

        df = pd.concat([df, pd.DataFrame({"Question": [question], "Answer": [answer]})], ignore_index=True)

        print("\nUpdated Dataframe:")
        print(df)

        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() != "y":
            df.to_csv("question_answer_dataset.csv", index=False)
            print("Dataframe saved to 'question_answer_dataset.csv'")
            print("Goodbye!")
            break


