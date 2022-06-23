input timeFrame = {default DAY, WEEK};

def H = high(period = timeFrame)[1];
def L = low(period = timeFrame)[1];
def C = close(period = timeFrame)[1];
def O = open(period = timeFrame)[1];

def calc_PP = (H + L + C) / 3;

def calc_R1 =  (2 * calc_PP) - L;
def calc_R2 = calc_PP + H - L;
def calc_R3 = H + 2 * (calc_PP - L);

def calc_S1 = (2 * calc_PP) - H;
def calc_S2 = calc_PP - H + L;
def calc_S3 = L - 2 * (H - calc_PP);

plot HI = H;
plot LO = L; 
plot CL = C;
plot OP = O;

plot R1 = calc_R1; 
plot R2 = calc_R2;
plot R3 = calc_R3;
plot PP = calc_PP;
plot S1 = calc_S1;  
plot S2 = calc_S2;
plot S3 = calc_S3;

R1.SetDefaultColor(color.orange);
R2.SetDefaultColor(color.orange);
R3.SetDefaultColor(color.orange);
S1.SetDefaultColor(color.magenta);
S2.SetDefaultColor(color.magenta);
S3.SetDefaultColor(color.magenta);

OP.SetDefaultColor(color.white);
HI.SetDefaultColor(color.green);
LO.SetDefaultColor(color.red);
CL.SetDefaultColor(color.dark_orange);


R1.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);
R2.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);
R3.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);
S1.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);
S2.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);
S3.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);

OP.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);
HI.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);
LO.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);
CL.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);

PP.DefineColor("Color", Color.CYAN);
PP.AssignValueColor(PP.color("Color"));
PP.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);