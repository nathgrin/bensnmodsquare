
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib
import matplotlib.font_manager as font_manager
import matplotlib.colors
# matplotlib.rc('font',size=32)

import os

ntot = 31

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
},
'pastelrainbow': { # from https://colorswall.com/palette/164437 and adapted
    0: '#000000',
    1: '#ff5e5e',
    2: '#ffa45e',
    3: '#ffda5e',
    4: '#efef6c',
    5: '#76aa3e',
    6: '#2b7372',
    7: '#5e5eff',
    8: '#6c4cbd',
    9: '#794a94',
    10: '#c3a1c9',
},
}
    
def get_color(n,name):
    import matplotlib.colors as mcolors
    import matplotlib
    global ntot
    if name == "colorwheel":
        phase = -0.05#-0.025#
        # # print(n,n/11+phase)
        h = (n/ntot)+phase
        if h > 1:
            h = h-1
        # h = 1-h
        # return mcolors.hsv_to_rgb((h,1,1))
        cmap = plt.get_cmap('rainbow')
        return cmap(h)
    elif name == "viridis" or name == "inferno" or name == "plasma":
        phase = -0.05#-0.025#
        # # print(n,n/11+phase)
        h = (n/ntot)+phase
        if h > 1:
            h = h-1
        # h = 1-h
        # return mcolors.hsv_to_rgb((h,1,1))
        cmap = plt.get_cmap(name)
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
    # plt.xkcd()
    
    
    
    from matplotlib import patheffects
    from matplotlib import rcParams
    strokewidth = 4 if 'xkcd' in fontname else 2.5
    rcParams.update({'path.effects': [
            patheffects.withStroke(linewidth=strokewidth, foreground="w")],})
    
    load_matplotlib_local_fonts(fontname)
    
    
    print(" >",fname)
    
    w,h = 10,10
    fig = plt.figure(frameon=False,figsize=(w,h))
    # fig.set_size_inches(w,h)
    # fig.set_dpi(300)
    
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    
    for i in range(1,n):
        for j in range(1,n):
            
            x,y,number = j/n,1-i/n,i*j % n #(i*i+j*j) % n #
            ax.add_patch(Rectangle((x-0.5/(n+1),y-0.5/(n+1)), 1/(n+1), 1/(n+1),color=get_color(number,colorsname)))
            if 'xkcd' in fontname:
                ax.text(x,y,str(number),va='center',ha='center',transform=ax.transAxes,fontsize=12,c=fontcolor)#fontsize=24
            else:
                for strokewidth,fontcolor in [(3,'w'),(2,'k')]:
                    ax.text(x,y-0.0005,str(number),va='center',ha='center',transform=ax.transAxes,fontsize=12,c=fontcolor)#fontsize=24
            
    
    # ax.imshow(your_image, aspect='auto')
    print("SAVING",fname)
    plt.savefig(fname,dpi=300)
    plt.show()
    

    
def main(): 
    
    
    
    global ntot
    fontname = 'xkcd-script.ttf'
    n = ntot
    colorsname = 'speels'
    fontcolor = 'w'
    i = 0
    for fontname in ['Montserrat-VariableFont_wght.ttf']:#'xkcd-script.ttf']:#,'xkcd.otf',
        fontcolor='k' if 'xkcd' in fontname else 'w'
        for colorsname in ['plasma','viridis']:#['colorwheel']:#,'pastelrainbow']:#,]:#,'vaal','speels']:
            # fname = '%s.png'%('abcdefghijklmnopqrstuvwxyz'[i])
            # i += 1
            fname = "bens_nmod_square_%i_%s_%s_%s.png"%(n,fontname,colorsname,fontcolor)
            fname = fname.replace('.otf','').replace('.ttf','')
            
            
            make_fig(fname,n,fontname,colorsname,fontcolor)
    
    
if __name__ == "__main__":
    main()
