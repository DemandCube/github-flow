github-flow
===========

Command line tool for github, seeing open pull requests, issue and etc, for a Organization or Repo


- This is part of [NeverwinterDP the Data Pipeline for Hadoop](https://github.com/DemandCube/NeverwinterDP)

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


# Supporting Services
- Badge <http://badge.fury.io/>
- PyPi <https://pypi.python.org/pypi>


# plugins

Use this to develop plugins
- https://pythonhosted.org/setuptools/setuptools.html#dynamic-discovery-of-services-and-plugins
- https://nose.readthedocs.org/en/latest/plugins/builtin.html


# References 
- Distutils <https://docs.python.org/2.7/distutils/>
- Version Comparison Distutils <https://wiki.python.org/moin/Distutils/VersionComparison>

# Active Development Bookmarks
- Example setup.py <https://github.com/ansible/ansible/blob/devel/setup.py>
- <http://click.pocoo.org/setuptools/#introduction>
