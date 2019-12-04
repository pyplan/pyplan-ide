

class BaseDynamic(object):


    @staticmethod
    def clearAllCircularDependency(stringDef):
        """ Replaces cp.dynamic(x,y,z) , pp.dynamic(x,y,z) and dynamic(x,y,z) for 0
        """
        response = stringDef
        initialIndex = -1
        startIndex = -1
        finalIndex = -1
        toReplace = ''
        dynLen = len('cp.dynamic(')
        initialIndex = stringDef.find('cp.dynamic(')
        if initialIndex == -1:
            initialIndex = stringDef.find('pp.dynamic(')
        if initialIndex == -1:
            initialIndex = stringDef.find('dynamic(')            
            dynLen = len('dynamic(')
        if initialIndex != -1:
            startIndex = initialIndex
            initialIndex = initialIndex + dynLen
            if len(stringDef) > initialIndex:
                finalIndex = stringDef[initialIndex+1:].find(')')

        if initialIndex != -1 and finalIndex != -1:
            toReplace = stringDef[startIndex:initialIndex + finalIndex + 2]
            response = stringDef.replace(toReplace, "0")

        return response


# implementations

    def circularEval(self, node, params): raise ValueError("not implemented")

    def generateLoopDef(self, node, nodeDefinition,
                        cyclicVariables): raise ValueError("not implemented")

    def generateInitDef(self, node, nodeResult,
                        dynamicIndex): raise ValueError("not implemented")

    def generateCircularParameters(
        self, node, nodeList): raise ValueError("not implemented")

    def clearCircularDependency(
        self, stringDef, replaceWith="0"): raise ValueError("not implemented")
