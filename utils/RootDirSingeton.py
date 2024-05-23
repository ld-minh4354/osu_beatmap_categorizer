import os


class RootDirSingleton:
    class __define_root_dir:
        def __init__(self):
            self.path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

    # global instance in class
    instance = None

    def __init__(self):
        if not RootDirSingleton.instance:
            RootDirSingleton.instance = RootDirSingleton.__define_root_dir()
        return  # does nothing if already constructed

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def get_root_dir(self):
        return self.instance.path

ROOT_DIR = RootDirSingleton().get_root_dir()

print(ROOT_DIR)