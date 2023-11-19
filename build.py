from pybuilder.core import use_plugin, init, task

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.pytest")
use_plugin("python.flake8")
use_plugin("python.pylint")
use_plugin("python.bandit")

default_task = "publish"

@init
def set_properties(project):
    project.build_depends_on('prometheus_client', 'requests')
