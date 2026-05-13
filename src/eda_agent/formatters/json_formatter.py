import json

class JSONFormatter:
    @staticmethod
    def format(output):
        return json.dumps(output, indent=2)

