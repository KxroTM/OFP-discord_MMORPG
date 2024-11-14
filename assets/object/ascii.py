
spawn_monster = [
"    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠲⣖⠒⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣴⣶⡄⠀⢰⣀⡼⡇⠀⠘⡆⠀⣀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⠿⠿⠛⣛⡿⠷⠶⣟⢷⡴⣧⣤⣰⡓⠉⡃⢀⣠⠄⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠟⠋⠀⠀⢀⠞⠁⠀⠀⠀⠈⢳⣿⡟⠒⢿⣿⠢⡭⡝⠁⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠋⠀⠀⣠⠤⠤⠼⣄⠀⠀⠿⠟⠀⡞⡿⢆⠀⠀⢻⣧⠙⢟⠋⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⣠⣿⣿⠋⠀⠀⢠⠎⠀⢀⣀⠀⠈⢳⡀⠀⠀⣼⡾⣧⠀⠀⠀⠀⢏⠏⠈⢧⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⣴⣿⡿⢁⡠⠔⠒⡞⠀⠀⠘⠿⠃⠀⢠⡿⢛⣿⡟⠓⠄⠀⠀⠀⠀⢸⢸⠀⠈⢆⠀⠀⠀⠀",
"⠀⠀⠀⠀⠰⢿⣿⣷⠋⠀⢀⣀⡙⢄⡀⠀⠀⠀⣠⣾⣷⣿⠋⠛⠀⠀⠀⠀⠀⠀⠈⡇⡧⢦⣼⡀⠀⠀⠀",
"⠀⠀⠀⠀⠘⣖⢺⣿⡀⠀⠘⠿⠃⠀⣹⢛⣿⠟⣋⠽⣾⡉⠃⠀⠀⠀⠀⠀⠀⠀⣀⡇⢡⠐⠂⡇⠀⠀⠀",
"⠀⢀⡆⢰⠺⣡⢋⣳⣵⣦⣤⣤⣤⣶⣿⣭⠶⡏⠙⠀⠈⠀⠀⠀⠀⢀⡤⠒⠉⢙⡢⡇⡘⠀⠀⢹⠀⠀⠀",
"⢀⡎⠣⠠⢧⠁⢸⢻⠹⡟⡇⠙⠇⠻⠀⠙⠀⠀⠀⠀⠀⠀⠀⠀⡴⠃⠀⢀⣠⣬⠟⡱⠁⠀⠀⠸⡄⠀⠀",
"⠈⠧⣀⣀⠸⡄⠈⢆⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢠⡇⣤⣰⠾⢋⡥⠊⠀⠀⠀⠀⢤⡇⠀⠀",
"⠀⠀⢠⡿⡎⣧⢲⡈⢦⠳⡀⠀⠀⠀⠀⢀⡀⠀⢰⡄⢠⣜⣷⠼⠛⣩⠤⠚⠁⠀⠀⠀⠀⠀⠰⠚⡇⠀⠀",
"⠀⠀⠀⡠⢛⣿⠠⠍⠂⠑⢍⡢⠼⣦⣷⣼⡷⠼⡖⣛⣩⠥⠒⠊⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀",
"⠀⠀⣴⡁⠾⢼⣀⣀⣀⣀⣀⣉⣑⣒⣒⣒⡓⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠠⠤⠤⠧⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠐⠒⠒⠤⠤⠤⠄⠀⠀⠀⠀⠈⠛⠛⠛⠛⠛⠛⠛⠛⠋⠉⠀⠀⠀⠉⠉⠒⠒⠒⠈⠉",
]

farmer_mob = [
"                          ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      ",
"                          ██▓▓▓▓▓▓▓▓██████████▓▓                        ",
"                          ▒▒▓▓▓▓▓▓██░░░░░░░░░░██                        ",
"                        ██▓▓▓▓████░░░░░░░░░░░░                    ▒▒▒▒▒▒",
"                        ▓▓▓▓████░░░░░░░░▒▒░░▒▒        ░░      ░░░░▒▒  ░░",
"                        ▓▓▓▓████░░░░░░░░▓▓░░▓▓        ░░░░░░  ▒▒▒▒▒▒    ",
"                        ▓▓▓▓██░░░░░░░░░░░░░░░░░░    ▒▒░░░░░░▒▒▒▒        ",
"                        ▓▓██████░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░░░░░            ",
"          ░░░░▒▒░░        ██████░░░░░░░░░░░░░▒▒▒        ░░░░            ",
"    ░░░░░░▒▒    ░░          ▒▒▒▒░░░░░░░░░░░░░           ░░░░            ",
"░░░░▒▒          ▒▒░░     ▒▒▒▒ ▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒        ░░░░            ",
"                  ░░░░▒▒▒▒  ▒▒▓▓▓▓▒▒▓▓▒▒▓▓▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒          ",
"                  ░░▒▒▒     ▒▒▓▓▓▓▒▒▓▓▒▒▓▓▒▒▒▒▓▓▒▒    ▒▒▒▒▒▒▒▒          ",
"            ░░░░▒▒░░▒▒      ▒▒▓▓▓▓▒▒▒▒▓▓▓▓▓▓▒▒▒▒▓▓▒▒  ▓▓▓▓▓▓            ",
"      ░░░░░░▒▒      ▒▒░░    ▒▒▓▓▓▓▓▓▒▒▓▓░░▓▓▓▓▒▒▓▓▓▓▒▒▓▓▓▓▓▓            ",
"  ░░░░▒▒              ░░░   ▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓            ",
"                      ▒▒░   ▒▒▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓              ",
"              ░░░░░░▒▒      ▓▓▓▓▓▓▓▓▒▒▓▓░░▓▓▓▓▒▒▓▓                      ",
"        ░░░░░░▒▒            ▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒▓▓                      ",
"    ░░░░▒▒                  ▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒                      ",
]


