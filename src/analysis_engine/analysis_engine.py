import pandas as pd
from src.utils.helpers.input_helpers import get_user_query, get_log
from src.utils.helpers.select_function import extract_operation, select_function_based_on_keyword, column_name, \
    build_question

logging = get_log()


class AnalysisEngine:

    @staticmethod
    def analysis_pipeline():
        """
        calling all the function for the pipeline and returning output
        @return function
        """

        operations = ["highest", "lowest", "average"]
        dataframe_columns = ["Facebook_Clicks", "Facebook_Views", "Facebook_bought", "Youtube_Views",
                             "Youtube_Clicks", "Youtube_Followers", "Youtube_bought", "Youtube_Subscription",
                             "Instagram_Views", "Instagram_Clicks", "Instagram_Followers"]

        df = pd.DataFrame(columns=["Question", "Answer"])
        index_counter = 1

        for operation in operations:
            for column in dataframe_columns:
                building_question = build_question(operation, column)
                extracted_column_name = column_name(building_question)

                if extracted_column_name is not None:
                    platform1 = extracted_column_name[0]
                    platform2 = extracted_column_name[1] if len(extracted_column_name) > 1 else None

                    function = select_function_based_on_keyword(building_question, operation, platform1, platform2)
                    question, answer = function

                    df = pd.concat([df, pd.DataFrame({"Question": [question], "Answer": [answer]})],
                                   ignore_index=True)
                    print("\nUpdated Dataframe:")
                    print(df)

                    index_counter += 1

        df.index = pd.RangeIndex(start=1, stop=df.shape[0] + 1)

        df.to_csv("question_answer_dataset.csv", index_label="Index")
        print("Dataframe saved to 'question_answer_dataset.csv'")
        print("Exit")


if __name__ == "__main__":
    analysis_instance = AnalysisEngine()
    analysis_instance.analysis_pipeline()
