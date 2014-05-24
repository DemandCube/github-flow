github-flow
===========

Command line tool for github, seeing open pull requests, issue and etc, for a Organization or Repo


- This is part of [NeverwinterDP the Data Pipeline for Hadoop](https://github.com/DemandCube/NeverwinterDP)




## Installation

```
pip install githubflow
```

## Contributing

See the [NeverwinterDP Guide to Contributing] (https://github.com/DemandCube/NeverwinterDP#how-to-contribute)


* * *

## Usage and Specs
github-flow has 1 command `ghf` and the following subcommands:

```
add-command1
```

- command1
  - Description of command1

Example flow to be enabled
```
pip install githubflow
ghf ......TODO......
```


# Usage

* * *
## command 1
```
Usage: ghf command1  [-hgliq]

TODO REPLACE WITH ACTUALL
This looks for multiinit.yml as the default configuration

    -g FILEPATH,                     (Optional) YAML file containing vagrant cloud config
        --vagrant_multiinit_config_file
    -l hostname:cloud/location,hostname2:cloud/location2,hostname3:cloud/location3,
        --list                       List of cloud config parameters
    -i, --vboxintnet NAME            (Optional) Custom virtualbox__intnet name for private network
    -q, --quiet                      (Optional) Suppress output to STDOUT and STDERR
    -h, --help                       Print this help
```

#### Example usages of multiinit
This will look for a file in the pwd named multiinit.yml and attempt to make the Vagrantfile
```
ghf command1
```


Example number 2
```
ghf command1 some option
```

### Use case
- You'll do this


* * *

# PRD - Product Requirement Document

`ghf org[/repo] command`

Repo authentication should use a common mechanism (can it piggy back off of what git uses ?) or something like netrc

TODO: make sure these command don't already exist from the commandline

### Commands
`issues`
- create issue
 
`pull[-requests]`
- open pull requests (can this already be done from the commandline?)
  - If already exists maybe print how todo this
- list all open pull requests

`repos[itories]`

`team`
- list all contributors to a org
 

Eventually should have a plugin architecture to allow things like other commands e.g. huboard

`ghf org[/repo] huboard`
- move issue to next stage
- list all stages



Needs pip install
Create config template

* * *

# Libraries
- Click <http://click.pocoo.org/>
- PyGithub <https://github.com/jacquev6/PyGithub>
- Whoosh <https://pypi.python.org/pypi/Whoosh> <https://pypi.python.org/pypi/WhooshDoc/1.0>

# Supporting Libraries
- Building with setuptools <https://pythonhosted.org/setuptools/>
- Testing with nose <https://nose.readthedocs.org/en/latest/>
- Testing with unittest <https://docs.python.org/2/library/unittest.html>
- Documentation with Sphinx <http://sphinx-doc.org/>
- Deployment with Pip <http://www.pip-installer.org/en/latest/>
- Development with Virtualenv <http://www.virtualenv.org/en/latest/>
- Config Mangement Ansible <https://github.com/ansible/ansible>
- Tabular output <https://pypi.python.org/pypi/tabulate/0.7.2>

# Supporting Services
- Badge <http://badge.fury.io/>
- PyPi <https://pypi.python.org/pypi>

# Github API
- https://developer.github.com/v3/
- https://developer.github.com/libraries/


# plugins

Use this to develop plugins
- https://pythonhosted.org/setuptools/setuptools.html#dynamic-discovery-of-services-and-plugins
- https://nose.readthedocs.org/en/latest/plugins/builtin.html
- https://nose.readthedocs.org/en/latest/plugins/writing.html


# References 
- Distutils <https://docs.python.org/2.7/distutils/>
- Version Comparison Distutils <https://wiki.python.org/moin/Distutils/VersionComparison>

# Active Development Bookmarks
- Example setup.py <https://github.com/ansible/ansible/blob/devel/setup.py>
- <http://click.pocoo.org/setuptools/#introduction>

# other github command line tools
- https://github.com/sociomantic/git-hub
- https://github.com/github/hub
- https://github.com/stephencelis/ghi
- http://nodegh.io/
- https://github.com/jsmits/github-cli
