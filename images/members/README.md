# How to generate professional profile images without background

This is written by [Tae](https://taewoon.kim/).

1. Crop your face from your favorite image.
2. Run [backgroundremover](https://github.com/nadermx/backgroundremover) to remove the background and generate a PNG with the alpha channel of the background set as 0.

Some examples are [Tae](Taewoon.png) and [Chengcheng](chengcheng.png)

Somewhere in the future when I have time, I'll make a docker image that crops your face from the image and run the backgroundremover.
