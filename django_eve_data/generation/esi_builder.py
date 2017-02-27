"""
Basicly we will create a static dump into a folder for easy access of ESI Api
Also on Changes we will be able with static code analysis to indicate problems in our Api.
"""
import os

import re
import requests
from jinja2 import Environment
from urllib.parse import urlsplit

from jinja2 import FileSystemLoader


def get_optional_parameter(value):
    return list(filter(lambda x: 'default' in x.keys() or 'minimum' in x.keys(), value))


def get_required_param(value):
    optional_param = get_optional_parameter(value)
    required_list = list(filter(lambda x: x.get('required', False) and x not in optional_param, value))
    return required_list


def get_kwargs(value):
    required = get_required_param(value)
    optional = get_optional_parameter(value)
    required.extend(optional)
    all_kwargs = list(filter(lambda x: x not in required, value))
    return [all_kwarg.get('name', 'notnamed') for all_kwarg in all_kwargs]


def get_param_default_template(value):
    param_type = value.get('type', 'string')
    default = value.get('default', value.get('minimum', ''))

    if param_type == "integer":
        return default
    else:
        return '"'+str(default)+'"'


def convert_string_to_python_variable(value):
    return re.sub("-| % | & ", "_", value).lower()


def convert_python_type(value):
    if value == "integer":
        return "int"
    elif value == "string":
        return "str"
    elif value == "array":
        return "list"
    return value



class SwaggerAPIBuilder(object):
    def __init__(self, swagger_url):
        response = requests.get(swagger_url)
        if not response.ok:
            raise EnvironmentError('Swagger_url is not properly working: ' + swagger_url)
        swagger_dict = response.json()
        dict_of_parts = dict()
        current_dir = os.path.dirname(os.path.abspath(__file__))

        base_url, _, _ = swagger_url.rpartition("/")
        # TODO info in files schreiben
        for url, options in swagger_dict.get('paths', {}).items():
            filename = url.split("/")[1]
            options['path'] = url
            old_list = dict_of_parts.get(filename, [])
            old_list.append(("".join((base_url, url)), options))
            dict_of_parts[filename] = old_list

        jinja_enviroment = Environment(loader=FileSystemLoader(os.path.join(current_dir, "template")),
                                       lstrip_blocks=True)
        jinja_enviroment.filters["convertPythonType"] = convert_python_type
        jinja_enviroment.filters["convertPythonParam"] = convert_string_to_python_variable
        jinja_enviroment.filters["getRequiredParams"] = get_required_param
        jinja_enviroment.filters["getOptionalParams"] = get_optional_parameter
        jinja_enviroment.filters["getParamDefaultTemplate"] = get_param_default_template
        jinja_enviroment.filters["getKwargs"] = get_kwargs

        template_start = jinja_enviroment.get_template('esi_file_start.html')
        template_class = jinja_enviroment.get_template('esi_base_template.html')

        current_path = os.path.join(os.path.dirname(current_dir), "esi_api")
        if not os.path.exists(current_path):
            os.makedirs(current_path)

        for filename, value in dict_of_parts.items():

            with open(os.path.join(current_path, filename + ".py"), 'w+') as new_file:
                new_file.write(template_start.render())
                for classurl, classdict in value:
                    options = classdict
                    splited_path_url = urlsplit(classdict.get('path', 'NoPathError')).path.split("/")
                    splited_name = list(
                        map(lambda s: "Detail" if s.startswith("{") else s.capitalize(), splited_path_url))
                    options['name'] = "".join(splited_name)
                    options['base_url'] = classurl
                    new_file.write(template_class.render(**options))


if __name__ == '__main__':
    SwaggerAPIBuilder("https://esi.tech.ccp.is/latest/swagger.json")
