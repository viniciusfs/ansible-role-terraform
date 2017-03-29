# Ansible role: Terraform

Installs Terraform in Ubuntu Desktop. :joy_cat:


## Role Variables

* `terraform_version`:
    - Description: Terraform version to install
    - Default: `0.9.2`

* `terraform_arch`:
    - Description: System arch to install
    - Default: `amd64`

* `terraform_package_url`:
    - Description: URL for installation package
    - Default: `https://releases.hashicorp.com/terraform/{{ terraform_version }}/terraform_{{ terraform_version }}_linux_{{ terraform_arch }}.zip`

* `terraform_destination`:
    - Description: Terraform binary installation path
    - Default: `/usr/local/bin`

## Example Playbook

    - hosts: workstations
      roles:
        - { role: viniciusfs.terraform }


## License

MIT


## Author Information

* Vinícius Figueiredo <viniciusfs@gmail.com>
