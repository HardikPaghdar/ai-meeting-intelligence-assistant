import unittest
from app import analyze_transcript

class MeetingTests(unittest.TestCase):
    def test_extracts_actions_and_decisions(self):
        result = analyze_transcript("Decision: launch the beta next month.\nMaya will prepare the release checklist.")
        self.assertIn("launch the beta next month", result["decisions"][0])
        self.assertEqual(result["action_items"][0]["owner"], "Maya")
        self.assertIn("checklist", result["action_items"][0]["task"])
    def test_empty_input_rejected(self):
        with self.assertRaises(ValueError): analyze_transcript("  ")
    def test_summary_is_bounded(self):
        result = analyze_transcript("\n".join(["A long agenda item."] * 100))
        self.assertLessEqual(len(result["summary"]), 600)

if __name__ == "__main__": unittest.main()
