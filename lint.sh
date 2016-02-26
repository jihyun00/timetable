#!/bin/sh

set -e

echo "flake8..."

flake8 .

echo "import-order..."

import-order jeonminheebot .
