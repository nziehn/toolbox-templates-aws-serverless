import os as _os
from toolbox import config as _config


get_env = _config.get_env  # publishing get_env fn


def get_config(env=None):
   config_path = _os.path.join(_os.path.dirname(__file__), '..', '..', 'config')
   config = _config.Config(path=config_path, env=env)
   return config


if __name__ == '__main__':
    print(get_config().get(['hello']))