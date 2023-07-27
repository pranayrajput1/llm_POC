import unittest
import pytest
import nltk
from nltk import word_tokenize

from src.utils.helpers.input_helpers import get_log

logging = get_log()


class Testing_Helper_Functions:

    def build_question(self, operation, column):
        """
        building question from the operation and column name
        @param operation
        @param column
        @return question
        """
        platform, metric = column.split("_")

        questions = []

        questions.append(f"What is the {operation} count of {platform} {metric}?")
        questions.append(f"Tell me the {operation} count of {platform} {metric}.")
        questions.append(f"What are the {operation} statistics for {platform} {metric}?")
        questions.append(f"Give me the {operation} count of {platform} {metric}.")
        questions.append(f"Identify the {operation} count of {platform} {metric}?")
        return questions

    def column_name(self, question):
        """
        Checking if there is any match for the column name from the candidates.
        @param question
        @return matching_columns
        """
        dataframe_columns = ["Facebook_Clicks", "Facebook_Views", "Facebook_bought", "Youtube_Views",
                             "Youtube_Clicks", "Youtube_Followers", "Youtube_bought", "Youtube_Subscription",
                             "Instagram_Views", "Instagram_Clicks", "Instagram_Followers"]
        dataframe_columns_lower = [column.lower() for column in dataframe_columns]

        candidates_list = self.preprocess_question([question])

        matching_columns_list = []

        for candidates in candidates_list:
            matching_columns = [dataframe_columns[dataframe_columns_lower.index(candidate)] for candidate in candidates
                                if
                                candidate in dataframe_columns_lower]
            matching_columns_list.extend(matching_columns)  # Extend the list instead of appending

        logging.info("Task : Finding the column")

        return matching_columns_list[0] if matching_columns_list else None

    def preprocess_question(self, questions):
        """
        generating combination of tokens to form potential column name in sequence
        @param questions
        @return candidates
        """
        stop_words = set(nltk.corpus.stopwords.words('english'))
        candidates_list = []

        for question in questions:
            tokens = word_tokenize(question.lower())
            tokens = [token for token in tokens if token not in stop_words]

            candidates = []
            for i in range(1, len(tokens) + 1):
                for j in range(len(tokens) - i + 1):
                    candidate = "_".join(tokens[j:j + i])
                    candidates.append(candidate)

            candidates_list.append(candidates)

        logging.info("Calculated the combination of column names for each question")
        return candidates_list


class Test_class(unittest.TestCase):
    def test_for_building_question(self):
        operation = "highest"
        column = "Facebook_Clicks"

        helper_functions = Testing_Helper_Functions()
        actual_questions = helper_functions.build_question(operation, column)

        expected_questions = [
            "What is the highest count of Facebook Clicks?",
            "Tell me the highest count of Facebook Clicks.",
            "What are the highest statistics for Facebook Clicks?",
            "Give me the highest count of Facebook Clicks.",
            "Identify the highest count of Facebook Clicks?"
        ]

        self.assertEqual(actual_questions, expected_questions)

    def test_for_column_name(self):
        helper_functions = Testing_Helper_Functions()

        question1 = "What are the highest statistics for Facebook Clicks?"
        expected_result1 = "Facebook_Clicks"

        question2 = "Give me the lowest count of Youtube Followers."
        expected_result2 = "Youtube_Followers"

        question3 = "Tell me the average value of Instagram Views."
        expected_result3 = "Instagram_Views"

        actual_result1 = helper_functions.column_name(question1)
        actual_result2 = helper_functions.column_name(question2)
        actual_result3 = helper_functions.column_name(question3)

        self.assertEqual(actual_result1, expected_result1)
        self.assertEqual(actual_result2, expected_result2)
        self.assertEqual(actual_result3, expected_result3)

        question4 = "What is the highest count of Twitter Likes?"
        expected_result4 = None

        actual_result4 = helper_functions.column_name(question4)

        self.assertEqual(actual_result4, expected_result4)


if __name__ == "__main__":
    unittest.main()
