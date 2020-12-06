from unittest import TestCase

from core_get.cli.parse.options_parsers.install_options_parser import InstallOptionsParser
from test.cli.parse.options_parsers.options_parser_test_helper import test_parse


class TestInstallOptionsParser(TestCase):
    def test_parses_correctly(self):
        install_options = test_parse(InstallOptionsParser, 'my-package-name')
        self.assertEqual(['my-package-name'], install_options.package_names)

    def test_parses_two_packages_correctly(self):
        install_options = test_parse(InstallOptionsParser, 'my-package-1', 'my-package-2')
        self.assertEqual(['my-package-1', 'my-package-2'], install_options.package_names)

    def test_fails_with_no_package_name(self):
        with self.assertRaises(SystemExit):
            test_parse(InstallOptionsParser)
