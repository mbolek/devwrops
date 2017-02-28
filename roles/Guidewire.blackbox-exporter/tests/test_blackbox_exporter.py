from testinfra.utils.ansible_runner import AnsibleRunner


testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_configuration(File):
    blackbox_config = File("/etc/blackbox.yml")
    assert blackbox_config.contains("modules")
    assert blackbox_config.user == "root"
    assert blackbox_config.group == "root"
    assert blackbox_config.mode == 0o644


def test_service_running_and_enabled(File, Command):
    blackbox_config = File("/etc/default/blackbox-exporter")
    assert blackbox_config.contains("START=yes")
    assert blackbox_config.user == "root"
    assert blackbox_config.group == "root"
    assert blackbox_config.mode == 0o644

    blackbox_service = Command("/sbin/service blackbox-exporter status")
    assert blackbox_service.rc == 0
