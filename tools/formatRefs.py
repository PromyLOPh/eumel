#!/usr/bin/env python3

from rdflib import URIRef, BNode, Literal, Graph, Namespace
from rdflib.namespace import RDF, NamespaceManager
from urllib.parse import urlparse
import sys
from itertools import chain

def first (it):
    try:
        return next (it)
    except StopIteration:
        return None

def humanList (l):
    if len (l) == 0:
        return ''
    elif len (l) == 1:
        return l[0]
    else:
        return ', '.join (l[:-1]) + ' and ' + l[-1]

def formatDomain (url):
    d = urlparse (url).hostname
    if d.startswith ('www.'):
        d = d[4:]
    return d

def formatPerson (s, g, n):
    firstname = first (g.objects (n, s.givenName))
    familyname = first (g.objects (n, s.familyName))
    if firstname:
        return '{} {}'.format (firstname, familyname)
    else:
        return familyname

def formatParent (s, g, n, useName = True):
    ret = []

    if useName:
        parentname = first (g.objects (n, s.name))
        if parentname:
            ret.append (parentname)

    volume = first (g.objects (n, s.volumeNumber))
    if volume:
        ret.append ('volume {}'.format (volume))

    issue = first (g.objects (n, s.issueNumber))
    if issue:
        ret.append ('issue {}'.format (issue))

    # pages
    start = first (g.objects (n, s.pageStart))
    end = first (g.objects (n, s.pageEnd))
    if start:
        try:
            num = int (end)-int (start)
        except (ValueError, TypeError):
            num = 1
        if end and num >= 1:
            ret.append ('pp. {}–{}'.format (start, end))
        else:
            ret.append ('p. {}'.format (start))

    return ', '.join (ret)

def relUri (base, u):
    if u.startswith (base):
        return u[len (base):]
    else:
        return u

def hideLocalUri (base, l):
    """
    Show local uris only iff no other sources are available
    """
    l = list (l)
    notLocal = list (filter (lambda u: relUri (base, u) == u, l))
    return notLocal or l

def getRecursive (s, g, n, predicate):
    """
    Look for predicate in n and all Things it is a part of until it is found
    """
    res = g.objects (n, predicate)
    if res:
        yield from res
    parents = g.objects (n, s.isPartOf)
    for p in parents:
        yield from getRecursive (s, g, p, predicate)

def getRecursiveAll (s, g, n, predicate):
    parents = list (g.objects (n, predicate))
    yield from parents
    for p in parents:
        yield from getRecursiveAll (s, g, p, predicate)

def warnUnusedButDefined (graph, rootNode):
    """
    Warn about defined, but unused subjects
    """

    subjects = set ()
    objects = set ()
    for s, p, o in graph:
        subjects.add (s)
        objects.add (o)
    for unused in subjects.difference (objects):
        if unused == rootNode:
            continue
        print ('Unused: {}'.format (unused), file=sys.stderr)
        for ctxp, ctxo in g[unused]:
            print ('\t{} {}'.format (ctxp, ctxo), file=sys.stderr)

if __name__ == '__main__':
    g = Graph()
    result = g.parse ("index.ttl", format='turtle')
    rootUri = sys.argv[1]
    rootNode = URIRef (rootUri)
    s = Namespace("https://schema.org/")

    warnUnusedButDefined (result, rootNode)

    for ref in result.objects (rootNode, s.citation):
        t = list (g.objects (ref, RDF.type))
        assert len (t) == 1
        t = t[0]

        # object _must_ have a name
        what = first (g.objects (ref, s.name))

        # look for people who wrote/translated/edited it
        who = map (lambda a: formatPerson (s, g, a), getRecursive (s, g, ref, s.author))
        #who = chain (who, map (lambda a: formatPerson (s, g, a) + ' (ed.)', getRecursive (s, g, ref, s.editor)))
        #who = chain (who, map (lambda a: formatPerson (s, g, a) + ' (trans.)', getRecursive (s, g, ref, s.translator)))
        who = humanList (list (who))

        # when was it published?
        when = first (getRecursive (s, g, ref, s.datePublished))

        # where can we find it? (print)
        # print from root to ref (i.e. magazine, volume, issue)
        parents = reversed (list (getRecursiveAll (s, g, ref, s.isPartOf)))
        where = list (filter (lambda x: x, [formatParent (s, g, p) for p in parents]))
        thiswhere = formatParent (s, g, ref, False)
        if thiswhere:
            where.append (thiswhere)

        # where can we find it? (online)
        urls = hideLocalUri (rootUri, g.objects (ref, s.url))
        urls = ['`{} <{}>`__'.format (formatDomain (url), relUri (rootUri, url)) for url in urls]

        refname = urlparse (ref).fragment
        if not refname:
            refname = first (g.objects (ref, s.alternateName))
        ret = '.. [{}] \\ '.format (refname)

        if who:
            ret += ' {}:'.format (who)

        ret += ' *{}*.'.format (what)

        if where:
            ret += ' {}.'.format (', '.join (where))

        if when:
            ret += ' {}.'.format (when)

        if urls:
            ret += ' {}.'.format (', '.join (urls))
        print (ret)

