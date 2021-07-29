set -o errexit
#dewarping
cd page_dewarp
for f in example_input/*
do 
    python page_dewarp.py $f
done
#detection
cd ../detector/
python main/demo.py
#recognition
cd ..
python demo.py