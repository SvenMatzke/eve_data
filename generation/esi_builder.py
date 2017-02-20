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

# TODO only params with default or required should be listet
# further i need to order those

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
