[![build-test](https://github.com/darkwizard242/ansible-role-bravebrowser/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-bravebrowser/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-bravebrowser/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-bravebrowser/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/56498?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/56498?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/56498?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-bravebrowser&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-bravebrowser) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-bravebrowser&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-bravebrowser) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-bravebrowser&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-bravebrowser) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-bravebrowser&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-bravebrowser) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-bravebrowser?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-bravebrowser?color=orange&style=flat-square)

# Ansible Role: bravebrowser

Role to install (_by default_) [Brave browser](https://brave.com/) package or uninstall (_if passed as var_) on Debian based systems and EL based systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables List:

```yaml
bravebrowser_app: brave-browser
bravebrowser_app_desired_state: present

# Debian family based
bravebrowser_repo_debian_gpg_key: https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
bravebrowser_repo_debian: "deb [arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"
bravebrowser_repo_debian_filename: "{{ bravebrowser_app }}"
bravebrowser_repo_debian_desired_state: present

# EL family based
bravebrowser_repo_el: "https://brave-browser-rpm-release.s3.brave.com/x86_64/"
bravebrowser_repo_el_name: brave-browser
bravebrowser_repo_el_description: brave-browser
bravebrowser_repo_el_gpgkey: https://brave-browser-rpm-release.s3.brave.com/brave-core.asc
bravebrowser_repo_el_gpgcheck: yes
bravebrowser_repo_el_enabled: yes
bravebrowser_repo_el_filename: "{{ bravebrowser_app }}"
bravebrowser_repo_el_desired_state: present
```

### Variables table:

Variable                               | Description
-------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
bravebrowser_app                       | Name of Brave browser application package require to be installed i.e. `brave-browser`
bravebrowser_app_desired_state         | State of the Brave browser package. Whether to install, verify if available or to uninstall (i.e. ansible apt module values: `present`, `latest`, or `absent`)
bravebrowser_repo_debian_gpg_key       | Brave browser key required on Debian family systems.
bravebrowser_repo_debian               | Brave browser repo URL for Debain family systems.
bravebrowser_repo_debian_filename      | Name of the repository file that will be stored at `/etc/apt/sources.list.d/` on Debian based systems.
bravebrowser_repo_debian_desired_state | `present` indicates creating the repository file if it doesn't exist on Debian based systems. Alternative is `absent` (not recommended as it will prevent from installation of **brave-browser** package).
bravebrowser_repo_el                   | Repository `baseurl` for Brave browser on EL based systems.
bravebrowser_repo_el_name              | Repository name for Brave browser on EL based systems.
bravebrowser_repo_el_description       | Description to be added in EL based repository file for Brave browser.
bravebrowser_repo_el_gpgkey            | Brave browser GPG key required on EL family systems
bravebrowser_repo_el_gpgcheck          | Boolean for whether to perform gpg check against Brave browser on EL based systems.
bravebrowser_repo_el_enabled           | Boolean to set so that Brave browser repository is enabled on EL based systems.
bravebrowser_repo_el_filename          | Name of the repository file that will be stored at `/yum/sources.list.d/brave-browser.repo` on EL based systems.
bravebrowser_repo_el_desired_state     | `present` indicates creating the repository file if it doesn't exist on EL based systems. Alternative is `absent` (not recommended as it will prevent from installation of **brave-browser** package).

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **brave-browser** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.bravebrowser
```

For customizing behavior of role (i.e. installing/upgrading to latest version of teams as an example) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.bravebrowser
  vars:
    bravebrowser_apps_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **brave-browser** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.bravebrowser
  vars:
    bravebrowser_apps_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-bravebrowser/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://alimuhammad.dev).
