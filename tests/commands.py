import unittest
import os
import sys
import subprocess


class TestCommands(unittest.TestCase):
    def test_new(self):
        # Descomment this when  will test with windows
        # if sys.platform.startswith("win32"):
        #     self.assertEqual(os.system("type nul > ../home/test1.py"), 0)
        #     self.assertEqual(os.system("type nul > ../home/test2.py"), 0)
        #     self.assertEqual(os.system("type nul > ../home/test3.py"), 0)
        # else:
        self.assertEqual(subprocess.call(["touch", "../home/test1.py"]), 0)
        self.assertEqual(subprocess.call(["touch", "../home/test2.py"]), 0)
        self.assertEqual(subprocess.call(["touch", "../home/test3.py"]), 0)


if __name__ == "__main__":
    unittest.main()
