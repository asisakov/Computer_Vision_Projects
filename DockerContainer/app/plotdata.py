import pandas as pd
import matplotlib 
import seaborn as sns
import io

"""
Create the plot and save it to .png format image
"""


if __name__ == '__main__':
    from PIL import Image

matplotlib.use('agg') # backend parameter with antigrain rendering

def regression_plot():
    """
    Function for plotting the regression in seaborn
    """

    df = pd.read_csv('tempYearly.csv')

    sns_plot = sns.regplot(x='Rainfall', y='Temperature', data=df) # construct regression line

    image = io.BytesIO()

    sns_plot.figure.savefig(image, format = 'png')

    image.seek(0) # reset position of image to 0

    return image

if __name__ == '__main__':
    """
    Save the image to png file
    """
    image = regression_plot()
    im = Image.open(image)
    im.save('regress.png', 'PNG')