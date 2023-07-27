import pandas as pd
from src.utils.helpers.input_helpers import get_user_query, get_log
from src.utils.helpers.select_function import select_function_based_on_keyword, column_name, \
    build_question

logging = get_log()


class AnalysisEngine:

    @staticmethod
    def analysis_pipeline():
        """
        calling all the function for the pipeline and returning output
        @return function
        """

        operations = ["highest", "lowest", "average","greatest","peak","least"]
        dataframe_columns = ["Facebook_Clicks", "Facebook_Views", "Facebook_bought", "Youtube_Views",
                             "Youtube_Clicks", "Youtube_Followers", "Youtube_bought", "Youtube_Subscription",
                             "Instagram_Views", "Instagram_Clicks", "Instagram_Followers"]
        questions = []
        answers = []

        for operation in operations:
            for column in dataframe_columns:
                building_questions = build_question(operation, column)
                questions.extend(building_questions)

                for question in building_questions:
                    extracted_col_names = column_name(question)
                    answer = select_function_based_on_keyword(question, operation, extracted_col_names)
                    answers.append(answer[1])

        df = pd.DataFrame({"Question": questions, "Answer": answers})
        df.index = pd.RangeIndex(start=1, stop=df.shape[0] + 1)

        df.to_csv("question_answer_dataset.csv", index_label="Index")
        print("Dataframe saved to 'question_answer_dataset.csv'")
        print("Exit")


if __name__ == "__main__":
    analysis_instance = AnalysisEngine()
    analysis_instance.analysis_pipeline()
