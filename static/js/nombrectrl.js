/**
 * Created with PyCharm.
 * User: peter
 * Date: 30/08/13
 * Time: 17:54
 * To change this template use File | Settings | File Templates.
 */
app.controller('nombreCtrl', function ($rootScope) {
    $rootScope.nombrehgen = function(){nombrehgen($rootScope)};
    $rootScope.nombrefgen = function(){nombrefgen($rootScope)};
    $rootScope.nombrehgen();
    $rootScope.nombrefgen();

});

function nombrehgen($scope) {
    $scope.nombreh = nombreh()+" "+apellido();
}
function nombrefgen($scope) {
    $scope.nombref = nombref()+" "+apellido();
}
function apellido(){
    var apellidos = ["Abdalla","Abeysena","Adams","Agin","Amey","Anderson","Appel","Appleton","Archer","Arini","Arms","Armstrong","Ashurst","Austin","Baines","Baker","Banham","Barker","Barthelemy","Basker","Bates","Beaton","Beatty","Beckett","Bell","Bennett","Bentley","Berry","Bethell","Bevan","Billings","Birch","Bishop","Black","Bland","Blundell","Boam","Bone","Boon","Borrow","Bott","Bower","Bowskill","Bowyer","Bradley","Braswell","Braysher","Breen","Brittan","Britton","Broadley","Brown","Browne","Buffet","Bull","Burch","Burdett","Burton","Butcher","Carmel","Carpenter","Carr","Carrington","Carroll","Carter","Cartwright","Chainey","Chamberlain","Chambers","Chandler","Chanter","Chaplin","Chapman","Chase","Chatterton","Clancy","Clark","Clements","Coan","Cockrell","Cole","Collins","Comely","Coppard","Coupland","Courtenay","Cox","Coy","Craft","Crepy","Cripps","Cullingworth","Dailly","Dave","Davenport","Davies","Day","Delaney","Dixon","Doallo","Dobson","Doherty","Doodes","Douglas","Dowle","Dowling","Downer","Downing","Dudin","East","Eden","Edmonds","Edwards","Enfield","Estey","Evans","Fairbrass","Farmer","Ferreri","Fitzgerald","Flavin","Flanders","Fogg","Ford","Forster","Freeman","Frost","Gale","Galer","Galliford","Gannon","Gardner","Garland","Garlick","Garritt","Gatrill","Gee","George","Gerrard","Gibbons","Gill","Gladstone","Gogarty","Goodman","Goodrick","Grady","Graham","Grand","Grantham","Gray","Greaney","Greenacre","Greenwood","Griffin","Grist","Groom","Hall","Hallott","Hansen","Hard","Hardy","Harrigan","Harris","Harrison","Harvey","Hawkins","Hawkswell","Hayes","Haynes","Henrichs","Henriette","Heppleston","Hewitt","Hickman","Hicks","Highfield","Hignell","Hill","Hills","Hillyer","Hilton","Hines","Hogg","Hollingworth","Hollis","Hooper","Hough","Howard","Howes","Hoy","Huggett","Hyatt","Ilo","Jackson","James","Jarvis","Jaye","Jeffery","Jenkins","Jenks","Jennings","Jensen","Johnson","Jolly","Jones","Jordan","Joseph","Jowett","Kay","Keen","Keene","Kelly","Khan","Kidd","King","Kirkham","Krueger","Lasher","Law","Laws","Lawson","Lee","Lees","Legerton","Legrass","Legrice","Leuff","Lewis","Lifsey","Lindsay","Long","Longbottom","Lovecraft","Lovejoy","Lucas","Luttrell","Lyons","MacKay","MacNeil","Madsen","Maguire","Malone","Marrison","Marsh","Maskell","Mathew","Maxey","May","McCann","McDermott","McNamara","Mellor","Merrell","Miller","Mills","Mitchell","Mockford","Modise","Moller","Monk","Moore","Morgan","Mori","Morsello","Mortensen","Morton","Mould","Mullen","Murtagh","Nash","Needs","Newell","Newman","Nicholls","Nielsen","Nonn","Norman","Norris","Norton","O'Brian","O'Connell","Ogg","Older","Oliveras","Pagan","Page","Paknoham","Parkes","Parkin","Paterson","Patterson","Paynter","Peacock","Pearson","Peate","Pell","Perceval","Peters","Petersen","Peterson","Pickford","Pickman","Pilkington","Pilling","Pipe","Pollacco","Porter","Posen","Power","Pratchett","Price","Pritchard","Ptraci","Quinn","Ractliffe","Rafique","Ragas","Raines","Read","Rhodes","Ricca","Richards","Richardson","Rickards","Riddel","Riddle","Ridgwell","Rigby","Ritchie","Roome","Rose","Roxburgh","Rudge","Russell","Sadler","Salmon","Salter","Sanders","Sanderson","Sandland","Sapsford","Saunders","Scaife","Scatchard","Scorer","Shanahan","Shaw","Sherritt","Short","Silverston","Simkins","Simmons","Simper","Simpson","Skegg","Sledge","Smith","Smithe","Southerden","Sperry","Spurgeon","Stacey","Stamp","Stancombe","Stanley","Stanway","Stevens","Stonham","Stopps","Stout","Stratton","Styles","Sutherland","Swindell","Swinhoe","Tallis","Tamplin","Taylor","Thatcher","Theaker","Theakston","Thomas","Thompson","Thomson","Thorpe","Tompkins","Topp","Trump","Tuck","Turner","Upton","Varrier","Vowles","Waldron","Walker","Wallace","Walsh","Walters","Walton","Waterford","Waters","Watkins","Watson","Weatherwax","Webley","Welham","West","Weston","Wharfe","Whelan","White","Whitehead","Whittles","Wilkinson","Williams","Willmott","Wilson","Witt","Wolfe","Won","Woodhams","Woodhouse","Woods","Woollon","Wragg","Wright","Young"];
    return apellidos[Math.floor(Math.random()*apellidos.length)];
}
function nombreh(){
    var nombresh = ["Aaron","Alex","Alexander","Andew","Anthony","Archibald","Arthur","Barnabus","Barney","Ben","Benjamin","Bill","Bob","Bobby","Brent","Brian","Carl","Charles","Charlie","Chris","Christopher","Chuck","Clarence","Cliff","Clive","Collin","Dan","Daniel","Darren","Daryl","Dave","David","Dennis","Derek","Dilbert","Donald","Eamon","Earl","Eric","Eugene","Francis","Frank","Gareth","Garth","Gary","Geoff","Geoffrey","George","Gerald","Gerard","Gerry","Harry","Herbert","Horace","Howard","Ian","James","Jason","John","Jon","Jonathon","Joseph","Karl","Keith","Larry","Lawrence","Lionel","Luther","Marcus","Mark","Martin","Mathew","Matt","Matthew","Michael","Mike","Nathan","Nathaniel","Nick","Nicolas","Niles","Oswald","Oliver","Pat","Patrick","Paul","Peter","Phil","Phillip","Quincy","Randolph","Randy","Richard","Rincewind","Robert","Robin","Rudolph","Rupert","Sam","Samuel","Sandy","Shannon","Simon","Stephen","Steve","Steven","Tarquil","Thomas","Tim","Timmy","Timothy","Tom","Wallace","Wally","Walter","Will","William","Wilbur"];
    return nombresh[Math.floor(Math.random()*nombresh.length)];
}

function nombref(){
    var nombresf = ["Agnes","Alexandra","Alexandria","Alice","Allison","Angela","Anne","Betty","Carol","Caroline","Carrie","Cecile","Celia","Danielle","Daria","Doris","Dorothy","Ellen","Esme","Fanny","Florence","Gertrude","Gill","Gillian","Gytha","Heidi","Irene","Janet","Janice","Jasmine","Julia","Julie","Karen","Kathy","Katy","Lucile","Lucy","Magrat","Margaret","Marge","Mary","Molly","Nadine","Nancy","Olive","Pat","Patty","Paula","Pauline","Perdita","Petra","Rebecca","Ruby","Sally","Sharon","Simone","Stephanie","Susan","Tracy","Victoria","Violet"];
    return nombresf[Math.floor(Math.random() * nombresf.length)];
}
