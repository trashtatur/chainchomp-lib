import re
from typing import List

from chainchomplib.configlayer import helperFunctions
from chainchomplib.abstracts.AbstractResolver import AbstractResolver


class FunctionResolver(AbstractResolver):

    @staticmethod
    def __parse_config_template_strings(function_name: str, arguments: List[str] or None) -> str:
        if callable(getattr(helperFunctions, function_name)):
            function_to_execute = getattr(helperFunctions, function_name)
            if arguments is not None:
                return function_to_execute(','.join(arguments))
            return function_to_execute()
        return function_name

    @staticmethod
    def parse(string):
        potential_templates = re.split('({{.+?}})', string)
        potential_template_string = string
        for potential_template in potential_templates:
            if potential_template.startswith('{{') and potential_template.endswith('}}'):
                # Regex unit tests can be found here: https://regex101.com/r/xlWU9G/2
                content = re.match('{{([^()]+)(\((.+)\))?}}', potential_template)
                args = content.group(3).split(',') if content.group(3) is not None else None
                resolved_template = FunctionResolver.__parse_config_template_strings(content.group(1), args)
                potential_template_string = potential_template_string.replace(potential_template, resolved_template)
        return potential_template_string
