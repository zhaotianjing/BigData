class Reducer:
    def reduce(self, d):
        returnval = []
        for k, v in d.items():
            returnval.append("%s\t%s"%(k, sum(v)))
        return returnval
