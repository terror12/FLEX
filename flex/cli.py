# -*- coding: utf-8 -*-
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""
    flex.cli

    This module contains the code which creates flex project's command line
    interface structure.

    :license: GPLv3, see LICENSE for more details.
"""

# import os
#
# import click
# import yaml
# from . import __version__
# #from .carbon import Carbon
# from .constants import TASKLIST, TASK_LOGLEVEL_CHOICES
# from .helpers import template_render, validate_render_scenario
# from .exceptions import HelpersError, CarbonError
#
#
# def print_header():
#     click.echo("-" * 50)
#     click.echo("Carbon Framework v%s" % __version__)
#     click.echo("Copyright (C) 2017 Red Hat, Inc.")
#     click.echo("-" * 50)
#
#
# @click.group()
# @click.option("-v", "--verbose", count=True,
#               help="Add verbosity to the commands.")
# @click.version_option()
# def carbon(verbose):
#     """Carbon - Interoperability Testing Framework"""
#     if verbose:
#         click.echo('\n--- Verbose mode ON (verbosity %s)---\n' % verbose)
#
#
# # @carbon.command()
# def create():
#     """Create a scenario configuration."""
#     raise NotImplementedError
#
#
# @carbon.command()
# @click.option("-s", "--scenario",
#               default=None,
#               metavar="",
#               help="Scenario definition file to be executed.")
# @click.option("-d", "--data-folder",
#               default=None,
#               metavar="",
#               help="Directory for saving carbon runtime files.")
# @click.option("-w", "--workspace",
#               default=None,
#               metavar="",
#               help="Scenario workspace.")
# @click.option("--log-level",
#               type=click.Choice(TASK_LOGLEVEL_CHOICES),
#               default=None,
#               help="Select logging level. (default=info)")
# @click.pass_context
# def validate(ctx, scenario, data_folder, log_level, workspace):
#     """Validate a scenario configuration."""
#     # Make sure the file exists and gets its absolute path
#     if os.path.isfile(scenario):
#         scenario = os.path.abspath(scenario)
#     else:
#         click.echo('You have to provide a valid scenario file.')
#         ctx.exit()
#
#     # Checking if include section is present and getting validated scenario stream/s
#     try:
#         scenario_stream = validate_render_scenario(scenario)
#     except yaml.YAMLError:
#         click.echo('Error loading updated scenario data!')
#         ctx.exit()
#     except HelpersError:
#         click.echo('Included File is invalid or Include section is empty .'
#                    'You have to provide valid scenario files to be included.')
#         ctx.exit()
#     except CarbonError:
#         click.echo('Error loading updated included scenario data!')
#         ctx.exit()
#
#     cbn = Carbon(
#         __name__,
#         log_level=log_level,
#         data_folder=data_folder,
#         workspace=workspace
#     )
#
#     # This is the easiest way to configure a full scenario.
#     cbn.load_from_yaml(scenario_stream)
#
#     # The scenario will start the main pipeline and run through the ordered
#     # list of pipelines. See :function:`~carbon.Carbon.run` for more details.
#     cbn.run(tasklist=["validate"])
#
#
# @carbon.command()
# @click.option("-t", "--task",
#               default=None,
#               type=click.Choice(TASKLIST),
#               multiple=True,
#               help="Select task to run. (default=all)")
# @click.option("-s", "--scenario",
#               default=None,
#               metavar="",
#               help="Scenario definition file to be executed.")
# @click.option("-d", "--data-folder",
#               default=None,
#               metavar="",
#               help="Directory for saving carbon runtime files.")
# @click.option("-w", "--workspace",
#               default=None,
#               metavar="",
#               help="Scenario workspace.")
# @click.option("--log-level",
#               type=click.Choice(TASK_LOGLEVEL_CHOICES),
#               default=None,
#               help="Select logging level. (default=info)")
# @click.pass_context
# def run(ctx, task, scenario, log_level, data_folder, workspace):
#     """Run a scenario configuration."""
#     print_header()
#
#     # Make sure the file exists and gets its absolute path
#     if scenario is not None and os.path.isfile(scenario):
#         scenario = os.path.abspath(scenario)
#     else:
#         click.echo('You have to provide a valid scenario file.')
#         ctx.exit()
#
#     # Checking if include section is present and getting validated scenario stream/s
#     try:
#         scenario_stream = validate_render_scenario(scenario)
#     except yaml.YAMLError:
#         click.echo('Error loading updated scenario data!')
#         ctx.exit()
#     except HelpersError:
#         click.echo('Included File is invalid or Include section is empty .'
#                    'You have to provide valid scenario files to be included.')
#         ctx.exit()
#     except CarbonError:
#         click.echo('Error loading updated included scenario data!')
#         ctx.exit()
#
#     # Create a new carbon compound
#     cbn = Carbon(
#         __name__,
#         log_level=log_level,
#         data_folder=data_folder,
#         workspace=workspace
#     )
#
#     # Sending the list of scenario streams to the carbon object
#     cbn.load_from_yaml(scenario_stream)
#
#     # Setup the list of tasks to run
#     if not task:
#         task = TASKLIST
#     else:
#         task = list(task)
#
#     # The scenario will start the main pipeline and run through the task
#     # pipelines declared. See :function:`~carbon.Carbon.run` for more details.
#     cbn.run(tasklist=task)
#
#
# @carbon.command()
# @click.option("-s", "--scenario",
#               default=None,
#               metavar="",
#               help="Scenario definition file to be executed.")
# @click.option("-l", "--label",
#               default=None,
#               metavar="",
#               help="Creates a list of which Orchestrate tasks to run. (default=all)")
# @click.option("-d", "--data-folder",
#               default=None,
#               metavar="",
#               help="Directory for saving carbon runtime files.")
# @click.option("-w", "--workspace",
#               default=None,
#               metavar="",
#               help="Scenario workspace.")
# @click.option("--log-level",
#               type=click.Choice(TASK_LOGLEVEL_CHOICES),
#               default=None,
#               help="Select logging level. (default=info)")
# @click.pass_context
# def orchestrate(ctx, scenario, label, data_folder, workspace, log_level):
#     """
#     Run a scenario configuration specifically for the orchestration task.
#     :param ctx: Context object which holds state for this particular invocation.
#     """
#     print_header()
#
#     # Make sure the file exists and gets its absolute path
#     if scenario is not None and os.path.isfile(scenario):
#         scenario = os.path.abspath(scenario)
#     else:
#         click.echo('You have to provide a valid scenario file.')
#         ctx.exit()
#
#     # Checking if include section is present and getting validated scenario stream/s
#     try:
#         scenario_stream = validate_render_scenario(scenario)
#     except yaml.YAMLError:
#         click.echo('Error loading updated scenario data!')
#         ctx.exit()
#     except HelpersError:
#         click.echo('Included File is invalid or Include section is empty .'
#                    'You have to provide valid scenario files to be included.')
#         ctx.exit()
#     except CarbonError:
#         click.echo('Error loading updated included scenario data!')
#         ctx.exit()
#
#     # Create a new carbon compound
#     cbn = Carbon(
#         __name__,
#         log_level=log_level,
#         data_folder=data_folder,
#         workspace=workspace
#     )
#
#     # Sending the list of scenario streams to the carbon object
#     cbn.load_from_yaml(scenario_stream)
#
#     # Setup the list of tasks to run
#     # TODO: Update this to mimic ansible skip-tasks
#     task = "Orchestrate"
#     # conver to the list
#     #list = str.split(",")
#     #print "list: ", list
#     label = label.split(",")
#
#     # The scenario will start the main pipeline and run through the task
#     # pipelines declared. See :function:`~carbon.Carbon.run` for more details.
#     cbn.run(tasklist=task, labellist=label)
