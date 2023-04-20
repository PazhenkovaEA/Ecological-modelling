# Analysis of NGS data on Cruncher

I. Download the data

 Usually we got the data from Eurofins ([https://eurofinsgenomics.eu/](https://eurofinsgenomics.eu/)), ask Tomaž for login and password. Just open order page and ***scroll down***.

Here is an example of fastq you need to download.

![Screenshot 2022-06-13 at 09.46.00.png](Analysis%20of%20NGS%20data%20on%20Cruncher%206234b67a8d64486c9625838b47253c03/Screenshot_2022-06-13_at_09.46.00.png)

Then, copy the data to Cruncher. Name the directory as library you are going to analyse (e.g. in this case, DAB073). So the path will be: **~/Documents/obi3/DAB073**

II.  Format input files.

For details about the pipeline and input format check github: https://github.com/PazhenkovaEA/ngs_pipelines.py

You’ll get from the lab file(s) from the robot (Aliquot plates), you should place them to **~/Documents/obi3/DAB073/AP**. Check, that file names are “something_libraryname_APnumber.xls” (e.g. 220510_DAB073_B65.xls), you’ll probably need to rename original files. 

Also you’ll get a file, where library is connected to aliquot plate. It’s long, and you need to keep  only rows for your library. Place it to **~/Documents/obi3/DAB073/**, rename to AliquotP.xlsx (not mandatory, just to avoid typing extra arguments while running scripts). Check, that in “Library_BC” column library name is correct. 

For the bear another files (primers and tags) are standard, you don’t need to change anything. For other species check them as well.

III. Analysis.

❗️  (***Optionally***) since work schedule on Cruncher is a bit chaotic, I usually check two things before I start. First, if there is enough space on disk (you’ll need around 40 Gb per library). From terminal you can do it with `df -h` . It shows you free place on all drives. Second, check if somebody is already running something. Here the utility `top`  helps you (ctrl+c to exit). 

Run the script from this location:

`cd ~/Documents/obi3`

I use the utility ***screen*** to run an analysis in the background. Check manual for details, but basic commands are:

`screen -S libraryname` to create a new screen

`screen -r libraryname` to recover existing screen 

to exit from screen press ctrl+a, then D. To kill the screen press ctrl+a then K. 

Activate obi3 enviroment

`. /home/romunov/Elena/obitools3/obi3-env/bin/activate`

Create ngsfilter

`python create_ngsfilter.py --project=./DAB073 --plates=./DAB073/AliquotP.xlsx --tags=./UA_tagscombo.csv --primers=./UA_primers.csv`

Run script obitools3 for demultiplexing (takes about 3 hours)

`python obitools3.py --project=./DAB073 --library=DAB073 --reads1=./DAB073/NG-30277_DAB073_lib600140_8142_1_1.fastq --reads2=./DAB073/NG-30277_DAB073_lib600140_8142_1_2.fastq --primers=./UA_primers.csv`

Allele calling part:

`python callAllele1.py --project=./DAB073 --primers=./UA_primers.csv`

That’s almost it, check the “results” folder.

The last step. Create a read count report. For this, you will need [custom_functions.R](https://github.com/PazhenkovaEA/ngs_pipelines.py/blob/master/custom_functions.R) and [read_count.Rmd](https://github.com/PazhenkovaEA/ngs_pipelines.py/blob/master/read_count.Rmd) from https://github.com/PazhenkovaEA/ngs_pipelines.py. I usually run it on my laptop, not on Cruncher. You’ll need to change a path and library name in [read_count.Rmd](https://github.com/PazhenkovaEA/ngs_pipelines.py/blob/master/read_count.Rmd), and it will produce a nice pdf. 

This is how the final map with results looks like:

![Screenshot 2022-06-13 at 17.23.25.png](Analysis%20of%20NGS%20data%20on%20Cruncher%206234b67a8d64486c9625838b47253c03/Screenshot_2022-06-13_at_17.23.25.png)