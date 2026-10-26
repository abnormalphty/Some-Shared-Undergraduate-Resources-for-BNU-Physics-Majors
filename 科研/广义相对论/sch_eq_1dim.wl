(* ::Package:: *)

ClearAll;

hBar = 1;
m = 1;
TFinal = 20.0;

L = 60;
NGrid = 2^11;
dx = 2*L/NGrid;
X = Table[-L + j*dx,{j,0,NGrid-1}];

dt = 0.01;
NSteps = Round[TFinal/dt];

xiMma = 
	N[If[EvenQ[NGrid],
		Join[Range[0,NGrid/2],Range[-NGrid/2+1,-1]],
		Join[Range[0,(NGrid - 1)/2],Range[-(NGrid-1)/2 , -1]]
		]*(Pi/L)
	];
	
(*F = 1.0;
VFunc[x_] := F*x;*)

V0 = 5.0\:ff1b
a = 2.0;
VFunc[x_] := N[If[x>=0 && x<=a,V0,0.0]];

E_Kin = 1.5;
x0 = -10.0;
sigma = 100.0;
p0 = N[Sqrt[2*m*E_Kin]];
Att = 1.0;
Psi0Func[x_] := (Att/Sqrt[sigma*Sqrt[Pi]]) *  Exp[-(x-x0)^2/(2*sigma^2)]*Exp[I*p0*x];

Psi = N[Psi0Func /@ X];
VGrid = N[VFunc /@ X];