goblin_monster = [
r"                           __.--|~|--.__                               ,,;/;",
r"                         /~     | |    ;~\                          ,;;;/;;'",
r"                        /|      | |    ;~\\                     ,;;;;/;;;'",
r"                       |/|      \_/   ;;;|\                    ,;;;;/;;;;'",
r"                       |/ \          ;;;/  )                 ,;;;;/;;;;;'",
r"                   ___ | ______     ;_____ |___....__      ,;;;;/;;;;;'",
r"             ___.-~ \\\\(| \  \.\ \__/ /./ /:|)~   ~   \   ,;;;;/;;;;;'",
r"         /~~~    ~\    |  ~-.     |   .-~: |//  _.-~~--,;;;;/;;;;;'",
r"        (.-~___     \.'|    | /-.__.-\|::::| //~     ,;;;;/;;;;;'",
r"        /      ~~--._ \|   /          `\:: |/      ,;;;;/;;;;;'",
r"     .-|             ~~|   |  /V''''V\ |:  |     ,;;;;/;;;;;' \\",
r"    /                   \  |  ~`^~~^'~ |  /    ,;;;;/;;;;;'    ;",
r"   (        \             \|`\._____./'|/    ,;;;;/;;;;;'      '\\",
r"  / \        \                             ,;;;;/;;;;;'     /    |",
r" |            |                          ,;;;;/;;;;;'      |     |",
r"|`-._          |                       ,;;;;/;;;;;'              \\",
r"|             /                      ,;;;;/;;;;;'  \              \__________",
r"(             )                 |  ,;;;;/;;;;;'      |        _.--~",
r" \          \/ \              ,  ;;;;;/;;;;;'       /(     .-~_..--~~~~~~~~~~",
r" \__         '  `       ,     ,;;;;;/;;;;;'    .   /  \   / /~",
r" /          \\'  |`._______ ,;;;;;;/;;;;;;'    /   :    \/'/'       /|_/|   ``|",
r"| _.-~~~~-._ |   \ __   .,;;;;;;/;;;;;;' ~~~~'   .'    | |       /~ (/\/    ||",
r"/~ _.-~~~-._\    /~/   ;;;;;;;/;;;;;;;'          |    | |       / ~/_-'|-   /|",
r"(/~         \| /' |   ;;;;;;/;;;;;;;;            ;   | |       (.-~;  /-   / |",
r"|            /___ `-,;;;;;/;;;;;;;;'            |   | |      ,/)  /  /-   /  |",
r" \            \  `-.`---/;;;;;;;;;' |          _'   |T|    /'('  /  /|- _/  //",
r"   \           /~~/ `-. |;;;;;''    ______.--~~ ~\  |u|  ,~)')  /   | \~-==//",
r"     \      /~(   `-\  `-.`-;   /|    ))   __-####\ |a|   (,   /|    |  \\",
r"       \  /~.  `-.   `-.( `-.`~~ /##############'~~)| |   '   / |    |   ~\\",
]

knight = [
r"      _,.",
r"    ,` -.)",
r"   ( _/-\\\\-._",
r"  /,|`--._,-^|            ,",
r"  \_| |`-._/||          ,'|",
r"    |  `-, / |         /  /",
r"    |     || |        /  /",
r"     `r-._||/   __   /  /",
r" __,-<_     )`-/  `./  /",
r"'  \   `---'   \   /  /",
r"    |           |./  /",
r"    /           //  /",
r"\_/' \         |/  /",
r" |    |   _,^-'/  /",
r" |    , ``  (\/  /_",
r"  \,.->._    \X-=/^",
r"  (  /   `-._//^`",
r"   `Y-.____(__}",
r"    |     {__)",
r"          ()",
]

squeleton = [
r"              .7",
r"            .'/",
r"           / /",
r"          / /",
r"         / /",
r"        / /",
r"       / /",
r"      / /",
r"     / /  "      , 
r"    / /    "      ,
r"  __|/",
r",-\__\\",
r"|f-\"Y\|",
r"\()7L/",
r" cgD                              __ _",
r" |\(                            .'  Y '>,",
r"  \ \                          / _   _   \\",
r"   \\\                         )(_) (_)(|}",
r"    \\\                        {  4A   } /",
r"     \\\                        \\uLuJJ/\\l",
r"      \\\                       |3    p)/",
r"       \\\___ __________        /nnm_n//",
r"       c7___-__,__-)\,__)(\".  \_>-<_/D",
r"                  //V     \_\"-._.__G G_c__.-__<\"/ ( \\",
r"                         <\"-._>__-,G_.___)\   \\7\\",
r"                        (\"-.__.| \\\"<.__.-\" )   \ \\",
r"                        |\"-.__\"\  |\"-.__.-\".\   \ \\",
r"                        (\"-.__\"\". \\\"-.__.-\".|    \_\\",
r"                        \\\"-.__\"\"|!|\"-.__.-\".)     \ \\",
r"                         \"-.__\"\"\_|\"-.__.-\"./      \ l",
r"                          \".__\"\"\">G>-.__.-\">       .--,_",
r"                              \"\"  G",
]
