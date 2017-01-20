#!/usr/bin/env python3

from rdflib import URIRef, BNode, Literal, Graph, Namespace
from rdflib.namespace import RDF, NamespaceManager
from urllib.parse import urlparse
import sys
from itertools import chain, groupby
from jinja2 import Environment
from formatRefs import first

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

if __name__ == '__main__':
    env = Environment ()
    env.filters['urlparse'] = urlparse
    template = env.from_string ("""
{% macro schemaval(n, name, tag='span') -%}
<{{ tag }} property="{{ name }}">{{ n|attr(name) }}</{{ tag }}>
{%- endmacro %}
{%- for companyname, software in items %}
    {% set company = companyname._ %}
    <div typeof="{{ company.a }}" class="company">
    {{ schemaval(company, 'name', 'h3') }}
    {% set addr = company.address %}
    <p property="address">
        {% if addr.streetAddress %}{{ schemaval(addr, 'streetAddress') }}<br>
        {% elif addr.postOfficeBoxNumber %}PO box {{ schemaval(addr, 'postOfficeBoxNumber') }}<br>
        {% endif %}
        {{ schemaval(addr, 'postalCode') }} {{ schemaval(addr, 'addressLocality') }}
    </p>
    {% set url = company.url %}
    {% if url %}
        <p><a property="url" href="{{ url }}">{{ url }}</a></p>
    {% endif %}
    <div class="products">
    {%- for s in software|sort(attribute='name') %}
        <div typeof="{{ s.a }}" id="{{ s|string|urlparse|attr('fragment') }}" class="softwareProduct">
            <h4>{{ schemaval(s, 'name') }}{% if s.softwareVersion %} ({{ schemaval(s, 'softwareVersion') }}){% endif %}</h4>
            <p>
                {% if s.dateCreated %}{{ schemaval(s, 'dateCreated') }}
                    {% if s.datePublished %}/{{ schemaval(s, 'datePublished') }}{% endif %}
                {% elif s.datePublished %}{{ schemaval(s, 'datePublished') }}
                {% endif %}
            </p>
            {% if s.description %}{{ schemaval(s, 'description', 'p') }}{% endif %}
            <ul property="offers">
            {% for o in s.offers_|sort(attribute='name') %}
                <li>
                {% if o.name %}{{ schemaval(o, 'name') }}, {% endif %}
                <span property="priceSpecification">{{ schemaval(o.priceSpecification, 'price') }}
                {{ schemaval(o.priceSpecification, 'priceCurrency') }}</span>,
                {{ schemaval(o, 'validFrom') }}{% if o.validThrough and o.validFrom != o.validThrough %}–{{ schemaval(o, 'validThrough') }}{% endif %}
                </li>
            {% endfor %}
            </ul>
        </div>
    {% endfor -%}
    </div>
    </div>
{% endfor %}""")
    g = Graph()
    result = g.parse ("index.ttl", format='turtle')
    s = Namespace ("https://schema.org/")

    items = []

    for n in g.subjects (RDF.type, s.SoftwareApplication):
        n = RDFWalker (g, s, n)
        if n.author:
            items.append (n)

    items = groupby (sorted (items, key=lambda x: str (x.author.name).lower ()), lambda x: x.author.name)
    print (template.render(items=items))

