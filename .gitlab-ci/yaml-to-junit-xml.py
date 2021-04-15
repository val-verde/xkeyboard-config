#!/usr/bin/env python3
#
# Converts the YAML format from the layout tester into JUnit XML
#
# This file is formatted with Python Black

import yaml
import sys
from xml.dom import minidom

with open(sys.argv[1]) as fd:
    yml = yaml.safe_load(open(sys.argv[1]))

    doc = minidom.Document()
    suite = doc.createElement("testsuite")
    suite.setAttribute("name", "XKB layout compilation tests")
    doc.appendChild(suite)

    # JUnit differs between test case failures
    # and errors (something else blew up)
    # We use failures for unrecognized keysyms and errors
    # for everything else (i.e. keymap compilation errors)
    ntests, nfailures, nerrors = 0, 0, 0

    for testcase in yml:
        ntests += 1
        node = doc.createElement("testcase")
        node.setAttribute("classname", f"{testcase['rmlvo'][0]} rules layout test")
        # We don't care about rules and model here, LVO is enough
        r, m, l, v, o = testcase["rmlvo"]
        if v:
            name = f"{l}({v})"
        else:
            name = l
        if o:
            name += f", {o}"
        node.setAttribute("name", f"keymap compilation: {name}")
        suite.appendChild(node)

        if testcase["status"] != 0:
            f = None
            if testcase["status"] == 99:  # missing keysym
                nfailures += 1
                f = doc.createElement("failure")
            else:  # everything else is an error
                nerrors += 1
                f = doc.createElement("error")
            f.setAttribute("message", testcase["error"])
            cdata = doc.createCDATASection(
                f"Error message: {testcase['error']} in command {testcase['cmd']}"
            )
            f.appendChild(cdata)
            node.appendChild(f)

    suite.setAttribute("tests", str(ntests))
    suite.setAttribute("errors", str(nerrors))
    suite.setAttribute("failures", str(nfailures))

    print(doc.toprettyxml(indent="  "))
