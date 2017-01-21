from rdflib.namespace import RDF, NamespaceManager

class RDFWalker:
    """
    Simple RDF graph walker
    """

    def __init__ (self, g, s, n, path=[]):
        """
        :param g: Graph
        :param s: Namespace
        :param n: Start node
        """
        self.g = g
        self.n = n
        self.s = s
        self._path = path

    def __getattr__ (self, k):
        """
        If k is underscore _, walk up tree one level, otherwise search for
        direct descendents and get first one.
        """
        if k == '_':
            return RDFWalker (self.g, self.s, self._path[0], self._path[1:])
        yieldall = False
        if k.endswith ('_'):
            yieldall = True
            k = k[:-1]

        if k == 'a':
            attr = RDF.type
        else:
            attr = getattr (self.s, k)

        ret = [RDFWalker (self.g, self.s, n, [self.n] + self._path) for n in self.g.objects (self.n, attr)]

        if yieldall:
            return ret
        elif not ret:
            return None
        else:
            return ret[0]

    def __eq__ (self, b):
        return self.n == b.n

    def __lt__ (self, b):
        return str (self) < str (b)

    def __str__ (self):
        return str (self.n)


