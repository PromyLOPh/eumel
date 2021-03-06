History
-------

In 1974 the research group *Programmiersprachen und Compiler II* at TU Berlin
led by C.H.A Koster and Hochschulrechenzentrum (HRZ) Bielefeld developed
different versions of *SLAN*, a programming language family suited for
educational purposes. This language was later renamed to *ELAN*, an
abbreviation for *Elementary Language* [hahn79]_ [klingen83]_ or *Educational
Language* [hommel79]_.

Jochen Liedtke and Ulrich Bartling, both studying maths at Bielefeld University
at that time, created a compiler for SLAN3B as part of their diploma thesis in
1976 [liedtke76]_\ [bartling76]_. It was written in CDL, a machine independent
compiler description language, and generated code for Siemens’ BS 1000 and
BS 2000 mainframe operating system running on a BS 4004/45 machine. It was
later ported to the IBM 370 and TR 440 [hahn79]_.

But ELAN was supposed to be used in schools or at universities and most of them
could not affort the cost of such a machine. Thus a compiler and runtime system
for the smaller and less expensive microprocessors was needed [liedtke79]_.
Development of this system began in 1977 or 1978\ [#]_. It ran on the Zilog Z80
microprocessor with 64 kilobytes of RAM. This machine’s cost were approximately
20,000 DM (10,000 USD). The runtime system was called *Extendable multi user
microprocessor ELAN system*, abbreviated *EUMEL*.

A year later, in 1979, details about EUMEL were published in GMD Spiegel
[liedtke79]_, a quarterly publication published by GMD, and then presented at
*9. Jahrestagung der Gesellschaft für Informatik* at University of Bonn
[kloeckner79]_. Officially the cooperation between HRZ Bielefeld and GMD began
in fall 1979 [gmdspiegel85d]_.

The original ELAN compiler written by Liedtke and Bartling was rewritten in
1982 as part of project MIKROS at GMD [eumelspiegel82d]_. Its replacement was
programmed using CDL’s successor, CDL2 [cdl2-basismaschine82]_ [gmdbericht84]_.
This work resulted in ports of EUMEL to different processor architectures,
starting with Zilog 8001 used by the Olivetti M 20. This version was presented
a year later at Hannover Messe 1983 [computerwoche83a]_ [rechenanlagen83]_.

For their efforts to `transfer EUMEL to Japan`_ a delegation consisting of
Konrad Klöckner, Jochen Liedtke, Peter Heyderhoff, Dietmar Heinrichs and Uwe
Beyer received the *Technologie-Transfer-Preis* worth 15.000 DM by Minister of
Scientific Research Heinz Riesenhuber on 1985-12-09. [happycomputer86]_
[gmdspiegel85d]_ [generalanzeiger85]_

Another two years later, in October 1987, the spin-off company ERGOS (Ergonomic
Office Software GmbH) finally started marketing EUMEL to customers. GMD was
still responsible for development and maintenance of EUMEL and schulis until
1990 [gmdspiegel87c]_.

.. [#] See [gmdspiegel85a]_, [liedtke93]_, [gmdbericht84]_, [ambros90b]_ and [praxis1]_

.. _transfer EUMEL to Japan: popularity_

Releases
^^^^^^^^

The following table lists release dates. It was reconstructed from multiple
sources.

.. csv-table::
   :header: Version,Date,

    0.7,May 1979, .. \_:person_dewitz
    1.5, ≤1981
    1.5.5, ≤1981-07, [eumelspiegel81a]_
    1.5.6, 1981-10-12, [eumelspiegel81b]_
    1.6, ≤fall 1982, [alwr82]_
    1.6.3,1982-05-07, [eumelspiegel82b]_
    1.6.4,1982-07-01, [eumelspiegel82d]_
    1.6.5,1982-10-10, [eumelspiegel82c]_
    1.7, ≤mid 1984, [korrekturen84]_
    1.7.3, ≤1985-09-21, [eumelaktuell85]_
    1.7.5, 1986-10-01, [eumelaktuell86]_ p. 9
    1.8.0, 1986-10-01, [eumelaktuell87a]_ p. 56
    1.8.7, ≤1990, [ambros90b]_

.. figure:: assets/releases.svg

L3
^^

Ideas for EUMEL’s successor „version 2.0“ were first presented by Liedtke in
1985 [gmdspiegel85c]_.  Since fall 1986 EUMEL „native code“ was in development
[gmdbericht86a]_.  This would later become the *Level 3 Operating System (L3)*,
which was presented in 1988. It dropped the EUMEL0 virtual machine in favor of
native x86 code since Intel’s 386 processor provided all the features necessary
[gmdspiegel88a]_. In the same year, on 1988-06-30, a workshop with 63
attendants was held at GMD Birlinghofen  [gmdspiegel88c]_

Workshops
^^^^^^^^^

Yearly workshop were held at different locations, first at Bielefeld University
and later at GMD Birlinghofen.

.. csv-table::
    :header: Date,Location,Attendance,

    1981-05-15,,,[eumelspiegel81a]_
    1982-05-15,Bielefeld University,,[eumelspiegel82b]_ [eumelspiegel82d]_
    1983-05-07,Bielefeld University,,[einladung-workshop83]_
    1984-05-19,Bielefeld University,,(see picture below) [einladung-workshop84]_
    1985-09-21,GMD Birlinghofen,300,[gmdspiegel85c]_ [eumelaktuell86]_ p. 31
    1986-10-04,GMD Birlinghofen,350,[gmdbericht86b]_ [eumelaktuell87a]_ p. 56
    1987-09-19/21,GMD Sankt Augustin,200/100,[gmdspiegel87b]_
    1988-10-01,Realschule Niederpleis,200,[gmdspiegel88d]_

.. figure:: assets/eumel-tagung-84-resized.jpg
   :target: assets/eumel-tagung-84.jpg

   5th EUMEL workshop at Bielefeld University. Picture taken 1984-05-19. Source: BITS_

.. _BITS: http://www.uni-bielefeld.de/bits/

