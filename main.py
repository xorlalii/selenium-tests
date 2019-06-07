import unittest
import HtmlTestRunner
import os


def run():

    # get the directory path to output report file
    dir = os.getcwd()

    # get all tests from tests folder and load test(loader.discover)
    loader = unittest.TestLoader()
    start_dir = os.path.join(dir, "tests")
    tests = loader.discover(start_dir)

    # create a test suite
    test_suite = unittest.TestSuite(tests)

    # configure HTMLTestRunner options
    runner = HtmlTestRunner.HTMLTestRunner(
        combine_reports=True, report_name='Test Report', report_title='Acceptance Tests',
        open_in_browser=True
    )

    # run the suite using HTMLTestRunner
    runner.run(test_suite)


if __name__ == '__main__':
    # unittest.main()
    run()
