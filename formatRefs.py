#!/usr/bin/env python3

from rdflib import URIRef, BNode, Literal, Graph, Namespace
from rdflib.namespace import RDF, NamespaceManager
from urllib.parse import urlparse
import sys

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

def formatParent (s, g, n):
    parent = first (g.objects (n, s.isPartOf))
    parentname = first (g.objects (parent, s.name)) if parent else None
    volume = first (g.objects (n, s.volumeNumber))
    ret = ''
    if parentname:
        ret += '{}'.format (parentname)
        if volume:
            ret += ', volume {}'.format (volume)
        issue = first (g.objects (parent, s.issueNumber))
        if issue:
            ret += ', issue {}'.format (issue)
    return ret

if __name__ == '__main__':
    g = Graph()
    result = g.parse ("index.ttl", format='turtle')
    s = Namespace("https://schema.org/")
    for ref in result.objects (predicate=s.citation):
        t = list (g.objects (ref, RDF.type))
        assert len (t) == 1
        t = t[0]

        name = first (g.objects (ref, s.name))
        authors = humanList ([formatPerson (s, g, author) for author in g.objects (ref, s.author)])
        published = first (g.objects (ref, s.datePublished ))
        refname = urlparse (ref).fragment
        if not refname:
            refname = first (g.objects (ref, s.alternateName))
        ret = '.. [{}]'.format (refname)
        if authors:
            ret += ' {}:'.format (authors)
        ret += ' *{}*.'.format (name)
        parent = formatParent (s, g, ref)
        if parent:
            ret += ' {}.'.format (parent)
        if published:
            ret += ' {}.'.format (published)
        urls = ['`{} <{}>`__'.format (formatDomain (url), url) for url in g.objects (ref, s.url)]
        if urls:
            ret += ' {}.'.format (', '.join (urls))
        print (ret)

