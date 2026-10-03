import argparse
import json
import datetime as dt
from pathlib import Path
from functions import *

timedateformat = '%a, %b, %Y, %H:%M:%S %p'

def test_create_task():
    """Test create a new task"""

    test_path = Path('test.json')
    test_path.write_text('[]')
    test_args = argparse.Namespace(add='test')

    create_task(args=test_args,path=test_path)

    data = json.loads(test_path.read_text())
    assert data[0]['status'] == 'Todo'

def test_update_task():
    """Test updating an existing task."""

    test_path = Path('test.json')
    test_path.write_text('[]')

    test_args = argparse.Namespace(update='test')
    create_arg = argparse.Namespace(add='test')

    create_task(args=create_arg,path=test_path)
    update_task(args=test_args,path=test_path)

    data = json.loads(test_path.read_text())
    tday = dt.datetime.today().strftime(timedateformat).format()
    
    data[0].update({'updatedAt': tday})

    assert data[0]['updatedAt'] == tday