import re
class Parser:
    def __init__(self, drawer):
        self.drawer = drawer
        self.source = []
        self.command = ""
        self.data = 0
        lines = [line for line in open("lookUpTable.txt")]
        self.commands = {}
        commandPattern = re.compile("^([A-Z])\s+(.*)$")
        for line in lines:
            match = re.match(commandPattern, line)
            if match is not None:
                self.commands[match.group(1)] = match.group(2)

    def parse(self, lines):
        for line in lines:
            self.parseLine(line)
    
    def parseLine(self, line):
        commandPattern = re.compile("^([A-Z])\s*(.*)$", re.IGNORECASE)
        match = re.match(commandPattern, line)
        if match is not None:
            command = match.group(1)
            value = self.commands[command.upper()]
            parameterPattern = re.compile("<([0-9]+)>")
            parameters = re.findall(parameterPattern, value)
            parameters = [int(parameter) for parameter in parameters]
            replaceCount = 0
            numParameters = 0
            if parameters:
                numParameters = max(parameters)
                parameterExpression = "\s+([0-9]+)" * numParameters
                parameterPattern = re.compile("^[A-Z]"+parameterExpression, re.IGNORECASE)
                match = re.match(parameterPattern, line)
                if match is not None:
                    parameters = match.groups()
                    parameterPattern = re.compile("<([0-9]+)>")
                    match = re.search(parameterPattern, value)
                    while match is not None:
                        replaceCount = replaceCount + 1
                        parameterNumber=int(match.group(1))
                        value=value[:match.start()] + parameters[parameterNumber-1] + value[match.end():]
                        match = re.search(parameterPattern, value)
            if numParameters == replaceCount:
                exec(value)
            else:
                print("Parameter count mismatch!")
