#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

import radiopaedia.commands
import fma.commands
import unifr.commands
from spiderpig import run_cli


if __name__ == '__main__':
    run_cli(
        namespaced_command_packages={
            'radiopaedia': radiopaedia.commands,
            'fma': fma.commands,
            'unifr': unifr.commands,
        }
    )
