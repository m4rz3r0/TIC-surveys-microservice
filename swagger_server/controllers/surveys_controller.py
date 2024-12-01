import connexion
import six

from swagger_server.models.survey_detail import SurveyDetail  # noqa: E501
from swagger_server.models.survey_list import SurveyList  # noqa: E501
from swagger_server import util


def surveys_get():  # noqa: E501
    """Obtener encuestas disponibles

    Lista todas las encuestas que están publicadas y disponibles para responder. # noqa: E501


    :rtype: SurveyList
    """
    return 'do some magic!'


def surveys_id_get(id):  # noqa: E501
    """Obtener detalles de una encuesta

    Devuelve la información de una encuesta específica, incluidas sus preguntas. # noqa: E501

    :param id: ID de la encuesta
    :type id: int

    :rtype: SurveyDetail
    """
    return 'do some magic!'
