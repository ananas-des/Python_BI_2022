#!/bin/bash
sed -i 's/if index is not None and isinstance(index, set):/# if index is not None and isinstance(index, set):/' ./ultraviolent/lib/python3.11/site-packages/pandas/core/frame.py
sed -i 's/    raise ValueError("index cannot be a set")/#    raise ValueError("index cannot be a set")/' ./ultraviolent/lib/python3.11/site-packages/pandas/core/frame.py