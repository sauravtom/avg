# avg : artistic video generator
Converts photos into artistic videos & gifs


### Demo
![All examples](https://raw.githubusercontent.com/sauravtom/avg/master/samples/demonstration.gif)  

### Dependencies
* Python 2.7.x 
* PIL
* [Imagemagick](https://www.imagemagick.org/) (for .gif output)
* [ffmpeg](https://www.ffmpeg.org/) (for .mp4 output)

```
usage: avg.py [-h] -i IMAGE [-f FRAMES] [-d DELAY] [-v] -o SAVEPATH

AVG v1.0

arguments:
  -h, --help            show this help message and exit
  -i IMAGE, --image Source image path 
                    
  -f FRAMES, --frames Number of frames in output (default=6)

  -d DELAY, --delay Morphtime interval , time delay between frames (default value 5)
                                          
  -o SAVEPATH, --savepath SAVEPATH 
                          
  -v VIDEO, --video Get output media in video format 
      
```

### Usage

```
python avg.py -i input.png -o output.gif
```

If video output is required, then pass along the --video flag as well.
```
python avg.py -i input.png -o output.gif -v True
```

