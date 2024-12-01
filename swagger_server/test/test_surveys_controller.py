# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.survey_detail import SurveyDetail  # noqa: E501
from swagger_server.models.survey_list import SurveyList  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSurveysController(BaseTestCase):
    """SurveysController integration test stubs"""

    def test_surveys_get(self):
        """Test case for surveys_get

        Obtener encuestas disponibles
        """
        response = self.client.open(
            '/surveys',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_surveys_id_get(self):
        """Test case for surveys_id_get

        Obtener detalles de una encuesta
        """
        response = self.client.open(
            '/surveys/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
