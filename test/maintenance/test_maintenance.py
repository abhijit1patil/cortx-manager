#!/usr/bin/env python3

"""
 ****************************************************************************
 Filename:          test_timelion_provider.py
 Description:       Test timelion provider for csm.

 Creation Date:     07/08/2019
 Author:            Ajay Paratmandali

 Do NOT modify or remove this copyright and confidentiality notice!
 Copyright (c) 2001 - $Date: 2015/01/14 $ Seagate Technology, LLC.
 The code contained herein is CONFIDENTIAL to Seagate Technology, LLC.
 Portions are also trade secret. Any use, duplication, derivation, distribution
 or disclosure of this code, for any reason, not expressly authorized is
 prohibited. All other rights are expressly reserved by Seagate Technology, LLC.
 ****************************************************************************
"""

import sys
import os
import asyncio

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from csm.test.common import TestFailed
from eos.utils.log import Log
from core.services.maintenance import MaintenanceAppService
from csm.common.ha_framework import PcsHAFramework

class TestMaintenanceAppService:
    def __init__(self):
        pass

    @staticmethod
    def init():
        _maintenance = MaintenanceAppService(PcsHAFramework())
        _loop = asyncio.get_event_loop()
        return _maintenance, _loop

def init(args):
    pass

#################
# Tests
#################
def nodes_status(args):
    """
    Use timelion provider to initalize csm
    """
    _maintenance, _loop = TestMaintenanceAppService.init()
    Log.console('Testing node status ...')
    try:
        status = _loop.run_until_complete(_maintenance.get_status(node=None))
        if status.get("node_status"):
            Log.console(status)
        else:
            raise TestFailed("Node status test failed")
    except Exception as e:
        raise TestFailed(f"Node status test failed: {e}")

def stop(args):
    """
    Stop all nodes from cluster
    """
    Log.console('Testing node stop ...')
    _maintenance, _loop = TestMaintenanceAppService.init()
    try:
        status = _loop.run_until_complete(_maintenance.stop("srvnode-1"))
        if status.get("message", None):
            Log.console(status)
        else:
            raise TestFailed("stop test failed")
    except Exception as e:
        raise TestFailed(f"stop test failed: {e}")

def start(args):
    """
    Start all nodes from cluster
    """
    Log.console('Testing node start ...')
    _maintenance, _loop = TestMaintenanceAppService.init()
    try:
        status = _loop.run_until_complete(_maintenance.start("srvnode-1"))
        if status.get("message", None):
            Log.console(status)
        else:
            raise TestFailed("start test failed")
    except Exception as e:
        raise TestFailed(f"start test failed: {e}")

def shutdown(args):
    """
    Start all nodes from cluster
    """
    Log.console('Testing node shutdown ...')
    _maintenance, _loop = TestMaintenanceAppService.init()
    try:
        status = _loop.run_until_complete(_maintenance.shutdown("srvnode-1"))
        if status.get("message", None):
            Log.console(status)
        else:
            raise TestFailed("shutdown test failed")
    except Exception as e:
        raise TestFailed(f"shutdown test failed: {e}")

test_list = [ nodes_status, stop, start, shutdown ]
