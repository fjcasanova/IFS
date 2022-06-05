from numpy import array, dot, full
from numpy.random import choice
from math import cos,sin,floor
from random import randint
from matplotlib.image import imsave
import matplotlib.pyplot as plt

def image(ifs, n) :
    IFS = ifs()
    matrices = IFS.matrices
    vecteurs = IFS.vecteurs
    probabilites = IFS.probabilites
    m = len(matrices)
    def f(i, x ,y ) :
        M = matrices[i]
        v = vecteurs[i]
        X = array([x,y])
        return M.dot(X) + v
    x, y = 0, 0
    X, Y = [x], [y]
    for k in range(n) :
        i = choice([k for k in range(m)], p = probabilites)
        x, y = f(i-1, x, y)
        X.append(x)
        Y.append(y)
    plt.scatter(X, Y, s = .5, edgecolor = IFS.color1)
    plt.scatter(X, Y, s = .001, edgecolor = IFS.color2)
    plt.axis('off')
    plt.rcParams["figure.figsize"] = (50,50)
    plt.show()

class Feuille() :
    def __init__(self) :
        self.name = 'Feuille'
        self.matrices = [array([[.14, .01], [0, .51]]), array([[.43, .53], [-.45, .5]]),array([[.45, -.49], [.47, .47]]),array([[.49, 0],[0, .51]])]
        self.vecteurs = [array([-.08,-1.31]), array([1.49,-.75]), array([-1.62,-.74]), array([.02,1.62])]
        self.probabilites = [1/len(self.matrices) for k in range(len(self.matrices))]
        self.color1 = 'indianred'
        self.color2 = 'brown'

class Spirale() :
    def __init__(self) :
        self.name = 'Spirale'
        self.matrices = [array([[0.787879   , -0.424242    ],
                                [0.242424    , 0.859848    ]]),
                        array([[-0.121212     , 0.257576    ],
                                [0.151515     , 0.053030     ]]),
                        array([[0.181818, -0.136364],
                                [0.090909,0.181818]])]
        self.vecteurs = [array([1.758647   ,1.758647   ]), array([-6.721654     ,1.377236     ]), array([6.086107,1.568035])]
        self.probabilites = [.1,.8,.1]
        self.color1 = 'red'
        self.color2 = 'firebrick'

class Mandelbrot() :
    def __init__(self) :
        self.name = 'Mandelbrot'
        self.matrices = [array([[.202, -.805],[-.689,-.342]]), array([[.138,.665],[-.502,-.222]])]
        self.vecteurs = [array([-.373,-.653]), array([.66,-.277]),]
        self.probabilites = [1/len(self.matrices) for k in range(len(self.matrices))]
        self.color1 = 'mediumseagreen'
        self.color2 = 'darkgreen'

class Arbre() :
    def __init__(self) :
        self.name = 'Arbre'
        self.matrices = [array([[.05, .0],[0,.4]]), array([[-.05,.0],[.0,-.4]]),array([[.03,-.14],[.0,.26]]),array([[-.03,.14],[0,-.26]]), array([[.56,.44],[-.37,.51]]), array([[.19,.07],[-.1,.15]]), array([[-.33,-.34],[-.33,.34]])]
        self.vecteurs = [array([-.06,-.47]), array([-.06,-.47]), array([-.16,-.01]), array([-.16,-.01]), array([.3,.15]), array([-.2,.28]), array([-.54,.39])]
        self.probabilites = [1/len(self.matrices) for k in range(len(self.matrices))]
        self.color1 = 'mediumseagreen'
        self.color2 = 'darkgreen'

class Sierpinsky() :
    def __init__(self) :
        self.name = 'Sierpinsky'
        self.matrices = array([[.5,0],[0,.5]])
        self.vecteurs = [array([0,.0]), array([.5, .0]), array([0., 0.5])]
        self.probabilites = [1/len(self.matrices) for k in range(len(self.matrices))]
        self.color1 = 'mediumseagreen'
        self.color2 = 'darkgreen'

class Arbre2() :
    def __init__(self) :
        self.name = 'Arbre2'
        self.matrices = [array([[.05, .0],
                                [0,.6]]),
                        array([[-.05,.0],
                                [.0,-.5]]),
                        array([[ .6 * cos(.698), -.5 * sin(.698)],
                                [.6 * sin(.698),  .5 * cos(.698)]]),
                        array([[ .5 * cos(.3490),-.45* sin(.3492)],
                                [.5 * sin(.3490), .45* cos(.3492)]]),
                        array([[ .5 * cos(-.524),-.55* sin(-.524)],
                                [.5 * sin(-.524), .55* cos(-.524)]]),
                        array([[.55 * cos(-.698),-.4 * sin(-.698)],
                                [.55* sin(-.698), .4 * cos(-.698)]])]
        self.vecteurs = [array([0,0]), array([0,1]), array([0,.6]), array([0,1.1]), array([0,1]), array([0,.7])]
        self.probabilites = [1/len(self.matrices) for k in range(len(self.matrices))]
        self.color1 = 'mediumseagreen'
        self.color2 = 'darkgreen'

class Dragon() :
    def __init__(self) :
        self.name = 'Dragon'
        self.matrices = [array([[0.824074,0.281428],[-0.212346,0.864198]]), array([[0.088272,0.520988],[-0.463889,-0.377778]])]
        self.vecteurs = [array([-1.882290,-0.110607]), array([0.785360, 8.095795])]
        self.probabilites = [.8,.2]
        self.color1 = 'red'
        self.color2 = 'firebrick'

class Flocon() :
    def __init__(self) :
        self.name = 'Flocon'
        self.matrices = [array([[0.382   , -0.0    ],
                                [0.0    , 0.382    ]]),
                        array([[ 0.118     , -.3633    ],
                                [0.3633     , 0.118     ]]),
                        array([[0.118, .3633],
                                [-.3633, .118]]),
                        array([[-.309, -.2245],
                                [.2245, -.309]]),
                        array([[-.309, .2245],
                                [-.2245, -.309]]),
                        array([[0.382, .0],
                                [-.0, -.382]])]
        self.vecteurs = [array([.309   ,.57   ]), array([.3633     ,.3306     ]), array([.518,.694]),array([.607   ,.309   ]), array([.7016     ,.5335     ]), array([.309,.677])]
        self.probabilites = [1/len(self.matrices) for k in range(len(self.matrices))]
        self.color1 = 'skyblue'
        self.color2 = 'steelblue'

class Pythagore() :
    def __init__(self) :
        self.name = 'Pythagore'
        self.matrices = [array([[.01   , 0    ],
                                [ 0    , 0.45    ]]),
                        array([[ -.01     , 0    ],
                                [ 0     , -.45     ]]),
                        array([[.42, -.42],
                                [.42, .42]]),
                        array([[.42, .42],
                                [-.42, .42]])]
        self.vecteurs = [array([.0   ,.0   ]), array([.0     ,.4     ]), array([.0,.4]),array([.0   ,.4   ])]
        self.probabilites = [1/len(self.matrices) for k in range(len(self.matrices))]
        self.color1 = 'mediumseagreen'
        self.color2 = 'darkgreen'
