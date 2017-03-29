import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_terraform_file(File):
    terraform = File('/usr/local/bin/terraform')

    assert terraform.exists
    assert terraform.is_file
