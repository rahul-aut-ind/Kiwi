# -*- coding: utf-8 -*-

from modernrpc.core import rpc_method

from tcms.testcases.models import Category
from tcms.rpc.decorators import permissions_required


@permissions_required('testcases.view_category')
@rpc_method(name='Category.filter')
def filter(query):  # pylint: disable=redefined-builtin
    """
    .. function:: RPC Category.filter(query)

        Search and return Category objects matching query.

        :param query: Field lookups for :class:`tcms.testcases.models.Category`
        :type query: dict
        :return: List of serialized :class:`tcms.testcases.models.Category` objects
        :rtype: list(dict)
    """
    return Category.to_xmlrpc(query)
