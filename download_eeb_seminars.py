curl "https://www.eeb.ucla.edu/seminars.php?id=[001-800]" -o "file_#1.html"

####or 
        
for ii in {001..7};
do curl "https://www.eeb.ucla.edu/seminars.php?id=" $ii > ii.html;
done