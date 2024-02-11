#! /bin/bash

###########################
# clean notebooks output
###########################

# clean notebooks /notebooks/
for f in ./*/*.ipynb 
do
  # # html   # jupyter nbconvert --to html $f
  jupyter nbconvert --clear-output --inplace $f   # clear output
  # jupytext --to py:percent $f   # .py
done



###########################
# copy .py from .ipynb
###########################

# => COMMAND TO MAKE .py FRM .ipynb FILES AND COPY ALL IN ./src/ FOLDER
# => UNCOMMENT IF NEEDED

# for f in *.ipynb 
# do
#   jupytext --to py:percent $f
#   fn=$(basename $f); #   echo "FN => $fn"
#   new="./src/"$fn ; #   echo "new => $new"
#   mv $f $new
# done

# for f in ./*/*.ipynb 
# do
#   jupytext --to py:percent $f
#   fn=$(basename $f); #   echo "FN => $fn"
#   new="./src/"$fn ; #   echo "new => $new"
#   mv $f $new
# done


###########################
# black and flake8
###########################


.venv/bin/python3 -m flake8 .
.venv/bin/python3 -m black .


###########################
# pytest
###########################

# .venv/bin/python3 -m pytest 
.venv/bin/python3 -m pytest -vv -x -s tests/