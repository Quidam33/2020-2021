s=2;// начальное расстояние от лодки до катера
fi=3*%pi/4;
//функция, описывающая движение катера береговой охраны
function dr=f(tetha, r)
dr=r/sqrt(3);
endfunction;
//начальные условия в случае 2
r0=s;
tetha0=-%pi;
tetha=0:0.01:2*%pi;
r=ode(r0,tetha0,tetha,f);
//функция, описывающая движение лодки браконьеров
function xt=f2(t)
xt=tan(fi)*t;
endfunction
t=0:1:800;
polarplot(tetha,r,style = color('green')); //построение траектории
plot2d(t,f2(t),style = color('red'));


make pandoc "presentation.md" -F pandoc-crossref --pdf-engine=lualatex --number-sections -t beamer --slide-level=2 -o "presentation.pdf"