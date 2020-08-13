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


R1.SetDefaultColor(color.blue);
R2.SetDefaultColor(color.blue);
R3.SetDefaultColor(color.blue);
S1.SetDefaultColor(color.blue);
S2.SetDefaultColor(color.blue);
S3.SetDefaultColor(color.blue);

OP.SetDefaultColor(color.yellow);
HI.SetDefaultColor(color.yellow);
LO.SetDefaultColor(color.yellow);
CL.SetDefaultColor(color.yellow);

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
