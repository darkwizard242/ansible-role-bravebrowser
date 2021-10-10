import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'brave-browser'
PACKAGE_BINARY = '/usr/bin/brave-browser'
DEBIAN_REPO_FILE = '/etc/apt/sources.list.d/brave-browser.list'
EL_REPO_FILE = '/etc/yum.repos.d/brave-browser.repo'


def test_bravebrowser_package_installed(host):
    """
    Tests if brave-browser is installed.
    """
    assert host.package("brave-browser").is_installed


def test_bravebrowser_binary_exists(host):
    """
    Tests if brave-browser binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_bravebrowser_binary_file(host):
    """
    Tests if brave-browser binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_bravebrowser_binary_which(host):
    """
    Tests the output to confirm brave-browser's binary location.
    """
    assert host.check_output('which brave-browser') == PACKAGE_BINARY


def test_bravebrowser_repo_exists(host):
    """
    Tests if brave-browser repo exists on DEBIAN/EL Systems.
    """
    assert host.file(DEBIAN_REPO_FILE).exists or \
        host.file(EL_REPO_FILE).exists


def test_bravebrowser_repo_file(host):
    """
    Tests if brave-browser repo is a file type on DEBIAN/EL Systems.
    """
    assert host.file(DEBIAN_REPO_FILE).is_file or \
        host.file(EL_REPO_FILE).is_file
