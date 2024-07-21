
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib
import matplotlib.font_manager as font_manager
import matplotlib.colors
# matplotlib.rc('font',size=32)

import os

thecolors = {
'vaal': { # Childish
    0: 'lightcoral',
    1: 'darkseagreen',
    2: 'skyblue',
    3: 'lightpink',
    4: 'sandybrown',
    5: 'greenyellow',
    6: 'cornflowerblue',
    7: 'gold',
    8: 'aquamarine',#'turquoise',
    9: 'mediumslateblue',
    10: 'salmon',
},
'speels': { # Childish
    0: 'firebrick',
    1: 'yellowgreen',
    2: 'deepskyblue',
    3: 'hotpink',
    4: 'darkorange',
    5: 'lime',
    6: 'mediumblue',
    7: 'gold',
    8: 'darkcyan',
    9: 'blueviolet',
    10: 'tomato',
},
'firstguess': { # First guesses
    0: 'firebrick',
    1: 'seagreen',
    2: 'deepskyblue',
    3: 'hotpink',
    4: 'darkorange',
    5: 'limegreen',
    6: 'midnightblue',
    7: 'gold',
    8: 'darkcyan',
    9: 'indigo',
    10: 'tomato',
}
}
    
def get_color(n,name):
    import matplotlib.colors as mcolors
    import matplotlib
    if name == "colorwheel":
        phase = -0.05
        # # print(n,n/11+phase)
        h = (n/11)+phase
        if h > 1:
            h = h-1
        # h = 1-h
        # return mcolors.hsv_to_rgb((h,1,1))
        cmap = matplotlib.cm.get_cmap('rainbow')
        return cmap(h)
    else:
        return thecolors[name].get(n,"white")
        
def load_matplotlib_local_fonts(fname):

    # Load a font from TTF file, 
    # relative to this Python module
    # https://stackoverflow.com/a/69016300/315168
    font_path = os.path.join(os.path.dirname(__file__), fname)
    assert os.path.exists(font_path)
    font_manager.fontManager.addfont(font_path)
    prop = font_manager.FontProperties(fname=font_path)

    #  Set it as default matplotlib font
    matplotlib.rc('font', family='sans-serif') 
    matplotlib.rcParams.update({
        'font.size': 16,
        'font.sans-serif': prop.get_name(),
    })
    
    
def make_fig(fname, n,fontname,colorsname,fontcolor):
    plt.xkcd()
    
    
    
    from matplotlib import patheffects
    from matplotlib import rcParams
    strokewidth = 4 if 'xkcd' in fontname else 2.5
    rcParams.update({'path.effects': [
            patheffects.withStroke(linewidth=strokewidth, foreground="w")],})
    
    load_matplotlib_local_fonts(fontname)
    
    
    print(" >",fname)
    
    w,h = 10,10
    fig = plt.figure(frameon=False)
    fig.set_size_inches(w,h)
    
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    
    for i in range(1,n):
        for j in range(1,n):
            
            x,y,number = j/n,1-i/n,i*j % n #(i*i+j*j) % n #
            ax.add_patch(Rectangle((x-0.5/(n+1),y-0.5/(n+1)), 1/(n+1), 1/(n+1),color=get_color(number,colorsname)))
            ax.text(x,y,str(number),va='center',ha='center',transform=ax.transAxes,fontsize=24,c=fontcolor)
            
    
    # ax.imshow(your_image, aspect='auto')
    fig.savefig(fname)
    plt.show()
    
    
def main(): 
    
    fontname = 'xkcd-script.ttf'
    n = 11
    colorsname = 'speels'
    fontcolor = 'w'
    i = 0
    for fontname in ['Montserrat-VariableFont_wght.ttf','xkcd-script.ttf']:#'xkcd.otf',
        fontcolor='k' if 'xkcd' in fontname else 'w'
        for colorsname in ['colorwheel','vaal','speels']:
            fname = '%s.png'%('abcdefghijklmnopqrstuvwxyz'[i])
            i += 1
            # fname = "bens_nmod_square_%i_%s_%s_%s.png"%(n,fontname,colorsname,fontcolor)
            # fname = fname.replace('.otf','').replace('.ttf','')
            
            
            
            make_fig(fname,n,fontname,colorsname,fontcolor)
    
    
if __name__ == "__main__":
    main()