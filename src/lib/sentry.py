import logging
import sentry_sdk
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration

import src.lib.config as _config
from src.lib.generate_id import generate_id as _generate_id


def init(run_id=None):
    '''
    1. Init sentry exception tracking
    2. Improve default log formatting
    3. Silence noise logger(s)

    :param run_id: Parameter can be provided as reference to find all logs
    that belong to a single run of a serverless function
    '''
    sentry_config = _config.get_config().get('sentry')
    if not sentry_config:
        return

    sentry_key = sentry_config['key']
    sentry_project = sentry_config['project']

    if not run_id:
        run_id = _generate_id()

    log_format = '%(levelname)s:\n%(name)s:{}: %(message)s'.format(run_id)
    if _config.get_env() in ['staging', 'production']:
        log_format = log_format.replace('\n', '\r')
    logging.basicConfig(level=logging.INFO, format=log_format)

    # silence botocore logs
    logging.getLogger('botocore').setLevel(logging.WARNING)


    if _config.get_env() in ['staging', 'production']:
        log_format = log_format.replace('\n', '\r')
    logging.basicConfig(level=logging.INFO, format=log_format)

    sentry_sdk.init(
        dsn="https://{key}@sentry.io/{project}".format(key=sentry_key, project=sentry_project),
        integrations=[AwsLambdaIntegration()]
    )
