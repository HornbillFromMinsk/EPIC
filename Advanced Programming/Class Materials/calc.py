'''NUMBER: [0-9]+;
SPACE: (' ', '/t')


expr: expr* EOF;
exp: sum '/n';
sum: mul | sum op=('+' | '-') mul;
mul: last | sum op=('*' | '/') last;
mul: last | sum op=('*' | '/') last;
'''