#!/bin/bash
package_name=$1
mkdir $package_name
cd    $package_name
touch run.py
touch config.py
mkdir app
cd    app
touch __init__.py
mkdir templates
mkdir static
mkdir module_one
cd    module_one
touch __init__.py
touch controllers.py
touch models.py
cd    ../templates
mkdir module_one
cd    module_one
touch hello.html
