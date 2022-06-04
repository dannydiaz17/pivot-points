# WeeklyMonthlyPivots_TS
# http://thinkscripter.wordpress.com
# thinkscripter@gmail.com
# Last Update 20 APR 2009

input timeFrame = {default WEEK, MONTH};
input showOnlyToday = no;

plot R3;
plot R2;
plot R1;
plot PP;
plot S1;
plot S2;
plot S3;

plot OP;
plot HI;
plot LO;
plot CL;


R3 = ;
R2 = ;
R1 = ;
PP = ;
S1 = ;
S2 = ;
S3 = ;

OP = ;
HI = ;
LO = ;
CL = ;


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
