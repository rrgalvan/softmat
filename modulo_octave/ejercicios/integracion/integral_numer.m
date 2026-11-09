function I = integral_numer(f, a, b, N)
    % Comprobación de límites (boundary checking) de los subintervalos
    if N <= 0 || floor(N) ~= N
        error('El número de subintervalos N debe ser un entero positivo.');
    end
    
    h = (b - a) / N;
    x = linspace(a, b, N + 1);
    y = f(x);
    
    % Suma de los extremos + 2 veces los puntos intermedios
    I = (h / 2) * (y(1) + 2 * sum(y(2:end-1)) + y(end));
end

