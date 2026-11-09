%% ------------------------------------------------------------------------
%% APARTADO 1: Definición de la función de integración numérica
%% ------------------------------------------------------------------------
% La regla del trapecio compuesta aproxima la integral mediante:
% I ≈ (h/2) * [ f(a) + 2*sum(f(x_i)) + f(b) ]  donde h = (b-a)/N
% Contenido en el script 'integral_numer.m'


%% ------------------------------------------------------------------------
%% APARTADO 2: Integrales exactas calculadas manualmente
%% ------------------------------------------------------------------------
% f1(x) = x^2                        en [0, 2]   -> Int = [x^3/3]_0^2 = 8/3
% f2(x) = cos(x)                     en [0, pi/2]-> Int = [sin(x)]_0^(pi/2) = 1
% f3(x) = 3*cos(3x)*exp(sin(3x))     en [0, pi/6]-> Int = [exp(sin(3x))]_0^(pi/6) = e^1 - e^0 = e - 1

% Definición de las funciones anónimas
f1 = @(x) x.^2;
a1 = 0; b1 = 2;
exacta1 = (2^3)/3 - (0^3)/3; % 8/3 ≈ 2.666667

f2 = @(x) cos(x);
a2 = 0; b2 = pi/2;
exacta2 = sin(pi/2) - sin(0); % 1

f3 = @(x) 3 * cos(3*x) .* exp(sin(3*x));
a3 = 0; b3 = pi/6;
exacta3 = exp(sin(3*pi/6)) - exp(sin(0)); % exp(1) - 1 ≈ 1.718282

%% ------------------------------------------------------------------------
%% APARTADOS 3 y 4: Aproximación, evaluación del error y tabla
%% ------------------------------------------------------------------------
valores_N = [10, 50, 100, 500];
num_N = length(valores_N);

% Inicializamos matrices para almacenar resultados
res_f1 = zeros(num_N, 3); % [N, Aprox, Error]
res_f2 = zeros(num_N, 3);
res_f3 = zeros(num_N, 3);

for i = 1:num_N
    N = valores_N(i);
    
    % Evaluación f1
    aprox1 = integral_numer(f1, a1, b1, N);
    err1 = abs(exacta1 - aprox1);
    res_f1(i, :) = [N, aprox1, err1];
    
    % Evaluación f2
    aprox2 = integral_numer(f2, a2, b2, N);
    err2 = abs(exacta2 - aprox2);
    res_f2(i, :) = [N, aprox2, err2];
    
    % Evaluación f3
    aprox3 = integral_numer(f3, a3, b3, N);
    err3 = abs(exacta3 - aprox3);
    res_f3(i, :) = [N, aprox3, err3];
end

% Muestra de resultados por pantalla formateados en tabla
fprintf('\n=========================================================================\n');
fprintf(' TABLA DE RESULTADOS: INTEGRACIÓN NUMÉRICA (REGLA DEL TRAPECIO COMPUESTA)\n');
fprintf('=========================================================================\n');

fprintf('\n1. Función: f1(x) = x^2 en [%.1f, %.1f] | Valor exacto: %.8f\n', a1, b1, exacta1);
fprintf('-------------------------------------------------------------\n');
fprintf('    N         Aproximación            Error Absoluto\n');
fprintf('-------------------------------------------------------------\n');
for i = 1:num_N
    fprintf('  %4d         %12.8f            %12.4e\n', res_f1(i,1), res_f1(i,2), res_f1(i,3));
end

fprintf('\n2. Función: f2(x) = cos(x) en [%.1f, pi/2] | Valor exacto: %.8f\n', a2, exacta2);
fprintf('-------------------------------------------------------------\n');
fprintf('    N         Aproximación            Error Absoluto\n');
fprintf('-------------------------------------------------------------\n');
for i = 1:num_N
    fprintf('  %4d         %12.8f            %12.4e\n', res_f2(i,1), res_f2(i,2), res_f2(i,3));
end

fprintf('\n3. Función: f3(x) = 3*cos(3x)*e^(sin(3x)) en [0, pi/6] | Valor exacto: %.8f\n', exacta3);
fprintf('-------------------------------------------------------------\n');
fprintf('    N         Aproximación            Error Absoluto\n');
fprintf('-------------------------------------------------------------\n');
for i = 1:num_N
    fprintf('  %4d         %12.8f            %12.4e\n', res_f3(i,1), res_f3(i,2), res_f3(i,3));
end
fprintf('=========================================================================\n\n');


