# coding: utf-8

"""
    flyteidl/service/admin.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flyteadmin.models.core_execution_error import CoreExecutionError  # noqa: F401,E501
from flyteadmin.models.core_literal_map import CoreLiteralMap  # noqa: F401,E501
from flyteadmin.models.core_node_execution_phase import CoreNodeExecutionPhase  # noqa: F401,E501
from flyteadmin.models.core_output_data import CoreOutputData  # noqa: F401,E501
from flyteadmin.models.flyteidladmin_task_node_metadata import FlyteidladminTaskNodeMetadata  # noqa: F401,E501
from flyteadmin.models.flyteidladmin_workflow_node_metadata import FlyteidladminWorkflowNodeMetadata  # noqa: F401,E501


class AdminNodeExecutionClosure(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'output_uri': 'str',
        'error': 'CoreExecutionError',
        'output_data': 'CoreLiteralMap',
        'full_outputs': 'CoreOutputData',
        'phase': 'CoreNodeExecutionPhase',
        'started_at': 'datetime',
        'duration': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'workflow_node_metadata': 'FlyteidladminWorkflowNodeMetadata',
        'task_node_metadata': 'FlyteidladminTaskNodeMetadata',
        'deck_uri': 'str',
        'dynamic_job_spec_uri': 'str'
    }

    attribute_map = {
        'output_uri': 'output_uri',
        'error': 'error',
        'output_data': 'output_data',
        'full_outputs': 'full_outputs',
        'phase': 'phase',
        'started_at': 'started_at',
        'duration': 'duration',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'workflow_node_metadata': 'workflow_node_metadata',
        'task_node_metadata': 'task_node_metadata',
        'deck_uri': 'deck_uri',
        'dynamic_job_spec_uri': 'dynamic_job_spec_uri'
    }

    def __init__(self, output_uri=None, error=None, output_data=None, full_outputs=None, phase=None, started_at=None, duration=None, created_at=None, updated_at=None, workflow_node_metadata=None, task_node_metadata=None, deck_uri=None, dynamic_job_spec_uri=None):  # noqa: E501
        """AdminNodeExecutionClosure - a model defined in Swagger"""  # noqa: E501

        self._output_uri = None
        self._error = None
        self._output_data = None
        self._full_outputs = None
        self._phase = None
        self._started_at = None
        self._duration = None
        self._created_at = None
        self._updated_at = None
        self._workflow_node_metadata = None
        self._task_node_metadata = None
        self._deck_uri = None
        self._dynamic_job_spec_uri = None
        self.discriminator = None

        if output_uri is not None:
            self.output_uri = output_uri
        if error is not None:
            self.error = error
        if output_data is not None:
            self.output_data = output_data
        if full_outputs is not None:
            self.full_outputs = full_outputs
        if phase is not None:
            self.phase = phase
        if started_at is not None:
            self.started_at = started_at
        if duration is not None:
            self.duration = duration
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if workflow_node_metadata is not None:
            self.workflow_node_metadata = workflow_node_metadata
        if task_node_metadata is not None:
            self.task_node_metadata = task_node_metadata
        if deck_uri is not None:
            self.deck_uri = deck_uri
        if dynamic_job_spec_uri is not None:
            self.dynamic_job_spec_uri = dynamic_job_spec_uri

    @property
    def output_uri(self):
        """Gets the output_uri of this AdminNodeExecutionClosure.  # noqa: E501

        Links to a remotely stored, serialized core.LiteralMap of node execution outputs. DEPRECATED. Use GetNodeExecutionData to fetch output data instead.  # noqa: E501

        :return: The output_uri of this AdminNodeExecutionClosure.  # noqa: E501
        :rtype: str
        """
        return self._output_uri

    @output_uri.setter
    def output_uri(self, output_uri):
        """Sets the output_uri of this AdminNodeExecutionClosure.

        Links to a remotely stored, serialized core.LiteralMap of node execution outputs. DEPRECATED. Use GetNodeExecutionData to fetch output data instead.  # noqa: E501

        :param output_uri: The output_uri of this AdminNodeExecutionClosure.  # noqa: E501
        :type: str
        """

        self._output_uri = output_uri

    @property
    def error(self):
        """Gets the error of this AdminNodeExecutionClosure.  # noqa: E501


        :return: The error of this AdminNodeExecutionClosure.  # noqa: E501
        :rtype: CoreExecutionError
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this AdminNodeExecutionClosure.


        :param error: The error of this AdminNodeExecutionClosure.  # noqa: E501
        :type: CoreExecutionError
        """

        self._error = error

    @property
    def output_data(self):
        """Gets the output_data of this AdminNodeExecutionClosure.  # noqa: E501

        Raw output data produced by this node execution. DEPRECATED. Use GetNodeExecutionData to fetch output data instead.  # noqa: E501

        :return: The output_data of this AdminNodeExecutionClosure.  # noqa: E501
        :rtype: CoreLiteralMap
        """
        return self._output_data

    @output_data.setter
    def output_data(self, output_data):
        """Sets the output_data of this AdminNodeExecutionClosure.

        Raw output data produced by this node execution. DEPRECATED. Use GetNodeExecutionData to fetch output data instead.  # noqa: E501

        :param output_data: The output_data of this AdminNodeExecutionClosure.  # noqa: E501
        :type: CoreLiteralMap
        """

        self._output_data = output_data

    @property
    def full_outputs(self):
        """Gets the full_outputs of this AdminNodeExecutionClosure.  # noqa: E501

        Raw output data produced by this node execution.  # noqa: E501

        :return: The full_outputs of this AdminNodeExecutionClosure.  # noqa: E501
        :rtype: CoreOutputData
        """
        return self._full_outputs

    @full_outputs.setter
    def full_outputs(self, full_outputs):
        """Sets the full_outputs of this AdminNodeExecutionClosure.

        Raw output data produced by this node execution.  # noqa: E501

        :param full_outputs: The full_outputs of this AdminNodeExecutionClosure.  # noqa: E501
        :type: CoreOutputData
        """

        self._full_outputs = full_outputs

    @property
    def phase(self):
        """Gets the phase of this AdminNodeExecutionClosure.  # noqa: E501

        The last recorded phase for this node execution.  # noqa: E501

        :return: The phase of this AdminNodeExecutionClosure.  # noqa: E501
        :rtype: CoreNodeExecutionPhase
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this AdminNodeExecutionClosure.

        The last recorded phase for this node execution.  # noqa: E501

        :param phase: The phase of this AdminNodeExecutionClosure.  # noqa: E501
        :type: CoreNodeExecutionPhase
        """

        self._phase = phase

    @property
    def started_at(self):
        """Gets the started_at of this AdminNodeExecutionClosure.  # noqa: E501

        Time at which the node execution began running.  # noqa: E501

        :return: The started_at of this AdminNodeExecutionClosure.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this AdminNodeExecutionClosure.

        Time at which the node execution began running.  # noqa: E501

        :param started_at: The started_at of this AdminNodeExecutionClosure.  # noqa: E501
        :type: datetime
        """

        self._started_at = started_at

    @property
    def duration(self):
        """Gets the duration of this AdminNodeExecutionClosure.  # noqa: E501

        The amount of time the node execution spent running.  # noqa: E501

        :return: The duration of this AdminNodeExecutionClosure.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this AdminNodeExecutionClosure.

        The amount of time the node execution spent running.  # noqa: E501

        :param duration: The duration of this AdminNodeExecutionClosure.  # noqa: E501
        :type: str
        """

        self._duration = duration

    @property
    def created_at(self):
        """Gets the created_at of this AdminNodeExecutionClosure.  # noqa: E501

        Time at which the node execution was created.  # noqa: E501

        :return: The created_at of this AdminNodeExecutionClosure.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AdminNodeExecutionClosure.

        Time at which the node execution was created.  # noqa: E501

        :param created_at: The created_at of this AdminNodeExecutionClosure.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this AdminNodeExecutionClosure.  # noqa: E501

        Time at which the node execution was last updated.  # noqa: E501

        :return: The updated_at of this AdminNodeExecutionClosure.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AdminNodeExecutionClosure.

        Time at which the node execution was last updated.  # noqa: E501

        :param updated_at: The updated_at of this AdminNodeExecutionClosure.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def workflow_node_metadata(self):
        """Gets the workflow_node_metadata of this AdminNodeExecutionClosure.  # noqa: E501


        :return: The workflow_node_metadata of this AdminNodeExecutionClosure.  # noqa: E501
        :rtype: FlyteidladminWorkflowNodeMetadata
        """
        return self._workflow_node_metadata

    @workflow_node_metadata.setter
    def workflow_node_metadata(self, workflow_node_metadata):
        """Sets the workflow_node_metadata of this AdminNodeExecutionClosure.


        :param workflow_node_metadata: The workflow_node_metadata of this AdminNodeExecutionClosure.  # noqa: E501
        :type: FlyteidladminWorkflowNodeMetadata
        """

        self._workflow_node_metadata = workflow_node_metadata

    @property
    def task_node_metadata(self):
        """Gets the task_node_metadata of this AdminNodeExecutionClosure.  # noqa: E501


        :return: The task_node_metadata of this AdminNodeExecutionClosure.  # noqa: E501
        :rtype: FlyteidladminTaskNodeMetadata
        """
        return self._task_node_metadata

    @task_node_metadata.setter
    def task_node_metadata(self, task_node_metadata):
        """Sets the task_node_metadata of this AdminNodeExecutionClosure.


        :param task_node_metadata: The task_node_metadata of this AdminNodeExecutionClosure.  # noqa: E501
        :type: FlyteidladminTaskNodeMetadata
        """

        self._task_node_metadata = task_node_metadata

    @property
    def deck_uri(self):
        """Gets the deck_uri of this AdminNodeExecutionClosure.  # noqa: E501


        :return: The deck_uri of this AdminNodeExecutionClosure.  # noqa: E501
        :rtype: str
        """
        return self._deck_uri

    @deck_uri.setter
    def deck_uri(self, deck_uri):
        """Sets the deck_uri of this AdminNodeExecutionClosure.


        :param deck_uri: The deck_uri of this AdminNodeExecutionClosure.  # noqa: E501
        :type: str
        """

        self._deck_uri = deck_uri

    @property
    def dynamic_job_spec_uri(self):
        """Gets the dynamic_job_spec_uri of this AdminNodeExecutionClosure.  # noqa: E501

        dynamic_job_spec_uri is the location of the DynamicJobSpec proto message for a DynamicWorkflow. This is required to correctly recover partially completed executions where the subworkflow has already been compiled.  # noqa: E501

        :return: The dynamic_job_spec_uri of this AdminNodeExecutionClosure.  # noqa: E501
        :rtype: str
        """
        return self._dynamic_job_spec_uri

    @dynamic_job_spec_uri.setter
    def dynamic_job_spec_uri(self, dynamic_job_spec_uri):
        """Sets the dynamic_job_spec_uri of this AdminNodeExecutionClosure.

        dynamic_job_spec_uri is the location of the DynamicJobSpec proto message for a DynamicWorkflow. This is required to correctly recover partially completed executions where the subworkflow has already been compiled.  # noqa: E501

        :param dynamic_job_spec_uri: The dynamic_job_spec_uri of this AdminNodeExecutionClosure.  # noqa: E501
        :type: str
        """

        self._dynamic_job_spec_uri = dynamic_job_spec_uri

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AdminNodeExecutionClosure, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AdminNodeExecutionClosure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
