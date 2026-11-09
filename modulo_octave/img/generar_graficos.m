%% Script para generar las imágenes de las transparencias Beamer
% Genera y exporta en formato PNG todas las gráficas descritas en las diapositivas.

clear; clc; close all;

% Directorio de salida (opcional: se guardarán en la misma carpeta del script)
% Si se prefiere crear una carpeta específica, descomentar la siguiente línea:
% if ~exist('img', 'dir'), mkdir('img'); end

%% ------------------------------------------------------------------------
%% 1. Plot 2D básico (Diapositivas I y II) -> plot-exp-sin.png
%% ------------------------------------------------------------------------
figure(1);
x = linspace(0, 20, 100); 
y = exp(-x ./ 100) .* sin(x);

plot(x, y);

% Exportar a PNG
print('-dpng', '-r300', 'plot-exp-sin.png');
fprintf('Generada: plot-exp-sin.png\n');

%% ------------------------------------------------------------------------
%% 2. Plot 2D con etiquetas (Diapositivas III y IV) -> abanico2.png
%% ------------------------------------------------------------------------
figure(2);
plot(x, y);

% Atributos agregados a la ventana activa
title('Una funcion cualquiera'); 
xlabel('Tiempo'); 
ylabel('Amplitud');

% Exportar a PNG
print('-dpng', '-r300', 'abanico2.png');
fprintf('Generada: abanico2.png\n');

%% ------------------------------------------------------------------------
%% 3. Plot 2D múltiple con estilos y leyenda (Diapositivas V y VI) -> plot-exp-sin-cos.png
%% ------------------------------------------------------------------------
figure(3);
x_m = linspace(0, 20, 50);

% Curvas con distintos estilos (puntos ':' y línea con triángulos '-^')
set(0, 'DefaultLineLineWidth', 1.5);   % Grosor de las curvas
plot(x_m, exp(x_m / 10) .* sin(x_m), ':', ...
     x_m, exp(x_m / 10) .* cos(x_m), '-^'); 

% Leyenda
legend('exp(x/10)*sin(x)', 'exp(x/10)*cos(x)');

% Exportar a PNG (en las transparencias ponía .eps, adaptado a PNG como pides)
print('-dpng', '-r300', 'plot-exp-sin-cos.png');
fprintf('Generada: plot-exp-sin-cos.png\n');

%% ------------------------------------------------------------------------
%% 4. Curvas 3D con plot3 -> plot3.png
%% ------------------------------------------------------------------------
figure(4);
t = 0:0.1:10*pi;
x_3d = (1 + sin(t)) .* cos(t);
y_3d = (1 + sin(t)) .* sin(t);
z_3d = t;

plot3(x_3d, y_3d, z_3d);

% Exportar a PNG
print('-dpng', '-r300', 'plot3.png');
fprintf('Generada: plot3.png\n');

%% ------------------------------------------------------------------------
%% 5. Superficies 3D con mesh, view y colorbar -> mesh-3d.png
%% ------------------------------------------------------------------------
figure(5);
[X, Y] = meshgrid(-pi:0.1:pi, -pi:0.1:pi);

% Nota: En el texto de las transparencias se indica f(x,y)=sin(x)*cos(y),
% pero en el código de la transparencia pone z=sin(x).*sin(y). Se mantiene el código:
Z = sin(X) .* sin(Y);

mesh(X, Y, Z);

% Ajuste de perspectiva y barra de color
view(30, 60);
colorbar('East');

% Exportar a PNG
print('-dpng', '-r300', 'mesh-3d.png');
fprintf('Generada: mesh-3d.png\n');

%%-------------------------------------------------
%% 6. Curvas de nivel
%% ------------------------------------------------------------------------

[x, y] = meshgrid(-pi:0.1:pi, -pi:0.1:pi);
z = sin ( x ) .* sin ( y ) ;
contourf (x ,y , z ) ;

% Exportar a PNG
print('-dpng', '-r300', 'contour.png');
fprintf('Generada: mesh-3d.png\n');

%% Finalización
fprintf('\n¡Todas las imágenes PNG han sido generadas correctamente!\n');
