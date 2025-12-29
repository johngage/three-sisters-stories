#!/bin/bash
cd /Users/johngage/Family/three_sisters/three-sisters-stories
python build.py
git add .
git commit -m "Updated content $(date '+%Y-%m-%d')"
git push
echo "✅ Website updated!"
