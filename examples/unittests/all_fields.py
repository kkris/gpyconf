from gpyconf import fields
from gpyconftest import Configuration
import gpyconf.frontends.gtk

MULTI_OPTION_FIELD_OPTIONS = (
    ('foo', 'Select me for foo'),
    ('bar', 'Select me for bar'),
    (42, 'Select me for the answer to Life, the Universe, and Everything')
)

def _all(module):
    from types import ModuleType
    for attr in dir(module):
        if attr == 'Field':
            continue
        if attr.startswith('_'):
            continue
        attr = getattr(module, attr)
        if isinstance(attr, ModuleType):
            # exclude modules:
            continue
        yield attr

def call(callable):
    if issubclass(callable, fields.MultiOptionField):
        # expects parameter, extra handling
        ins = callable(callable._class_name, options=(MULTI_OPTION_FIELD_OPTIONS))
    else:
        ins = callable()
    ins.label = ins._class_name
    return ins

_fields = [field for field in _all(fields) if issubclass(field, fields.Field) and not field.abstract]
_dict = dict((field._class_name.lower(), field) for field in map(call, _fields))
_dict['logging_level'] = 'info'
_dict['frontend'] = gpyconf.frontends.gtk.ConfigurationDialog.with_arguments(title='All Fields',
                                                                                 ignore_missing_widgets=True)

AllFieldsTest = type('AllFieldsTest', (Configuration,), _dict)
# generate the class

if __name__ == '__main__':
    #from gpyconf.backends.python import PythonModuleBackend as BACKEND
    #from gpyconf.backends._json import JSONBackend as BACKEND
    from gpyconf.backends._xml import XMLBackend as BACKEND
    #from gpyconf.backends.configparser import ConfigParserBackend as BACKEND

    test = AllFieldsTest(backend=BACKEND)
    test.get_frontend().dialog.set_size_request(800, 600)
    test.run_frontend()
