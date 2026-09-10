import unittest

from student_information import generate_username, normalize_name


class StudentInformationTests(unittest.TestCase):
    def test_normalize_name_trims_and_capitalizes(self):
        self.assertEqual(normalize_name("  jOhN   doE  "), "John Doe")

    def test_generate_username_ignores_name_punctuation(self):
        self.assertEqual(generate_username("Jo.hn D'oe", "12345"), "joh12345")

    def test_generate_username_ignores_student_id_punctuation(self):
        self.assertEqual(generate_username("John Doe", "A/12-3"), "johA123")

    def test_generate_username_has_safe_fallback_prefix(self):
        self.assertEqual(generate_username("!!!", "12345"), "std12345")


if __name__ == "__main__":
    unittest.main()
