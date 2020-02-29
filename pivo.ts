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

R3 = ;
R2 = ;
R1 = ;
PP = ;
S1 = ;
S2 = ;
S3 = ;

R1.SetDefaultColor(color.red);
R2.SetDefaultColor(color.red);
R3.SetDefaultColor(color.red);
S1.SetDefaultColor(color.red);
S2.SetDefaultColor(color.red);
S3.SetDefaultColor(color.red);

R1.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);
R2.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);
R3.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);
S1.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);
S2.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);
S3.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);

PP.DefineColor("Color", Color.CYAN);
PP.AssignValueColor(PP.color("Color"));
PP.SetPaintingStrategy(PaintingStrategy.HORIZONTAL);
