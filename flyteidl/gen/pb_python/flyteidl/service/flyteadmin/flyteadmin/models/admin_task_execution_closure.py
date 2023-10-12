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

from flyteadmin.models.admin_reason import AdminReason  # noqa: F401,E501
from flyteadmin.models.core_execution_error import CoreExecutionError  # noqa: F401,E501
from flyteadmin.models.core_literal_map import CoreLiteralMap  # noqa: F401,E501
from flyteadmin.models.core_output_data import CoreOutputData  # noqa: F401,E501
from flyteadmin.models.core_task_execution_phase import CoreTaskExecutionPhase  # noqa: F401,E501
from flyteadmin.models.core_task_log import CoreTaskLog  # noqa: F401,E501
from flyteadmin.models.flyteidlevent_task_execution_metadata import FlyteidleventTaskExecutionMetadata  # noqa: F401,E501
from flyteadmin.models.protobuf_struct import ProtobufStruct  # noqa: F401,E501


class AdminTaskExecutionClosure(object):
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
        'phase': 'CoreTaskExecutionPhase',
        'logs': 'list[CoreTaskLog]',
        'started_at': 'datetime',
        'duration': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'custom_info': 'ProtobufStruct',
        'reason': 'str',
        'task_type': 'str',
        'metadata': 'FlyteidleventTaskExecutionMetadata',
        'event_version': 'int',
        'reasons': 'list[AdminReason]'
    }

    attribute_map = {
        'output_uri': 'output_uri',
        'error': 'error',
        'output_data': 'output_data',
        'full_outputs': 'full_outputs',
        'phase': 'phase',
        'logs': 'logs',
        'started_at': 'started_at',
        'duration': 'duration',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'custom_info': 'custom_info',
        'reason': 'reason',
        'task_type': 'task_type',
        'metadata': 'metadata',
        'event_version': 'event_version',
        'reasons': 'reasons'
    }

    def __init__(self, output_uri=None, error=None, output_data=None, full_outputs=None, phase=None, logs=None, started_at=None, duration=None, created_at=None, updated_at=None, custom_info=None, reason=None, task_type=None, metadata=None, event_version=None, reasons=None):  # noqa: E501
        """AdminTaskExecutionClosure - a model defined in Swagger"""  # noqa: E501

        self._output_uri = None
        self._error = None
        self._output_data = None
        self._full_outputs = None
        self._phase = None
        self._logs = None
        self._started_at = None
        self._duration = None
        self._created_at = None
        self._updated_at = None
        self._custom_info = None
        self._reason = None
        self._task_type = None
        self._metadata = None
        self._event_version = None
        self._reasons = None
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
        if logs is not None:
            self.logs = logs
        if started_at is not None:
            self.started_at = started_at
        if duration is not None:
            self.duration = duration
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if custom_info is not None:
            self.custom_info = custom_info
        if reason is not None:
            self.reason = reason
        if task_type is not None:
            self.task_type = task_type
        if metadata is not None:
            self.metadata = metadata
        if event_version is not None:
            self.event_version = event_version
        if reasons is not None:
            self.reasons = reasons

    @property
    def output_uri(self):
        """Gets the output_uri of this AdminTaskExecutionClosure.  # noqa: E501

        Path to remote data store where output blob is stored if the execution succeeded (and produced outputs). DEPRECATED. Use GetTaskExecutionData to fetch output data instead.  # noqa: E501

        :return: The output_uri of this AdminTaskExecutionClosure.  # noqa: E501
        :rtype: str
        """
        return self._output_uri

    @output_uri.setter
    def output_uri(self, output_uri):
        """Sets the output_uri of this AdminTaskExecutionClosure.

        Path to remote data store where output blob is stored if the execution succeeded (and produced outputs). DEPRECATED. Use GetTaskExecutionData to fetch output data instead.  # noqa: E501

        :param output_uri: The output_uri of this AdminTaskExecutionClosure.  # noqa: E501
        :type: str
        """

        self._output_uri = output_uri

    @property
    def error(self):
        """Gets the error of this AdminTaskExecutionClosure.  # noqa: E501

        Error information for the task execution. Populated if the execution failed.  # noqa: E501

        :return: The error of this AdminTaskExecutionClosure.  # noqa: E501
        :rtype: CoreExecutionError
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this AdminTaskExecutionClosure.

        Error information for the task execution. Populated if the execution failed.  # noqa: E501

        :param error: The error of this AdminTaskExecutionClosure.  # noqa: E501
        :type: CoreExecutionError
        """

        self._error = error

    @property
    def output_data(self):
        """Gets the output_data of this AdminTaskExecutionClosure.  # noqa: E501

        Raw output data produced by this task execution. DEPRECATED. Use GetTaskExecutionData to fetch output data instead.  # noqa: E501

        :return: The output_data of this AdminTaskExecutionClosure.  # noqa: E501
        :rtype: CoreLiteralMap
        """
        return self._output_data

    @output_data.setter
    def output_data(self, output_data):
        """Sets the output_data of this AdminTaskExecutionClosure.

        Raw output data produced by this task execution. DEPRECATED. Use GetTaskExecutionData to fetch output data instead.  # noqa: E501

        :param output_data: The output_data of this AdminTaskExecutionClosure.  # noqa: E501
        :type: CoreLiteralMap
        """

        self._output_data = output_data

    @property
    def full_outputs(self):
        """Gets the full_outputs of this AdminTaskExecutionClosure.  # noqa: E501

        Raw output data produced by this task execution.  # noqa: E501

        :return: The full_outputs of this AdminTaskExecutionClosure.  # noqa: E501
        :rtype: CoreOutputData
        """
        return self._full_outputs

    @full_outputs.setter
    def full_outputs(self, full_outputs):
        """Sets the full_outputs of this AdminTaskExecutionClosure.

        Raw output data produced by this task execution.  # noqa: E501

        :param full_outputs: The full_outputs of this AdminTaskExecutionClosure.  # noqa: E501
        :type: CoreOutputData
        """

        self._full_outputs = full_outputs

    @property
    def phase(self):
        """Gets the phase of this AdminTaskExecutionClosure.  # noqa: E501

        The last recorded phase for this task execution.  # noqa: E501

        :return: The phase of this AdminTaskExecutionClosure.  # noqa: E501
        :rtype: CoreTaskExecutionPhase
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this AdminTaskExecutionClosure.

        The last recorded phase for this task execution.  # noqa: E501

        :param phase: The phase of this AdminTaskExecutionClosure.  # noqa: E501
        :type: CoreTaskExecutionPhase
        """

        self._phase = phase

    @property
    def logs(self):
        """Gets the logs of this AdminTaskExecutionClosure.  # noqa: E501

        Detailed log information output by the task execution.  # noqa: E501

        :return: The logs of this AdminTaskExecutionClosure.  # noqa: E501
        :rtype: list[CoreTaskLog]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Sets the logs of this AdminTaskExecutionClosure.

        Detailed log information output by the task execution.  # noqa: E501

        :param logs: The logs of this AdminTaskExecutionClosure.  # noqa: E501
        :type: list[CoreTaskLog]
        """

        self._logs = logs

    @property
    def started_at(self):
        """Gets the started_at of this AdminTaskExecutionClosure.  # noqa: E501

        Time at which the task execution began running.  # noqa: E501

        :return: The started_at of this AdminTaskExecutionClosure.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this AdminTaskExecutionClosure.

        Time at which the task execution began running.  # noqa: E501

        :param started_at: The started_at of this AdminTaskExecutionClosure.  # noqa: E501
        :type: datetime
        """

        self._started_at = started_at

    @property
    def duration(self):
        """Gets the duration of this AdminTaskExecutionClosure.  # noqa: E501

        The amount of time the task execution spent running.  # noqa: E501

        :return: The duration of this AdminTaskExecutionClosure.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this AdminTaskExecutionClosure.

        The amount of time the task execution spent running.  # noqa: E501

        :param duration: The duration of this AdminTaskExecutionClosure.  # noqa: E501
        :type: str
        """

        self._duration = duration

    @property
    def created_at(self):
        """Gets the created_at of this AdminTaskExecutionClosure.  # noqa: E501

        Time at which the task execution was created.  # noqa: E501

        :return: The created_at of this AdminTaskExecutionClosure.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AdminTaskExecutionClosure.

        Time at which the task execution was created.  # noqa: E501

        :param created_at: The created_at of this AdminTaskExecutionClosure.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this AdminTaskExecutionClosure.  # noqa: E501

        Time at which the task execution was last updated.  # noqa: E501

        :return: The updated_at of this AdminTaskExecutionClosure.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AdminTaskExecutionClosure.

        Time at which the task execution was last updated.  # noqa: E501

        :param updated_at: The updated_at of this AdminTaskExecutionClosure.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def custom_info(self):
        """Gets the custom_info of this AdminTaskExecutionClosure.  # noqa: E501

        Custom data specific to the task plugin.  # noqa: E501

        :return: The custom_info of this AdminTaskExecutionClosure.  # noqa: E501
        :rtype: ProtobufStruct
        """
        return self._custom_info

    @custom_info.setter
    def custom_info(self, custom_info):
        """Sets the custom_info of this AdminTaskExecutionClosure.

        Custom data specific to the task plugin.  # noqa: E501

        :param custom_info: The custom_info of this AdminTaskExecutionClosure.  # noqa: E501
        :type: ProtobufStruct
        """

        self._custom_info = custom_info

    @property
    def reason(self):
        """Gets the reason of this AdminTaskExecutionClosure.  # noqa: E501

        If there is an explanation for the most recent phase transition, the reason will capture it.  # noqa: E501

        :return: The reason of this AdminTaskExecutionClosure.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this AdminTaskExecutionClosure.

        If there is an explanation for the most recent phase transition, the reason will capture it.  # noqa: E501

        :param reason: The reason of this AdminTaskExecutionClosure.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def task_type(self):
        """Gets the task_type of this AdminTaskExecutionClosure.  # noqa: E501

        A predefined yet extensible Task type identifier.  # noqa: E501

        :return: The task_type of this AdminTaskExecutionClosure.  # noqa: E501
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this AdminTaskExecutionClosure.

        A predefined yet extensible Task type identifier.  # noqa: E501

        :param task_type: The task_type of this AdminTaskExecutionClosure.  # noqa: E501
        :type: str
        """

        self._task_type = task_type

    @property
    def metadata(self):
        """Gets the metadata of this AdminTaskExecutionClosure.  # noqa: E501

        Metadata around how a task was executed.  # noqa: E501

        :return: The metadata of this AdminTaskExecutionClosure.  # noqa: E501
        :rtype: FlyteidleventTaskExecutionMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this AdminTaskExecutionClosure.

        Metadata around how a task was executed.  # noqa: E501

        :param metadata: The metadata of this AdminTaskExecutionClosure.  # noqa: E501
        :type: FlyteidleventTaskExecutionMetadata
        """

        self._metadata = metadata

    @property
    def event_version(self):
        """Gets the event_version of this AdminTaskExecutionClosure.  # noqa: E501

        The event version is used to indicate versioned changes in how data is maintained using this proto message. For example, event_verison > 0 means that maps tasks logs use the TaskExecutionMetadata ExternalResourceInfo fields for each subtask rather than the TaskLog in this message.  # noqa: E501

        :return: The event_version of this AdminTaskExecutionClosure.  # noqa: E501
        :rtype: int
        """
        return self._event_version

    @event_version.setter
    def event_version(self, event_version):
        """Sets the event_version of this AdminTaskExecutionClosure.

        The event version is used to indicate versioned changes in how data is maintained using this proto message. For example, event_verison > 0 means that maps tasks logs use the TaskExecutionMetadata ExternalResourceInfo fields for each subtask rather than the TaskLog in this message.  # noqa: E501

        :param event_version: The event_version of this AdminTaskExecutionClosure.  # noqa: E501
        :type: int
        """

        self._event_version = event_version

    @property
    def reasons(self):
        """Gets the reasons of this AdminTaskExecutionClosure.  # noqa: E501

        A time-series of the phase transition or update explanations. This, when compared to storing a singular reason as previously done, is much more valuable in visualizing and understanding historical evaluations.  # noqa: E501

        :return: The reasons of this AdminTaskExecutionClosure.  # noqa: E501
        :rtype: list[AdminReason]
        """
        return self._reasons

    @reasons.setter
    def reasons(self, reasons):
        """Sets the reasons of this AdminTaskExecutionClosure.

        A time-series of the phase transition or update explanations. This, when compared to storing a singular reason as previously done, is much more valuable in visualizing and understanding historical evaluations.  # noqa: E501

        :param reasons: The reasons of this AdminTaskExecutionClosure.  # noqa: E501
        :type: list[AdminReason]
        """

        self._reasons = reasons

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
        if issubclass(AdminTaskExecutionClosure, dict):
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
        if not isinstance(other, AdminTaskExecutionClosure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
