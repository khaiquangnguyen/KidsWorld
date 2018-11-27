from helpers import print_title_fancily
islands = ["MathParadise", "HistoryField"]
WORLD_MAP = r"""
                  ,_   .  ._. _.  .
           , _-\','|~\~      ~/      ;-'_   _-'     ,;_;_,    ~~-
  /~~-\_/-'~'--' \~~| ',    ,'      /  / ~|-_\_/~/~      ~~--~~~~'--_
  /              ,/'-/~ '\ ,' _  , '|,'|~                   ._/-, /~
  ~/-'~\_,       '-,| '|. '   ~  ,\ /'~                /    /_  /~
.-~      '|        '',\~|\       _\~     ,_  ,               /|
          '\        /'~          |_/~\\,-,~  \ "         ,_,/ |
           |       /            ._-~'\_ _~|              \ ) /
            \   __-\           '/      ~ |\  \_          /  ~
  .,         '\ |,  ~-_      - |          \\_' ~|  /\  \~ ,
               ~-_'  _;       '\           '-,   \,' /\/  |
                 '\_,~'\_       \_ _,       /'    '  |, /|'
                   /     \_       ~ |      /         \  ~'; -,_.
                   |       ~\        |    |  ,        '-_, ,; ~ ~\
                    \,      /        \    / /|            ,-, ,   -,
                     |    ,/          |  |' |/          ,-   ~ \   '.
                    ,|   ,/           \ ,/              \       |
                    /    |             ~                 -~~-, /   _
                    |  ,-'                                    ~    /
                    / ,'                                      ~
                    ',|  ~
                      ~'
                      """


class Island:
    def __init__(self, name, description):
        self.buildings = []
        self.name = name
        self.description = description

    def show_island_name(self):
        print_title_fancily(self.name, self.description)


MathParadise = Island("MathParadise", "A paradise for math nerds")


class Building:
    def __init__(self, type):
        self.type = type


class Marketplace (Building):
    def __init__(self, parent_island=None):
        self.parent_island = parent_island
        self.vendors = []


class Vendor:
    def __init__(self, name, items=[]):
        self.items = items


class Item:
    def __init__(self, name, type, attributes=None):
        self.type = type
        self.attributes = attributes
        self.attributes = attributes
