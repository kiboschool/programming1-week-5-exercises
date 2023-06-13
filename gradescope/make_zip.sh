#!/usr/bin/env bash

# Loop through all subdirectories to find test files
test_cases=$(find .. -type f -name "test_*.py" -maxdepth 2)
for test in $test_cases; do
  # Get the parent directory name
  parent_dir=$(basename "$(dirname "$test")")
  mkdir -p ${parent_dir}
  cp "${test}" "${test#*/}"
done

find . -type f -name 'test_*.py' -exec zip gradescope.zip setup.sh requirements.txt run_autograder run_tests.py {} +

# Remove test files from gradescope after zip
for test in $test_cases; do
  parent_dir=$(basename "$(dirname "$test")")
  rm -Rf "${parent_dir}"
done
