Xvfb -screen 0 1020x720x16 :99 &
x11vnc -display :99 -forever &
export DISPLAY=:99
cd ~
wget https://pjreddie.com/media/files/yolov3.weights -O /usr/local/lib/python3.7/dist-packages/goodbyecaptcha/models/yolov3.weights
while :
do
    export DISPLAY=:99
    rm /root/.local/share/pyppeteer/ -r
    python3.7 register.py $PROXY $SERVER
done
