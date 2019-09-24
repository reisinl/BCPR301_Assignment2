import re


class Parser:
    def __init__(self, drawer):
        self.drawer = drawer
        self.source = []
        self.command = ""
        self.data = 0
        lines = [line for line in open("lookUpTable.txt")]
        self.commands = {}
        command_pattern = re.compile("^([A-Z])\s+(.*)$")
        for line in lines:
            match = re.match(command_pattern, line)
            if match is not None:
                self.commands[match.group(1)] = match.group(2)

    def parse(self, lines):
        for line in lines:
            self.parseLine(line)

    def parseLine(self, line):
        command_pattern = re.compile("^([A-Z])\s*(.*)$", re.IGNORECASE)
        match = re.match(command_pattern, line)
        if match is not None:
            command = match.group(1)
            value = self.commands[command.upper()]
            parameter_pattern = re.compile("<([0-9]+)>")
            parameters = re.findall(parameter_pattern, value)
            parameters = [int(parameter) for parameter in parameters]
            replace_count = 0
            num_parameters = 0
            if parameters:
                num_parameters = max(parameters)
                parameter_expression = "\s+([0-9]+)" * num_parameters
                parameter_pattern = re.compile(
                    "^[A-Z]" + parameter_expression, re.IGNORECASE
                )
                match = re.match(parameter_pattern, line)
                if match is not None:
                    parameters = match.groups()
                    parameter_pattern = re.compile("<([0-9]+)>")
                    match = re.search(parameter_pattern, value)
                    while match is not None:
                        replace_count = replace_count + 1
                        parameter_number = int(match.group(1))
                        start_val = value[:match.start()]
                        parameter_val = parameters[parameter_number - 1]
                        end_val = value[match.end():]
                        value = start_val + parameter_val + end_val
                        match = re.search(parameter_pattern, value)
            if num_parameters == replace_count:
                exec(value)
            else:
                print("Parameter count mismatch!")
