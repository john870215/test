import importlib
import os

# according to .env file APP_SETTINGS_MODULE loading which config file
app_settings = os.getenv("APP_SETTINGS_MODULE", "app.config.dev")
# app_settings = "app.config.dev"


class RuntimeSettings:
    def __init__(self, settings_module):
        self.SETTINGS_MODULE = settings_module
        self._module = None

    def __repr__(self) -> str:
        if not self._module:
            return "<RuntimeSettings [Unevaluated]>"

        return '<RuntimeSettings "%(settings_module)s">' % {
            "settings_module": self.SETTINGS_MODULE,
        }

    def _import_settings(self):
        if not self._module:
            try:
                settings = importlib.import_module(self.SETTINGS_MODULE)

            except AttributeError as err:
                raise ImportError(
                    'Module "%s" does not define, check .env or global environment has "APP_SETTINGS_MODULE" module python script'
                    % (self.SETTINGS_MODULE)
                ) from err

            self._module = settings

    def __getattr__(self, name):
        if not self._module:
            self._import_settings()

        return getattr(self._module, name)


settings = RuntimeSettings(app_settings)
# logger = settings.logger
