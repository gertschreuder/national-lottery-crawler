class Serialize(object):
    @staticmethod
    def jsonDumps(data):
        if data is None:
            return data
        if hasattr(data, "__dict__"):
            data = data.__dict__
        item = {}
        for k, v in data.items():
            if isinstance(v, list):
                lys = []
                [lys.append(Serialize.jsonDumps(i)) for i in v]
                item[k] = lys
            else:
                item[k] = v

        return item
