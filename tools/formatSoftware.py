#!/usr/bin/env python3

from rdflib import URIRef, BNode, Literal, Graph, Namespace
from rdflib.namespace import RDF, NamespaceManager
from urllib.parse import urlparse
import sys
from itertools import chain, groupby
from jinja2 import Environment
from formatRefs import first
from rdf import RDFWalker

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
    result = g.parse (sys.stdin, format='turtle')
    s = Namespace ("https://schema.org/")

    items = []

    for n in g.subjects (RDF.type, s.SoftwareApplication):
        n = RDFWalker (g, s, n)
        if n.author:
            items.append (n)

    items = groupby (sorted (items, key=lambda x: str (x.author.name).lower ()), lambda x: x.author.name)
    print (template.render(items=items))

