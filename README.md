# PySlides
A small python script to emulate a slide presentation.

# Requirements
python3  
colored: pip3 install colored  

# Usage:
 PySlides.py [-h] [-b BG] [-f FG] folder  
  
Create a folder for each different presentation and put them in the same folder as PySlide.py.  
Create a headers.txt file containing two lines: One for the presentation name and the other for any small secondary information that will compose the Title of the presentation.  
Create a txt file for each diferent slide. The names must be numbers in the same order of the slide presentation.  
The contents of the txt files must have no more than 30 lines and no more than 120 characters per line.  
The colors for the presentation frame are the ones used in the colored module.  
