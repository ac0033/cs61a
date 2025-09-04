import os
import sys

# Ensure parent directory is on sys.path so sibling packages are importable
PARENT_DIR = os.path.dirname(os.path.dirname(__file__))
if PARENT_DIR not in sys.path:
    sys.path.append(PARENT_DIR)

from projects.hog.ucb import trace  # re-export for local imports

__all__ = ["trace"]


